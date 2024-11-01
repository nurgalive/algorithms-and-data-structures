class SipHash:
    def __init__(self, key):
        self.key = key
        # Initialize internal state variables
        self.v0 = 0x736f6d6570736575
        self.v1 = 0x646f72616e646f6d
        self.v2 = 0x6c7967656e657261
        self.v3 = 0x7465646279746573
        # Initialize the counter
        self.counter = 0
        # Initialize magic constants
        self.c0 = 0x0706050403020100
        self.c1 = 0x0f0e0d0c0b0a0908
        self.c2 = 0x1716151413121110
        self.c3 = 0x1f1e1d1c1b1a1918

    def _compress(self, message_block):
        # XOR message block with magic constants
        v0 = self.v0 ^ message_block
        # Round 1
        v2 = self.v2 ^ self.c0
        v0 += v2
        v1 = self.v1 + self.v3
        v2 = ((v2 << 16) & 0xFFFFFFFFFFFFFFFF) | (v2 >> 48)
        v3 = (self.v3 >> 32)
        v2 ^= v0
        v3 ^= v1
        v0 = v0 << 32
        # Round 2
        v1 = v1 ^ self.c1
        v0 += v3
        v1 += v2
        v3 = ((v3 << 12) & 0xFFFFFFFFFFFFFFFF) | (v3 >> 52)
        v2 = (v2 >> 32)
        v2 ^= v0
        v3 ^= v1
        v0 = v0 << 32
        # Round 3
        v2 = v2 ^ self.c2
        v0 += v1
        v2 += v3
        v1 = ((v1 << 8) & 0xFFFFFFFFFFFFFFFF) | (v1 >> 56)
        v3 = (v3 >> 32)
        v1 ^= v2
        v3 ^= v0
        v0 = v0 << 32
        # Round 4
        v3 = v3 ^ self.c3
        v1 += v0
        v3 += v2
        v0 = (v0 >> 32)
        v2 = ((v2 << 7) & 0xFFFFFFFFFFFFFFFF) | (v2 >> 57)
        v0 ^= v1
        v2 ^= v3
        # Finalization
        v1 ^= self.key
        v3 ^= self.key
        v1 += v2
        v3 += v0
        v2 += v1
        v0 += v3
        # Combine the final state variables
        result = v0 ^ v1 ^ v2 ^ v3
        return result

    def hash(self, message):
        # Pad the message if necessary
        message += b'\x80'  # Append a single '1' bit
        while len(message) % 8 != 0:
            message += b'\x00'  # Append '0' bits until the length is a multiple of 8
        # Process message blocks
        hash_result = 0
        for i in range(0, len(message), 8):
            block = int.from_bytes(message[i:i+8], byteorder='little')
            hash_result = self._compress(block)
        return hash_result


# Example usage:
key = 0x0123456789abcdef
message = b"Hello, world!"
siphash = SipHash(key)
hash_value = siphash.hash(message)
print("SipHash of message:", hex(hash_value))
print("Decimal value:", hash_value)