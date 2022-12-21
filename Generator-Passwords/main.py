#Passwo Generator
#Author: Arslon Erkinov

import secrets
import string

def create_pw(pw_length=24):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    alphobet = letters + digits + special_chars
    passwd = ''
    pw_strong = False

    while not pw_strong:
        passwd = ''
        for i in range(pw_length):
            passwd += ''.join(secrets.choice(alphobet))
        if (any(char in special_chars for char in passwd) and sum(char in digits for char in passwd) >= 2):
            pw_strong = True
        return passwd

if __name__ == '__main__':
    print(create_pw())