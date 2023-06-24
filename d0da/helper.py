"""
Helper functions for D0DA protocol
"""


def create_packets(payload, packet_size, packets):
    """
    Create (fragment) packets from payload of packet_size
    """
    total_size = packet_size * packets
    for i in range(0, total_size, packet_size):
        if i < total_size:
            buf = payload[i : i + packet_size]
        else:
            buf = b""

        yield buf + b"\x00" * (packet_size - len(buf))


def chunk_bytes(value, bit_length):
    """
    Chunk value into bytes of bit_length
    """
    for _ in range(0, value.bit_length(), bit_length):
        yield value & ((1 << bit_length) - 1)
        value >>= bit_length


def one_is_more_encode(values):
    """
    Encode value into bytes with 7 bits of payload and 1 bit
    which indicates the continuation.
    """
    result = bytearray()
    for value in values:
        if value == 0:
            result.append(0)
        else:
            first = True
            for byte in chunk_bytes(value, 7):
                if first:
                    first = False
                else:
                    result[-1] ^= 1 << 7
                result.append(byte)
    return bytes(result)


def encode_color(red, green, blue):
    """
    Encode RGB bytes into two bytes.
    """
    encode = 0
    encode |= (red & 0xF8) << 8
    encode |= (green & 0xFC) << 3
    encode |= (blue & 0xF8) >> 3
    return encode


def ensure_size(values, size, default):
    if len(values) < size:
        values += (default,) * (size - len(values))
    if len(values) > size:
        values = values[:size]
    return values
