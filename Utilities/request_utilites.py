from pwn import *
import numpy as np

State= np.array
def get_cypher_texts(host:str, port:int)->State:
    cyphertexts= []
    with open('ciphertexts.txt', 'w') as file:
        for x in range(256):
            # Format the input string
            input_str = f'{x:02x}' + '000000000000000000000000000000'
            
            # Connect to the server
            conn = remote(host, port)
            
            # Send the input text
            conn.recvuntil(b'Enter plain text as hex string : ')
            conn.sendline(input_str.encode())
            
            # Receive and parse the output
            output = conn.recvall().decode()
            
            # Extract the ciphertext from the output
            lines = output.split('\n')
            for line in lines:
                if 'ciphertext' in line:
                    ciphertext = line.split(': ')[1]
                    cyphertexts.append(ciphertext)
                    file.write(f'{input_str} : {ciphertext}\n')
            
            # Close the connection
            conn.close()
    cyphertexts= np.array(cyphertexts)
    np.save('ciphertexts.npy', cyphertexts)
    return cyphertexts