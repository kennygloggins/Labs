def prompt(num=0):
    if num == 0:
        text = input('What do you want to be encrypted?')
        shift = input('Enter in your shift number(1-25):')
        if 0 < int(shift) < 26:
            crypt = encrypt(text, shift)
            if crypt:
                print(crypt)
        else:
            prompt(1)
    else:
        text = input('Enter a valid string:')
        shift = input('Enter in a valid shift number(1-25):')
        if 0 < int(shift) < 26:
            crypt = encrypt(text, shift)
            if crypt:
                print(crypt)
        else:
            prompt(1)

def encrypt(text, shift):
    crypt = ''
    shift = int(shift)
    try:
        for char in text:
            if char.isalpha():
                if char.islower() and ord(char)+shift < 123:
                    crypt += chr(ord(char)+shift)
                elif char.islower():
                    temp = 123 - (ord(char) + shift)
                    crypt += chr(97 + abs(temp))
                elif char.isupper() and ord(char)+shift < 91:
                    crypt += chr(ord(char)+shift)
                elif char.isupper():
                    temp = 91 - (ord(char) + shift)
                    crypt += chr(65 + abs(temp))
            elif 32 <= ord(char) < 65:
                temp = 65 - (ord(char) + shift)
                crypt += chr(32 + abs(temp))
            else:
                raise
        return crypt
    except:
        prompt(1)
        
prompt()