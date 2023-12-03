def shift_bytes_right(input_bytes, shift_amount):
    shifted_bytes = bytes((byte + shift_amount) % 256 for byte in input_bytes)
    return shifted_bytes


original_string = open('win_injection.py', 'rb').read()

shifted_string = shift_bytes_right(original_string, 6)
print("\n_______________________Right Shifted String:")
print(shifted_string)
