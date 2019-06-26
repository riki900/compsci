"""
    one time pad encryption
"""

from secrets import token_bytes
from typing import Tuple

BIG_ENDIANNESS: str = 'big'
CHARS_TO_STRIP: str = '\0'

def random_key(length: int) -> int:
    tb: bytes = token_bytes(length)
    return int.from_bytes(tb,BIG_ENDIANNESS)

def encrypt(message: str) -> Tuple[int, int]:
    message_bytes = message.encode()
    one_type_key: int = random_key(len(message))
    message_key: int = int.from_bytes(message_bytes,BIG_ENDIANNESS)
    encrypted: int = message_key ^ one_type_key
    return one_type_key, encrypted

def decrypt(one_time_key: int, message_key: int) -> str:
    decrypted: int = one_time_key ^ message_key
    temp: bytes = decrypted.to_bytes(decrypted.bit_length() + 7 // 8, BIG_ENDIANNESS)
    # return string without leading nulls
    return temp.decode().strip(CHARS_TO_STRIP)

if __name__ == "__main__":
    msg_txt = '  Attack at dawn  '
    one_time_key, message_key = encrypt(msg_txt)
    result: str = decrypt(one_time_key,message_key)
    assert msg_txt == result
    print('Terminado - OK')