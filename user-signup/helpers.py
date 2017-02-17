def alphabet_position(letter):
    #must get char and return int
    alphabet={'a':0, 'b':1, 'c':2, 'd':3,'e':4,'f':5, 'g':6,
     'h':7, 'i':8, 'j':9, 'k':10, 'l':11,'m':12, 'n':13,
     'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,
     'v':21,'w':22,'x':23,'y':24,'z':25 }
    letter=letter.lower()
    char_pos=alphabet.get(letter)
    return char_pos

#take char and int and return char
def rotate_character(char, rot):
    alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    if char.isalpha():
        char_pos=alphabet_position(char)
        new_char_pos=char_pos+rot
        if new_char_pos<=25:
            final_char=alpha[new_char_pos]
            return final_char
        else:
            new_char_pos=new_char_pos%26
            final_char=alpha[new_char_pos]
            return final_char

    else:
        return char
