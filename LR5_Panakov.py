# Good Luck!
def encode(string):
    encoded_bits = ""
    for char in string:
        binary = format(ord(char), '08b')
        tripled = ''.join(bit * 3 for bit in binary)
        encoded_bits += tripled
    return encoded_bits


def decode(bits):
    corrected_bits = ""
    for i in range(0, len(bits), 3):
        triple = bits[i:i+3]
        if triple.count('1') > 1:
            corrected_bits += '1'
        else:
            corrected_bits += '0'

    decoded_string = ""
    for i in range(0, len(corrected_bits), 8):
        byte = corrected_bits[i:i+8]
        ascii_value = int(byte, 2)
        decoded_string += chr(ascii_value)
    
    return decoded_string