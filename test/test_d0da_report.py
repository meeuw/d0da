"""
Test data sent from Wootility captured using Wireshark
"""
import struct
import d0da.d0da_report_pb2
import d0da.d0da_report


def test_decode_report():
    """
    Test decode report
    """
    report_data = bytes.fromhex(
        """
        d0 da 0e 00 c9 0a 41 0a 3f 9c f0 03 9c f0 03 9c
        f0 03 9c f0 03 9c f0 03 9c f0 03 9c f0 03 9c f0
        03 9c f0 03 9c f0 03 99 f2 03 99 f2 03 96 f3 03
        96 f3 03 96 f3 03 96 f3 03 96 f3 03 96 f3 03 96

        f3 03 96 f3 03 96 f3 03 0a 41 0a 3f 9c f0 03 9c
        f0 03 9c f0 03 9c f0 03 9c f0 03 9c f0 03 9c f0
        03 9c f0 03 9c f0 03 9c f0 03 99 f2 03 99 f2 03
        96 f3 03 96 f3 03 96 f3 03 96 f3 03 96 f3 03 96

        f3 03 96 f3 03 96 f3 03 96 f3 03 0a 41 0a 3f 9c
        f0 03 9c f0 03 9c f0 03 9c f0 03 9c f0 03 9c f0
        03 9c f0 03 9c f0 03 9c f0 03 9c f0 03 99 f2 03
        99 f2 03 96 f3 03 96 f3 03 96 f3 03 96 f3 03 96

        f3 03 96 f3 03 96 f3 03 96 f3 03 96 f3 03 00 00
        00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        """
    )
    assert report_data[:2] == d0da.d0da_report.D0DA
    assert report_data[2] == 0x0E  # RgbProfileColorsPart1
    d0da_length = struct.unpack("!H", report_data[3:5])[0]
    assert d0da_length > 0
    rgb_rows = d0da.d0da_report_pb2.RGBRows()
    rgb_rows.ParseFromString(report_data[5 : 5 + d0da_length])
    for row in rgb_rows.payload:
        print(d0da.helper.one_is_more_decode(row.row))
    assert report_data[5 + d0da_length :] == b"\x00" * 50
