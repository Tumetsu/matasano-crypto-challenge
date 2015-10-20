import base64
import binascii

def hexTobase64(hexvalue):
    bstring = binascii.unhexlify(hexvalue)
    return base64.b64encode(bstring).decode("ascii")

if __name__ == "__main__":
    print(hexTobase64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"))