#Mary Kate Sheehan
#12/5/2023
#Lab 12 Question 3


CODE = {'A': ')', 'a': '0', 'B': '(', 'b': '9', 'C': '*', 'c': '8',
        'D': '&', 'd': '7', 'E': '^', 'e': '6', 'F': '%', 'f': '5',
        'G': '$', 'g': '4', 'H': '#', 'h': '3', 'I': '@', 'i': '2',
        'J': '!', 'j': '1', 'K': 'Z', 'k': 'z', 'L': 'Y', 'l': 'y',
        'M': 'X', 'm': 'x', 'N': 'W', 'n': 'w', 'O': 'V', 'o': 'v',
        'P': 'U', 'p': 'u', 'Q': 'T', 'q': 't', 'R': 'S', 'r': 's',
        'S': 'R', 's': 'r', 'T': 'Q', 't': 'q', 'U': 'P', 'u': 'p',
        'V': 'O', 'v': 'o', 'W': 'N', 'w': 'n', 'X': 'M', 'x': 'm',
        'Y': 'L', 'y': 'l', 'Z': 'K', 'z': 'k', '!': 'J', '1': 'j',
        '@': 'I', '2': 'i', '#': 'H', '3': 'h', '$': 'G', '4': 'g',
        '%': 'F', '5': 'f', '^': 'E', '6': 'e', '&': 'D', '7': 'd',
        '*': 'C', '8': 'c', '(': 'B', '9': 'b', ')': 'A', '0': 'a',
        ':': ',', ',': ':', '?': '.', '.': '?', '<': '>', '>': '<',
        "'": '"', '"': "'", '+': '-', '-': '+', '=': ';', ';': '=',
        '{': '[', '[': '{', '}': ']', ']': '}'}

def encrypt(input_file, encrypt_file, code_dict):
    with open(input_file, 'r') as file_in:
        content = file_in.read()

    encrypted_content = ''
    for char in content:
        encrypted_content += code_dict.get(char, char)

    with open(encrypt_file, 'w') as file_out:
        file_out.write(encrypted_content)

    print(encrypted_content)
    
input_file = 'text.txt'
encrypt_file = 'encrypted_text.txt'
encrypt(input_file, encrypt_file, CODE)


def decrypt(encrypt_file, code_dict):
    with open(encrypt_file, 'r') as file_in:
        encrypted_content = file_in.read()

    decrypted_content = ''
    for char in encrypted_content:
        decrypted_content += code_dict.get(char, char)

    print(decrypted_content)

decrypt(encrypt_file, CODE)


   
        
    
