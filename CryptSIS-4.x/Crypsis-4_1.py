__author__ = 'RetR0'



from os import urandom
import os
import blowfish
import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes


to_do = input ("\n1 - Encrpytion\n2 - Decryption\n\n99 - Return to NOTHING\n\n\nPlease enter a number : ")

if to_do == "1":
    try:
        da_text_to_do_something_with = input ("\nEnter the name of the file to crypt :")
        with open (da_text_to_do_something_with, 'rb') as f_file_to_crypt:
            text_block = f_file_to_crypt.read()
    except:
        print ("\n")
        print ("Error while reading the file\n")
        input ("(press enter to continue)")
    some_random_shit_to_make_it_work = ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~     \n░░▒▒▓▓Crypt_SIS▓▓▒▒░░\n\n")
    some_random_shit_to_make_it_work = some_random_shit_to_make_it_work.encode('utf-8')
    text_block = bytearray(some_random_shit_to_make_it_work + text_block)
    print (text_block)

if to_do == "2":
    try:
        text = input ("\nEnter the name of the file to decrypt :")
        with open (text, 'rb') as f_file_to_crypt:
            text_block = f_file_to_crypt.read()
    except:
        print ("\n")
        print ("Error while reading the file\n")
        input ("(press enter to continue)")
        exit(-1)

output = input ("\nEnter the output file name :")


def blowfish_round_encryption ():

    key1_input = input ("\nImport the fisrt BLOW key file to use or leave empty to create one :")

    if len(key1_input) > 0:
        with open (key1_input, 'rb') as f_key1file:
            rawkey = f_key1file.read()
        iv_1 = bytes(rawkey[:8])
        key_1 = bytes(rawkey [8:])

    elif len(key1_input) == 0 :
            iv_1 = os.urandom(8)                
            key_1 = os.urandom(56)
            key1_input = input("\nEnter the name of the first BLOW key file to create : ")
            with open (key1_input, 'wb') as f_key1file:
                f_key1file.write(iv_1 + key_1)

    key2_input = input ("\nImport the second BLOW key file to use or leave empty to create one :")

    if len(key2_input) > 0:
        with open (key2_input, 'rb') as f_key2file:
            rawkey = f_key2file.read()
        iv_2 = bytes(rawkey[:8])
        key_2 = bytes(rawkey [8:])

    elif len(key2_input) == 0 :
            iv_2 = os.urandom(8)                
            key_2 = os.urandom(56)
            key2_input = input("\nEnter the name of the second BLOW key file to create : ")
            with open (key2_input, 'wb') as f_key2file:
                f_key2file.write(iv_2 + key_2)

    key3_input = input ("\nImport the third BLOW key file to use or leave empty to create one :")

    if len(key3_input) > 0:
        with open (key3_input, 'rb') as f_key3file:
            rawkey = f_key3file.read()
        iv_3 = bytes(rawkey[:8])
        key_3 = bytes(rawkey [8:])

    elif len(key3_input) == 0 :
            iv_3 = os.urandom(8)                
            key_3 = os.urandom(56)
            key3_input = input("\nEnter the name of the third BLOW key file to create : ")
            with open (key3_input, 'wb') as f_key3file:
                f_key3file.write(iv_3 + key_3)

    hashnsalt_1 = blowfish.Cipher(key_1)
    hashnsalt_2 = blowfish.Cipher(key_2)
    hashnsalt_3 = blowfish.Cipher(key_3)

    try:
        data_result_1 = b"".join(hashnsalt_1.encrypt_cfb(text_block, iv_1))
        print ("\nRound 1 : SUCCESS")
    except:
        print ("\nRound 1 : FAIL")
    try:
        data_result_2 = b"".join(hashnsalt_2.encrypt_cfb(data_result_1, iv_2))
        print ("\nRound 2 : SUCCESS")
    except:
        print ("\nRound 2 : FAIL")
    try:
        global final_data_result_1 
        final_data_result_1 = b"".join(hashnsalt_3.encrypt_cfb(data_result_2, iv_3))
        print ("\nRound 3 : SUCCESS")
    except:
        print ("\nRound 3 : FAIL")

def AES_round_encryption ():

    key1_input = input ("\nImport the fisrt AES key file to use or leave empty to create one :")

    if len(key1_input) > 0:
        with open (key1_input, 'rb') as f_key1file:
            key_1 = f_key1file.read()
        
    elif len(key1_input) == 0 :           
        key_1 = get_random_bytes(32)
        key1_input = input("\nEnter the name of the first AES key file to create : ")
        with open (key1_input, 'wb') as f_key1file:
            f_key1file.write(key_1)

    key2_input = input ("\nImport the second AES key file to use or leave empty to create one :")

    if len(key2_input) > 0:
        with open (key2_input, 'rb') as f_key2file:
            key_2 = f_key2file.read()

    elif len(key2_input) == 0 :           
        key_2 = get_random_bytes(32)
        key2_input = input("\nEnter the name of the second AES key file to create : ")
        with open (key2_input, 'wb') as f_key2file:
            f_key2file.write(key_2)
    
    key3_input = input ("\nImport the third AES key file to use or leave empty to create one :")

    if len(key3_input) > 0:
        with open (key3_input, 'rb') as f_key3file:
            key_3 = f_key3file.read()

    elif len(key3_input) == 0 :           
        key_3 = get_random_bytes(32)
        key3_input = input("\nEnter the name of the third AES key file to create : ")
        with open (key3_input, 'wb') as f_key3file:
            f_key3file.write(key_3)

    cipher_1 = AES.new(key_1, AES.MODE_CBC)
    data_result_1 = cipher_1.encrypt(pad(final_data_result_1, AES.block_size))
    cipher_2 = AES.new(key_2, AES.MODE_CBC)
    data_result_2 = cipher_2.encrypt(pad(data_result_1, AES.block_size))
    cipher_3 = AES.new(key_3, AES.MODE_CBC)    

    global final_data_result_2
    final_data_result_2 = cipher_3.encrypt(pad(data_result_2, AES.block_size))


def AES_round_decryption ():

    key1_input = input ("\nImport the fisrt AES key file to use :")

    with open (key1_input, 'rb') as f_key1file:
        key_1 = f_key1file.read()

    key2_input = input ("\nImport the second AES key file to use :")

    with open (key2_input, 'rb') as f_key2file:
        key_2 = f_key2file.read()

    key3_input = input ("\nImport the third AES key file to use :")

    with open (key3_input, 'rb') as f_key3file:
        key_3 = f_key3file.read()

    try:
        iv_3 = text_block [:16]
        encrypted_data = text_block [16:]
        cipher_3 = AES.new(key_3, AES.MODE_CBC, iv=iv_3)
        data_result_1 = unpad(cipher_3.decrypt(encrypted_data), AES.block_size)

        print ("\nRound 1 : SUCCESS")
        print ("\n")
        print (data_result_1)
    except:
        print ("\nRound 1 : FAILED")

    try:
        iv_2 = data_result_1 [:16]
        encrypted_data = data_result_1 [16:]
        cipher_2 = AES.new(key_2, AES.MODE_CBC, iv=iv_2)
        data_result_2 = unpad(cipher_2.decrypt(encrypted_data), AES.block_size)

        print ("\nRound 2 : SUCCESS")
        print ("\n")
        print (data_result_2)
    except:
        print ("\nRound 2 : FAIL")

    try:
        iv_1 = data_result_2 [:16]
        encrypted_data = data_result_2 [16:]
        cipher_1 = AES.new(key_1, AES.MODE_CBC, iv=iv_1)
        global final_data_result_1
        final_data_result_1 = unpad(cipher_1.decrypt(encrypted_data), AES.block_size)

        print ("\nRound 3 : SUCCESS")
        print ("\n")
        print (final_data_result_1)
    except:
        print ("\nRound 3 : FAIL")



def blowfish_round_decryption ():

    key1_input = input ("\nImport the fisrtv BLOW key file to use :")

    with open (key1_input, 'rb') as f_key1file:
        rawkey = f_key1file.read()
    iv_1 = bytes(rawkey[:8])
    key_1 = bytes(rawkey [8:])

    key2_input = input ("\nImport the second BLOW key file to use :")

    with open (key2_input, 'rb') as f_key2file:
        rawkey = f_key2file.read()
    iv_2 = bytes(rawkey[:8])
    key_2 = bytes(rawkey [8:])

    key3_input = input ("\nImport the third BLOW key file to use :")

    with open (key3_input, 'rb') as f_key3file:
        rawkey = f_key3file.read()
    iv_3 = bytes(rawkey[:8])
    key_3 = bytes(rawkey [8:])


    hashnsalt_1 = blowfish.Cipher(key_1)
    hashnsalt_2 = blowfish.Cipher(key_2)
    hashnsalt_3 = blowfish.Cipher(key_3)

    try:
        data_result_1 = b"".join(hashnsalt_3.decrypt_cfb(final_data_result_1, iv_3))
        print (data_result_1)
        print ("\nRound 1 : SUCCESS")
    except:
        print ("\nRound 1 : FAILED")
    try:
        data_result_2 = b"".join(hashnsalt_2.decrypt_cfb(data_result_1, iv_2))
        print (data_result_2)
        print ("\nRound 2 : SUCCESS")
    except:
        print ("\nRound 2 : FAILED")
    try:
        global final_data_result_2
        final_data_result_2 = b"".join(hashnsalt_1.decrypt_cfb(data_result_2, iv_1))
        print (final_data_result_2)
        print ("\nRound 3 : SUCCESS")
    except:
        print ("\nRound 3 : FAILED")


if to_do == "1":
    blowfish_round_encryption()
    AES_round_encryption()
    try:
        with open(output, 'wb') as f_output:
            f_output.write(final_data_result_2)
            print ("\n")
            print ("################DATA ENCRYPTED################\n")
            input ("(press enter to continue)")
    except: 
        print ("\n")
        input ("Error while encrypting failed (press enter to continue)")

if to_do == "2":
    AES_round_decryption()
    blowfish_round_decryption()
    try:
        with open(output, 'wb') as f_output:
            f_output.write(final_data_result_2)
            print ("\n")
            print ("################DATA DECRYPTED################\n")
            input ("(press enter to continue)")
    except: 
        print ("\n")
        input ("Error while decrypting failed (press enter to continue)")
