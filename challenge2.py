from challenge1 import hexTobase64
import binascii

def xorhex(hex1, hex2):
   return hex(int(hex1, 16) ^ int(hex2, 16))


if __name__ == "__main__":
    print(xorhex("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965"))
