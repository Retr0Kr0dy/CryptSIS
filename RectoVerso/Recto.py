__author__ = 'RetR0'

import os
from re import X
import win32api
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes
import getpass
import ctypes

cwd = os.getcwd()
username = getpass.getuser()
initial_path = input("Enter the folder name to crypt : ")
initial_path = cwd + "\\" + initial_path
final_path = input("Enter the final folder name : ")
final_path = cwd + "\\" + final_path 
key = get_random_bytes (32)
count = []

def encrypt_legit():
    counter = 0
    path = initial_path
    f_path = final_path
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            if '.' in file:
                files.append(os.path.join(r, file))
                count.append(file)
    for f in files:
        print(f)
        try:
            with open (f, 'rb') as f_file_to_encrypt:
                        text_block = f_file_to_encrypt.read()
        except:
            print("brooooo")
            continue    
        cipher = AES.new(key, AES.MODE_CBC)
        data_result = cipher.encrypt(pad(text_block, AES.block_size))
        try:
            xxx = count[counter]
            output = f_path + "\\" + xxx
            print (output)
            with open(output, 'wb') as f_output:
                f_output.write(cipher.iv)
                f_output.write(data_result)
        except:
            print("BRUHH")
        counter = counter + 1
    with open("key.key", 'wb') as f_key:
        f_key.write(key)   
encrypt_legit() 
