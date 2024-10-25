from pwn import *
import numpy as np
import subprocess

State= np.array
def get_cypher_texts(host:str, port:int)->State:
    cyphertexts= []
    with open('ciphertexts.txt', 'w') as file:

        for x in range(256):
            # Format the input string
            input_str = f'{x:02x}' + '000000000000000000000000000000'
            
            # Run the binary and connect to its stdin/stdout
            oracle = subprocess.Popen(
                ['oracle/encrypt.bin'],          # Path to the binary
                stdin=subprocess.PIPE,      # Use PIPE for input
                stdout=subprocess.PIPE,     # Use PIPE for output
                stderr=subprocess.PIPE      # Use PIPE for errors if needed
            )
            
            # Send the input string and get output
            stdout, stderr = oracle.communicate(input=f'{input_str}\n'.encode())
            
            # Decode output and parse ciphertext
            output = stdout.decode()
            lines = output.split('\n')
            for line in lines:
                if 'ciphertext' in line:
                    ciphertext = line.split(': ')[1]
                    cyphertexts.append(ciphertext)
                    file.write(f'{ciphertext}\n')
    cyphertexts= np.array(cyphertexts)
    np.save('ciphertexts.npy', cyphertexts)
    return cyphertexts