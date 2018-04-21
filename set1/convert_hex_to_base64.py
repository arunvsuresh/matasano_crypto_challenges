import base64

def convert_hex_to_base64(hex_string):
    decoded_str = hex_string.decode(encoding="hex")
    return base64.b64encode(decoded_str)
