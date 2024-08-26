from Utilities.tables import *
from Utilities.inverse_SBOX import *
def xor(w1: bytes, w2: bytes) -> bytes:
    return bytes([i ^ j for i, j in zip(w1, w2)])

def inv_rot_word(word: bytes) -> bytes:
    if len(word) != 4:
        raise ValueError(f"Wrong word length: {len(word)}")
    return bytes([word[-1]]) + word[:-1]

def inv_sub_word(word: bytes) -> bytes:
    if len(word) != 4:
        raise ValueError(f"Wrong word length: {len(word)}")
    return bytes([inverseSbox[b] for b in word])

def _r_con(n: int) -> bytes:
    if not 0 <= n < 256:
        raise ValueError(f"Wrong n: {n}")
    return bytes([LOOKUP_TABLE[n], 0, 0, 0])

def reverse_key_expansion(last_round_key: bytes, rounds: int) -> bytes:
    if len(last_round_key) != 16:
        raise ValueError(f"Wrong key length: {len(last_round_key)}")
    
    expanded_key = [last_round_key[i:i+4] for i in range(0, len(last_round_key), 4)]
    
    for r in range(rounds, 0, -1):
        temp = expanded_key[0]
        temp = inv_rot_word(temp)
        temp = inv_sub_word(temp)
        temp = xor(temp, _r_con(r))
        expanded_key = [xor(temp, expanded_key[-1])] + expanded_key[:-1]
        for i in range(1, 4):
            expanded_key[i] = xor(expanded_key[i], expanded_key[i-1])
    
    original_key = b''.join(expanded_key)
    return original_key