import re
import bitstring

from exceptions import ReadByteStringException
from models import BitTypes

VERSION_REGEX = re.compile(
    r"\+\+Fortnite\+Release\-(?P<major>\d+)\.(?P<minor>\d*)"
)


class ConstBitStreamWrapper(bitstring.ConstBitStream):
    def __init__(self, auto=None, length=None, offset=None, pos=0, **kwargs):
        super().__init__(auto, length, offset, pos, **kwargs)

    def skip_bytes(self, count):
        """Skip the next count bytes"""
        self.bytepos += count

    def read_uint8(self):
        """Read and interpret next 8 bits as an unassigned integer"""
        return self.read(BitTypes.UINT8.value)

    def read_uint16(self):
        """Read and interpret next 16 bits as an unassigned integer"""
        return self.read(BitTypes.UINT_16.value)

    def read_uint32(self):
        """Read and interpret next 32 bits as an unassigned integer"""
        return self.read(BitTypes.UINT_32.value)

    def read_int32(self):
        """Read and interpret next 32 bits as an signed integer"""
        return self.read(BitTypes.INT_32.value)

    def read_uint64(self):
        """Read and interpret next 64 bits as an unassigned integer"""
        return self.read(BitTypes.UINT_64.value)

    def read_float32(self):
        """Read and interpret next 32 bits as a float"""
        return self.read(BitTypes.FLOAT_LE_32.value)

    def read_byte(self):
        """Read and interpret next bit as an integer"""
        return int.from_bytes(
            self.read(BitTypes.BYTE.value), byteorder="little"
        )

    def read_bytes(self, size):
        """Read and interpret next bit as an integer"""
        return self.read("bytes:" + str(size))

    def read_bool(self):
        """Read and interpret next 32 bits as an boolean"""
        return self.read_uint32() == 1

    def hextostring(self, i):
        s = hex(i)[2:]
        return s if len(s) == 2 else f"0{s}"

    def read_guid(self):
        """Read and interpret next 16 bits as a guid"""
        return "".join(self.hextostring(i) for i in self.read("bytes:16"))

    def read_array(self, f):
        """Read an array where the first 32 bits indicate the length of the array"""
        length = self.read_uint32()
        return [f() for _ in range(length)]

    def read_tuple_array(self, f1, f2):
        """Read an tuple array where the first 32 bits indicate the length of the array"""
        length = self.read_uint32()
        return [(f1(), f2()) for _ in range(length)]

    def read_string(self):
        """Read and interpret next i bits as a string where i is determined defined by the first 32 bits"""
        size = self.read_int32()

        if size == 0:
            return ""

        is_unicode = size < 0

        if is_unicode:
            size *= -2
            return self.read_bytes(size)[:-2].decode("utf-16")

        stream_bytes = self.read_bytes(size)
        string = stream_bytes[:-1]
        if stream_bytes[-1] != 0:
            raise ReadByteStringException()

        try:
            return string.decode("utf-8")
        except UnicodeDecodeError:
            return string.decode("latin-1")
