import numpy as np
import galois
from Utilities.inverse_SBOX import get_inverse_SBOX

inverseSbox= get_inverse_SBOX()

State= np.array
def reverse_mix_column(state: State)->State:
    GF = galois.GF(2**8)
    return np.linalg.inv(GF(state))

def reverse_shift_rows(state: State) -> State:
    new_state = np.array(state, dtype=int)
    for i in range(4):
        new_state[i] = np.roll(new_state[i], i)
    return new_state

def inverse_SBOX(state: State)->State:
    toret= np.zeros_like(state)
    for i in range(state.shape[0]):
        for j in range(state.shape[1]):
            # Replace the value with the corresponding inverseSbox value
            toret[i, j] = inverseSbox[state[i, j]]
    return toret