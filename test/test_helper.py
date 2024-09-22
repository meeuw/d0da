"""
Tests for d0da.helper functions
"""
import pytest
import d0da.helper


def test_create_packets():
    """
    Test d0da.helper.create_packet
    """
    # Payload too small for first packet
    assert list(d0da.helper.create_packets(b"\x01\x02\x03\x04\x05\x06\x07", 8, 4)) == [
        b"\x01\x02\x03\x04\x05\x06\x07\x00",
        b"\x00\x00\x00\x00\x00\x00\x00\x00",
        b"\x00\x00\x00\x00\x00\x00\x00\x00",
        b"\x00\x00\x00\x00\x00\x00\x00\x00",
    ]
    # Payload too large for first packet
    assert list(
        d0da.helper.create_packets(b"\x01\x02\x03\x04\x05\x06\x07\x08\x09", 8, 4)
    ) == [
        b"\x01\x02\x03\x04\x05\x06\x07\x08",
        b"\x09\x00\x00\x00\x00\x00\x00\x00",
        b"\x00\x00\x00\x00\x00\x00\x00\x00",
        b"\x00\x00\x00\x00\x00\x00\x00\x00",
    ]
    # Payload fits exactly
    assert list(
        d0da.helper.create_packets(
            b"\x00\x01\x02\x03\x04\x05\x06\x07" b"\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f",
            8,
            2,
        )
    ) == [
        b"\x00\x01\x02\x03\x04\x05\x06\x07",
        b"\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f",
    ]


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("1111 1000 0000 0000", "1000 0000 1111 0000 0000 0011"),  # Red
        ("      111 1110 0000", "          1110 0000 0000 1111"),  # Green
        ("             1 1111", "                       1 1111"),  # Blue
        ("1111 1111 1111 1111", "1111 1111 1111 1111 0000 0011"),  # White
        ("0", "0"),  # Black
    ],
)
def test_one_is_more_encode(test_input, expected):
    """
    Test d0da.helper.one_is_more_encode
    """
    actual = d0da.helper.one_is_more_encode((int(test_input.replace(" ", ""), 2),))
    assert bin(int(actual.hex(), 16)) == f"0b{expected.replace(' ', '')}"


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ((0xFF, 0x00, 0x00), "1111100000000000"),  # Red
        ((0x00, 0xFF, 0x00), "     11111100000"),  # Green
        ((0x00, 0x00, 0xFF), "           11111"),  # Blue
        ((0xFF, 0xFF, 0xFF), "1111111111111111"),  # White
    ],
)
def test_encode_color(test_input, expected):
    """
    Test d0da.helper.encode_color
    """
    actual = d0da.helper.encode_color(*test_input)
    assert bin(actual) == f"0b{expected.replace(' ', '')}"


@pytest.mark.parametrize(
    "rgb",
    [
        (0xF8, 0x00, 0x00),
        (0x00, 0xF8, 0x00),
        (0x00, 0x00, 0xF8),
    ],
)
def test_encode_decode_color(rgb):
    """
    Test d0da.helper.decode_color
    """
    assert d0da.helper.decode_color(d0da.helper.encode_color(*rgb)) == rgb
