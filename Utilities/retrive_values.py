import numpy as np
from Utilities.reverse_utilities_function import reverse_shift_rows, reverse_mix_column, inverse_SBOX


def get_x1(ciphertexts: np.array):
    #guessing one x1
    valueforx1:int
    for x1 in range(0,256*256):
        key=f'c7c1{x1:04x}28c500004c8e000064ce0000'
        key_bytes = bytes.fromhex(key)
        xor_results= []
        # XOR each ciphertext with the key
        for ct in ciphertexts:
            ciphertext_bytes = bytes.fromhex(ct)
            xor_result = bytes(a ^ b for a, b in zip(ciphertext_bytes, key_bytes))
            xor_results.append(xor_result)
        #here we got 256 cipher text
        #now from here we will convert from one line string to matrices
        xor_results_array= np.array([list(ct) for ct in xor_results])

        after_mix_column= [ct.reshape(4, 4, order='F') for ct in xor_results_array]
        #now for a pariticular x1 we have all the possible cyphertexts here
        #now we need to reverse the mix column

        reverse_mix_columns=[]
        for matrice in after_mix_column:
            if np.linalg.det(matrice)!=0:
                reverse_mix_columns.append(reverse_mix_column(matrice))
        #now we have reversed the mix columns, now our task is to find the
        #reverse shift bytes

        reversed_shiftRow = []
        for matrice in reverse_mix_columns:
            reversed_shiftRow.append(reverse_shift_rows(matrice))

        #after getting the shift rows, i need to reverse the subbytes
        reverse_subbytes = []
        for matrice in reversed_shiftRow:
            reverse_subbytes.append(inverse_SBOX(matrice))

        # here we got the reverse_subbytes. Now at this point i need to to
        # xor of every correspoinding element ie.

        val1=0
        val2=0
        val3=0
        val4=0
        for matrice in reverse_subbytes:
            val1 ^= matrice[0][0]
            val2 ^= matrice[1][3]
            val3 ^= matrice[2][2]
            val4 ^= matrice[3][1]
        if(val1==0 and val2==0 and val3==0 and val4==0):
            valueforx1= x1
            break
    return valueforx1

def get_x2(ciphertexts: np.array, x1:int)->int:
    #guessing one x2
    valueforx2:int
    for x2 in range(0,256*256):
        key=f'c7c1{x1:04x}28c5{x2:04x}4c8e000064ce0000'
        key_bytes = bytes.fromhex(key)
        xor_results= []
        # XOR each ciphertext with the key
        for ct in ciphertexts:
            ciphertext_bytes = bytes.fromhex(ct)
            xor_result = bytes(a ^ b for a, b in zip(ciphertext_bytes, key_bytes))
            xor_results.append(xor_result)
        #here we got 256 cipher text
        #now from here we will convert from one line string to matrices
        xor_results_array= np.array([list(ct) for ct in xor_results])

        after_mix_column= [ct.reshape(4, 4, order='F') for ct in xor_results_array]
        #now for a pariticular x1 we have all the possible cyphertexts here
        #now we need to reverse the mix column

        reverse_mix_columns=[]
        for matrice in after_mix_column:
            if np.linalg.det(matrice)!=0:
                reverse_mix_columns.append(reverse_mix_column(matrice))
        #now we have reversed the mix columns, now our task is to find the
        #reverse shift bytes

        reversed_shiftRow = []
        for matrice in reverse_mix_columns:
            reversed_shiftRow.append(reverse_shift_rows(matrice))

        #after getting the shift rows, i need to reverse the subbytes
        reverse_subbytes = []
        for matrice in reversed_shiftRow:
            reverse_subbytes.append(inverse_SBOX(matrice))

        # here we got the reverse_subbytes. Now at this point i need to to
        # xor of every correspoinding element ie.

        val1=0
        val2=0
        val3=0
        val4=0
        for matrice in reverse_subbytes:
            val1 ^= matrice[0][1]
            val2 ^= matrice[1][0]
            val3 ^= matrice[2][3]
            val4 ^= matrice[3][2]
        if(val1==0 and val2==0 and val3==0 and val4==0):
            valueforx2= x2
            break
    return valueforx2

def get_x3(ciphertexts: np.array, x1:int, x2:int)->int:
    #guessing one x1
    valueforx3:int
    for x3 in range(0,256*256):
        key=f'c7c1{x1:04x}28c5{x2:04x}4c8e{x3:0x4}64ce0000'
        key_bytes = bytes.fromhex(key)
        xor_results= []
        # XOR each ciphertext with the key
        for ct in ciphertexts:
            ciphertext_bytes = bytes.fromhex(ct)
            xor_result = bytes(a ^ b for a, b in zip(ciphertext_bytes, key_bytes))
            xor_results.append(xor_result)
        #here we got 256 cipher text
        #now from here we will convert from one line string to matrices
        xor_results_array= np.array([list(ct) for ct in xor_results])

        after_mix_column= [ct.reshape(4, 4, order='F') for ct in xor_results_array]
        #now for a pariticular x1 we have all the possible cyphertexts here
        #now we need to reverse the mix column

        reverse_mix_columns=[]
        for matrice in after_mix_column:
            if np.linalg.det(matrice)!=0:
                reverse_mix_columns.append(reverse_mix_column(matrice))
        #now we have reversed the mix columns, now our task is to find the
        #reverse shift bytes

        reversed_shiftRow = []
        for matrice in reverse_mix_columns:
            reversed_shiftRow.append(reverse_shift_rows(matrice))

        #after getting the shift rows, i need to reverse the subbytes
        reverse_subbytes = []
        for matrice in reversed_shiftRow:
            reverse_subbytes.append(inverse_SBOX(matrice))

        # here we got the reverse_subbytes. Now at this point i need to to
        # xor of every correspoinding element ie.

        val1=0
        val2=0
        val3=0
        val4=0
        for matrice in reverse_subbytes:
            val1 ^= matrice[0][2]
            val2 ^= matrice[1][1]
            val3 ^= matrice[2][0]
            val4 ^= matrice[3][3]
        if(val1==0 and val2==0 and val3==0 and val4==0):
            valueforx3= x3
            break
    return valueforx3


def get_x4(ciphertexts: np.array, x1:int, x2:int, x3:int)->int:
    #guessing one x1
    valueforx4:int
    for x4 in range(0,256*256):
        key=f'c7c1{x1:04x}28c5{x2:04x}4c8e{x3:0x4}64ce{x4:0x04}'
        key_bytes = bytes.fromhex(key)
        xor_results= []
        # XOR each ciphertext with the key
        for ct in ciphertexts:
            ciphertext_bytes = bytes.fromhex(ct)
            xor_result = bytes(a ^ b for a, b in zip(ciphertext_bytes, key_bytes))
            xor_results.append(xor_result)
        #here we got 256 cipher text
        #now from here we will convert from one line string to matrices
        xor_results_array= np.array([list(ct) for ct in xor_results])

        after_mix_column= [ct.reshape(4, 4, order='F') for ct in xor_results_array]
        #now for a pariticular x1 we have all the possible cyphertexts here
        #now we need to reverse the mix column

        reverse_mix_columns=[]
        for matrice in after_mix_column:
            if np.linalg.det(matrice)!=0:
                reverse_mix_columns.append(reverse_mix_column(matrice))
        #now we have reversed the mix columns, now our task is to find the
        #reverse shift bytes

        reversed_shiftRow = []
        for matrice in reverse_mix_columns:
            reversed_shiftRow.append(reverse_shift_rows(matrice))

        #after getting the shift rows, i need to reverse the subbytes
        reverse_subbytes = []
        for matrice in reversed_shiftRow:
            reverse_subbytes.append(inverse_SBOX(matrice))

        # here we got the reverse_subbytes. Now at this point i need to to
        # xor of every correspoinding element ie.

        val1=0
        val2=0
        val3=0
        val4=0
        for matrice in reverse_subbytes:
            val1 ^= matrice[0][3]
            val2 ^= matrice[1][2]
            val3 ^= matrice[2][1]
            val4 ^= matrice[3][0]
        if(val1==0 and val2==0 and val3==0 and val4==0):
            valueforx4= x4
            break
    return valueforx4

