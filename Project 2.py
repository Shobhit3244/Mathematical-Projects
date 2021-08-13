"""2.A Caesar cipher is a simple substitution cipher based on the idea of
    shifting each letter of the plaintext message a fixed number (called the key)
    of positions in the alphabet. For example, if the key value is 2, the word "Sourpuss"
    would be encoded as "Uqwtrwuu." The original message can be recovered by "reencoding"
    it using the negative of the key
    Write a program that can encode and decode Caesar ciphers. The input to the program
    will be a string of plaintext and the value of the key. The output will be an encoded
    message where each character in the original message is replaced by shifting it key
    characters in the Unicode character set. For example, if ch is a character in the string
    and key is the amount to shift, then the character that replaces ch can be calculated
    as: chr (ord(ch) + key) .
"""

import sys


def cinput(option):
    strg = str(input("Enter String: "))
    code = int(input("Enter Code: "))

    if option == "e":
        result = encoding(strg, code)
    else:
        result = decoding(strg, code)

    return result


def encoding(text, code):
    result = ""
    for i in text:
        result += chr(ord(i)+code)
    return result


def decoding(text, code):
    result = ""
    for i in text:
        result += chr(ord(i) - code)
    return result


if __name__=="__main__":
    while True:
        print("1. Encode String \n2. Decode String \n3. Exit\n")
        opt = str(input("Enter Option of Your Choice[1, 2, 3]: "))
        if opt == '1':
            print(cinput('e')+"\n")
        elif opt == '2':
            print(cinput("")+"\n")
        elif opt == '3':
            break
        else:
            print("\nPlease Select Any one of the Following options:\n")

    sys.exit()
