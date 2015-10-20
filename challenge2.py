from challenge1 import hexTobase64
import binascii

def xorhex(hex1, hex2):
   return hex(hex1 ^ hex2)


if __name__ == "__main__":
    print(xorhex(0x1c0111001f010100061a024b53535009181c, 0x686974207468652062756c6c277320657965))
