class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet

    def encode(self, text):
        encoded_string = ""
        current_password_index = 0
        for char in text:
            if char not in self.alphabet:
                encoded_string += char
                continue
            if current_password_index == len(self.key):
                current_password_index = 0
            shift_offset = self.alphabet.index(self.key[current_password_index])
            current_password_index += 1
            debug_index = self.alphabet.index(char) + shift_offset
            while debug_index > len(self.alphabet):
                debug_index = debug_index - len(self.alphabet)
            encoded_string += self.alphabet[debug_index]
        return encoded_string

    def decode(self, text):
        decoded_string = ""
        current_password_index = 0
        for char in text:
            if char not in self.alphabet:
                decoded_string += char
                continue
            if current_password_index == len(self.key):
                current_password_index = 0
            shift_offset = self.alphabet.index(self.key[current_password_index])
            current_password_index += 1
            debug_index = self.alphabet.index(char) - shift_offset
            while debug_index > len(self.alphabet):
                debug_index = debug_index - len(self.alphabet)
            decoded_string += self.alphabet[debug_index]
        return decoded_string
