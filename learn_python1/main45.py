# message Encroption program in python

import random 
import string

enc= " " +string.punctuation+string.digits+string.ascii_letters
enc=list(enc)
key =enc.copy()
random.shuffle(key)

 # Encrypt 

text=input("enter the message to encrypt:")
enc_text=""

for letter in text:
    index = enc.index(letter)
    enc_text+=key[index]
print(f"original message:{text}")
print(f"enc message:{enc_text}")

# DECRYPT

enc_text=input("enter the message to decrypt:")
text=""

for letter in enc_text:
    index = key.index(letter)
    text+=enc[index]
print(f"enc message:{enc_text}")
print(f"original message:{text}")
