from helpers import alphabet_position, rotate_character
from sys import argv, exit

def user_input_is_valid(cl_args):
    if len(cl_args)>1 and cl_args[1].isdigit():
        return True
    else:
        return False

def encrypt(text, rot):
    encry=""
    for char in text:
        rot=int(rot)
        new_char=rotate_character(char, rot)
        if char==char.upper():
            new_char=new_char.upper()
        encry=encry+new_char
    return encry

def main():
    if user_input_is_valid(argv)==True:
        rot=argv[1]
    else:
        print("usage: python3 caesar.py n")
        exit()
    letter=str(input("Type a message: \n"))
    print(encrypt(letter, rot))


if __name__ == '__main__':
    main()
