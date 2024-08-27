import time


class CaesarCipher:
    @staticmethod
    def encode(text):
        result = ""
        for char in text:
            if char.isalpha():
                if char.isupper():
                    result += chr((ord(char) - 65 + 1) % 26 + 65)
                else:
                    result += chr((ord(char) - 97 + 1) % 26 + 97)
            else:
                result += char
        return result

    @staticmethod
    def decode(text):
        result = ""
        for char in text:
            if char.isalpha():
                if char.isupper():
                    result += chr((ord(char) - 65 - 1) % 26 + 65)
                else:
                    result += chr((ord(char) - 97 - 1) % 26 + 97)
            else:
                result += char
        return result


def main():
    input_file_name = (
        "input_file.txt"  # Assume input file name is always "input_file.txt"
    )
    try:
        with open(input_file_name, "r") as input_file:
            text = input_file.read()
    except FileNotFoundError:
        print("Input file not found.")
        return

    caesar = CaesarCipher()

    print("Encoding text...")
    time.sleep(5)  # Introduce a 5-second delay
    encoded_text = caesar.encode(text)
    output_file_name = (
        "encoding_file.txt"  # Assume output file name is always "encoding_file.txt"
    )
    with open(output_file_name, "w") as output_file:
        output_file.write(encoded_text)
    print("Text has been encrypted and saved to 'encoding_file.txt'.")

    print("Decoding text...")
    time.sleep(5)  # Introduce a 5-second delay
    decoded_text = caesar.decode(encoded_text)
    decoded_file_name = "decoding_file.txt"
    with open(decoded_file_name, "w") as decoded_file:
        decoded_file.write(decoded_text)
    print("Decoded text saved into 'decoding_file.txt'.")


if __name__ == "__main__":
    main()
