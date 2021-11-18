__author__ = 'RetR0'



from os import urandom
import os
import blowfish
import sys


to_do = input ("\n1 - Encrpytion\n2 - Decryption\n\n99 - Return to NOTHING\n\n\nPlease enter a number : ")
text = input ("\nEnter the name of the file to crypt :")
output = input ("\nEnter the output file name :")

if to_do == "1":

    key1_input = input ("\nImport the fisrt key file to use or leave empty to create one :")

    if len(key1_input) > 0:
        with open (key1_input, 'rb') as f_key1file:
            rawkey = f_key1file.read()
        iv_1 = bytes(rawkey[:8])
        key_1 = bytes(rawkey [8:])

    elif len(key1_input) == 0 :
            iv_1 = os.urandom(8)                
            key_1 = os.urandom(56)
            key1_input = input("\nEnter the name of the first key file to create : ")
            with open (key1_input, 'wb') as f_key1file:
                f_key1file.write(iv_1 + key_1)

    key2_input = input ("\nImport the second key file to use or leave empty to create one :")

    if len(key2_input) > 0:
        with open (key2_input, 'rb') as f_key2file:
            rawkey = f_key2file.read()
        iv_2 = bytes(rawkey[:8])
        key_2 = bytes(rawkey [8:])

    elif len(key2_input) == 0 :
            iv_2 = os.urandom(8)                
            key_2 = os.urandom(56)
            key2_input = input("\nEnter the name of the second key file to create : ")
            with open (key2_input, 'wb') as f_key2file:
                f_key2file.write(iv_2 + key_2)

    key3_input = input ("\nImport the third key file to use or leave empty to create one :")

    if len(key3_input) > 0:
        with open (key3_input, 'rb') as f_key3file:
            rawkey = f_key3file.read()
        iv_3 = bytes(rawkey[:8])
        key_3 = bytes(rawkey [8:])

    elif len(key3_input) == 0 :
            iv_3 = os.urandom(8)                
            key_3 = os.urandom(56)
            key3_input = input("\nEnter the name of the third key file to create : ")
            with open (key3_input, 'wb') as f_key3file:
                f_key3file.write(iv_3 + key_3)


if to_do == "2":

    key1_input = input ("\nImport the fisrt key file to use :")

    with open (key1_input, 'rb') as f_key1file:
        rawkey = f_key1file.read()
    iv_1 = bytes(rawkey[:8])
    key_1 = bytes(rawkey [8:])

    key2_input = input ("\nImport the second key file to use :")

    with open (key2_input, 'rb') as f_key2file:
        rawkey = f_key2file.read()
    iv_2 = bytes(rawkey[:8])
    key_2 = bytes(rawkey [8:])

    key3_input = input ("\nImport the third key file to use :")

    with open (key3_input, 'rb') as f_key3file:
        rawkey = f_key3file.read()
    iv_3 = bytes(rawkey[:8])
    key_3 = bytes(rawkey [8:])


hashnsalt_1 = blowfish.Cipher(key_1)
hashnsalt_2 = blowfish.Cipher(key_2)
hashnsalt_3 = blowfish.Cipher(key_3)


with open (text, 'rb') as f_file_to_crypt:
    text_block = f_file_to_crypt.read()


if to_do == "1":   
        try:
            data_result_1 = b"".join(hashnsalt_1.encrypt_cfb(text_block, iv_1))
            print ("\nRound 1 SUCCESS")
        except:
            print ("\nRound 1 ERROR")
        try:
            data_result_2 = b"".join(hashnsalt_2.encrypt_cfb(data_result_1, iv_2))
            print ("\nRound 2 SUCCESS")
        except:
            print ("\nRound 2 ERROR")
        try:
            final_data_result = b"".join(hashnsalt_3.encrypt_cfb(data_result_2, iv_3))
            print ("\nRound 3 SUCCESS")
        except:
            print ("\nRound 3 ERROR")

if to_do == "2":
        try:
            data_result_1 = b"".join(hashnsalt_3.decrypt_cfb(text_block, iv_3))
            print ("\nRound 1 SUCCESS")
        except:
            print ("\nRound 1 ERROR")
        try:
            data_result_2 = b"".join(hashnsalt_2.decrypt_cfb(data_result_1, iv_2))
            print ("\nRound 2 SUCCESS")
        except:
            print ("\nRound 2 ERROR")
        try:
            final_data_result = b"".join(hashnsalt_1.decrypt_cfb(data_result_2, iv_1))
            print ("\nRound 3 SUCCESS")
        except:
            print ("\nRound 3 ERROR")

else:
    print ("Invalid option")


with open (output, 'wb') as f_output:
    f_output.write(final_data_result)



#version 2.secret.1
