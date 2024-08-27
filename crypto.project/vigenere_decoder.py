def generate_vigenere_table():
    """Generate the Vigenère cipher table."""
    table = []
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(alphabet)):
        row = alphabet[i:] + alphabet[:i]
        table.append(row)
    return table

def vigenere_decrypt(ciphertext, keyword):
    """Decrypt ciphertext using the Vigenère cipher with the provided keyword."""
    # Prepare the Vigenère cipher table
    table = generate_vigenere_table()
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    # Convert inputs to uppercase
    ciphertext = ciphertext.upper()
    keyword = keyword.upper()
    
    # Remove non-alphabetic characters from ciphertext
    ciphertext = ''.join(filter(str.isalpha, ciphertext))
    
    # Extend the keyword to match the length of the ciphertext
    keyword_repeated = (keyword * (len(ciphertext) // len(keyword) + 1))[:len(ciphertext)]
    
    # Decrypt the ciphertext
    plaintext = []
    for c, k in zip(ciphertext, keyword_repeated):
        row = alphabet.index(k)
        col = alphabet.index(c)
        plaintext_char = table[row][col]
        plaintext.append(plaintext_char)
    
    return ''.join(plaintext)

def main():
    encoding_file = 'encoding_file'
    decoding_file = 'decoding_file'
    
    # Read ciphertext from file
    try:
        with open(encoding_file, 'r') as file:
            ciphertext = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{encoding_file}' does not exist.")
        return
    
    # Prompt for the keyword
    keyword = input("Enter the keyword for decryption: ")
    
    # Decrypt the ciphertext
    plaintext = vigenere_decrypt(ciphertext, keyword)
    
    # Write the plaintext to the output file
    with open(decoding_file, 'w') as file:
        file.write(plaintext)
    
    print(f"Decrypted text has been written to '{decoding_file}'")

if __name__ == "__main__":
    main()
