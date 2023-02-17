"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

from .. import TelemMessages

class JetsonMovementRequest(object):
    __slots__ = ["header", "req", "crc"]

    __typenames__ = ["TelemMessages.Header", "boolean", "byte"]

    __dimensions__ = [None, None, [4]]

    def __init__(self):
        self.header = TelemMessages.Header()
        self.header.flag = 0x7e
        self.header.type = 0x1
        self.header.length = bytes([ 0x0, 0x1 ])
        self.req = False
        self.crc = b""

    def encode(self):
        buf = BytesIO()
        buf.write(JetsonMovementRequest._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        assert self.header._get_packed_fingerprint() == TelemMessages.Header._get_packed_fingerprint()
        self.header._encode_one(buf)
        buf.write(struct.pack(">b", self.req))
        buf.write(bytearray(self.crc[:4]))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != JetsonMovementRequest._get_packed_fingerprint():
            raise ValueError("Decode error")
        return JetsonMovementRequest._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = JetsonMovementRequest()
        self.header = TelemMessages.Header._decode_one(buf)
        self.req = bool(struct.unpack('b', buf.read(1))[0])
        self.crc = buf.read(4)
        return self
    _decode_one = staticmethod(_decode_one)

    def _get_hash_recursive(parents):
        if JetsonMovementRequest in parents: return 0
        newparents = parents + [JetsonMovementRequest]
        tmphash = (0x2136108187a868eb+ TelemMessages.Header._get_hash_recursive(newparents)) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff) + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if JetsonMovementRequest._packed_fingerprint is None:
            JetsonMovementRequest._packed_fingerprint = struct.pack(">Q", JetsonMovementRequest._get_hash_recursive([]))
        return JetsonMovementRequest._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

    def get_hash(self):
        """Get the LCM hash of the struct"""
        return struct.unpack(">Q", JetsonMovementRequest._get_packed_fingerprint())[0]

