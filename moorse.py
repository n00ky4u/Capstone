
# Python program to implement Morse Code Translator 
  
''' 
VARIABLE KEY 
'cipher' -> 'stores the morse translated form of the english string' 
'decipher' -> 'stores the english translated form of the morse string' 
'citext' -> 'stores morse code of a single character' 
'i' -> 'keeps count of the spaces between morse characters' 
'message' -> 'stores the string to be encoded or decoded' 
'''
  
# Dictionary representing the morse code chart 
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 
  
# Function to encrypt the string 
# according to the morse code chart 
def en():
    message=input("Enter the plain text!\n")
    message=message.upper()
    cipher = '' 
    for letter in message: 
        if letter != ' ': 
  
            # Looks up the dictionary and adds the 
            # correspponding morse code 
            # along with a space to separate 
            # morse codes for different characters 
            cipher += MORSE_CODE_DICT[letter] + ' '
        else: 
            # 1 space indicates different characters 
            # and 2 indicates different words 
            cipher += ' '
  
    print(cipher) 
  
# Function to decrypt the string 
# from morse to english 
def dec(): 

    message=input("Enter the cipher text!\n")
    # extra space added at the end to access the 
    # last morse code 
    message += ' '
  
    decipher = '' 
    citext = '' 
    for letter in message: 
  
        # checks for space 
        if (letter != ' '): 
  
            # counter to keep track of space 
            i = 0
  
            # storing morse code of a single character 
            citext += letter 
  
        # in case of space 
        else: 
            # if i = 1 that indicates a new character 
            i += 1
  
            # if i = 2 that indicates a new word 
            if i == 2 : 
  
                 # adding space to separate words 
                decipher += ' '
            else: 
  
                # accessing the keys using their values (reverse of encryption) 
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT 
                .values()).index(citext)] 
                citext = '' 
  
    print(decipher) 
  
 

def morse():
    n=input("Enter 1 for encryption and 2 for decryption!\n")
    if(n=='1'):
        en()
    elif(n=='2'):
        dec()
    

