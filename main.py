from Utilities.request_utilites import get_cypher_texts
from Utilities.inverse_SBOX import get_inverse_SBOX
from Utilities.retrive_values import *
from Utilities.reverse_key_expansion import *

import os
import numpy as np


# Check if the file exists
if os.path.exists('ciphertexts.npy'):
    # Load the data from the file
    ciphertexts_array = np.load('ciphertexts.npy')
    print("Loaded data from 'ciphertexts.npy'")
else:
    # Retrieve the data using the getdata function
    Host = '10.21.235.223'
    Port = 8765
    ciphertexts_array = get_cypher_texts(Host, Port)
    # Save the data to 'ciphertexts.npy'
    np.save('ciphertexts.npy', ciphertexts_array)
    print("Retrieved data using getdata() and saved to 'ciphertexts.npy'")
inverseSbox = get_inverse_SBOX()

# initializing the key
key = f'c7c1000028c500004c8e000064ce0000'
print(f'Currently the guessed key is: {key}')
# for the first section of 0000 ,say x1
value_for_x1 = get_x1(ciphertexts_array)

key = f'c7c1{value_for_x1:04x}28c500004c8e000064ce0000'
print(f'After searching for the last two values of first columns we got key as')
print(key)

# now for the second part
value_for_x2 = get_x2(ciphertexts_array, value_for_x1)

key = f'c7c1{value_for_x1:04x}28c5{value_for_x2:04x}4c8e000064ce0000'
print(f'After searching for the last two values of second columns we got key as')
print(key)


# now for the third part
value_for_x3 = get_x3(ciphertexts_array, value_for_x1, value_for_x2)

key = f'c7c1{value_for_x1:04x}28c5{value_for_x2:04x}4c8e{value_for_x3:04x}64ce0000'
print(f'After searching for the last two values of third columns we got key as')
print(key)

# now for the third part
value_for_x4 = get_x4(ciphertexts_array, value_for_x1,
                      value_for_x2, value_for_x3)

key = f'c7c1{value_for_x1:04x}28c5{value_for_x2:04x}4c8e{value_for_x3:04x}64ce{value_for_x4:04x}'
print(f'After searching for the last two values of third columns we got key as')
print(key)


# now that we have recived the last round key
# we now need to reverse it through the key expansion

final_key = reverse_key_expansion(key, 4)
print(f'value of x1= {value_for_x1:0x04}')
print(f'value of x2= {value_for_x2:0x04}')
print(f'value of x3= {value_for_x3:0x04}')
print(f'value of x4= {value_for_x4:0x04}')
print(f'First round key is ={final_key}')
