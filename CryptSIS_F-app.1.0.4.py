__author__ = 'RetR0'


from hashlib import sha256
from os import urandom
import hashlib
import os
import blowfish
import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes


def main ():
    
    print ("\n")
    print ("""             -._.                   .,ad88888ba,.
        _____   '8',             .,ad8888888888888a,
     ,'888,'     '88',          d8P²²²98888P²²²98888b, 
   ,'8888,\       |88|          9b    d8888,    `9888B   
   \8888888\      |88|         ,d88aaa8888888b,,,d888P'  
    \8/^ \88\    ,'8,         d8888888888888888888888b  
          \88\  ,'8,'        d888888P""98888888888888P  
    /88~-._\.8'88,'          88888P'    9888888888888  
   /888_8_8_8~8\             `98P'       9888888888P'     
  /88/'      \88\                         `"9888P"' 
  \8/         \8/'                                  by Krdÿ.  """)    
    print (" ___________________________________________________________\n*************************************************************")
    print (""" ██████╗██████╗ ██╗   ██╗██████╗ ████████╗███████╗██╗███████╗
██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔════╝██║██╔════╝
██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ███████╗██║███████╗
██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ╚════██║██║╚════██║
╚██████╗██║  ██║   ██║   ██║        ██║   ███████║██║███████║
 ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝   ╚══════╝╚═╝╚══════╝""")
    print ("*************************************************************")
    print (" Encrypt/Decrpyt Using different Ciphers, Version F-app1.0.4")
    print (" -----------------------------------------------------------")

    to_do = input ("\nSelect a Cipher.\n\n1 - SHA256/utf-8\n2 - Blowfish\n3 - AES-256-CBC (cryptodome)\n4 - 2x3 (secret cipher shhhhhhhh)\n\n99 - Exit\n\nPlease enter a number : ")
    if to_do == "1":
        verion1cipher()
    
    if to_do == "2":
        version2cipher()

    if to_do == "3":
        version3cipher()

    if to_do == "4":
        version4cipher()

    # da_exit = (to_do == "99" or to_do == "exit" or to_do == "quit")

    if to_do == "99" or to_do == "exit" or to_do == "quit" or to_do == "bye":
        exit(-1)

    else:
        print ("\n")
        input ("Error : Invalid Option (press enter to continue)")
        main()


def verion1cipher ():

    print ("\n**********************SHA256/utf-8***************************")
    print ("*************************************************************")
    print ("""\n╔═══════════════════════════════════════════════════════════╗
║ Two way encryption using simple XOR operation with a      ║
║ raw text key and SHA256/utf-8 encoding.                   ║
║                                                           ║ 
║                                                           ║ 
║ For decryption, remake the same process, this script is   ║
║ only using XOR opertaion, to make it simple ;             ║
║                                                           ║ 
║      raw_text = 1 0 1 0 0 1 (random binary value)         ║
║           key = 0 1 1 0 1 0 (random binary value)         ║
║  encrypt_text = 0 0 1 1 0 0 (1;1=1 0;0=1 1;0=0 0;1=0)     ║
║           key = 0 1 1 0 1 0 (random binary value)         ║
║  decrypt_text = 1 0 1 0 0 1 (same math)                   ║
║                                                           ║ 
║ As you can see, data came back to it original state by    ║
║ being run through the key a second time.                  ║
║                                                           ║ 
║                                                           ║ 
║ Usage :                                                   ║ 
║ First, you got to specify wich file you want to encrypt,  ║
║ then you specify the name of the output file,             ║
║ last you got to enter the key you want to use in raw text ║
║ (you can't save the key).                                 ║
╚═══════════════════════════════════════════════════════════╝\n""")

    to_do = input ("\n1 - Encryption/Decryption\n\n99 - Return to previous menu\n\n\nPlease enter a number : ")

    if to_do == "1":
        i = 0
        file_to_crypt = input ("\nEnter the name of the file to encrypt/decrypt :")
        output = input ("\nEnter the output file name :")
        word_key = input ("\nEnter the key in raw text : ")

        pre_keys = sha256(word_key.encode('utf-8')).digest()
        hash_keys = hashlib.sha512(pre_keys)
        hash_digest = hash_keys.hexdigest()
        keys = sha256(hash_digest.encode('utf-8')).digest()

        with open (file_to_crypt, 'rb') as f_file_to_crypt:
            text_block = f_file_to_crypt.read()
            text_block_2 = bytes()
        for i in range (len(text_block)):
            c = text_block[i]
            j = i % len(keys)
            b = bytes ([c^keys[j]])
            text_block_2 = text_block_2 + b

        with open (output, 'wb') as f_output:
            f_output.write(text_block_2)

    if to_do == "99":
        main()

    else:
        print ("\n")
        input ("Error : Invalid Option (press enter to continue)")
        verion1cipher()


    #version 1.4 (modified)



def version2cipher ():

    print ("\n************************Blowfish*****************************")
    print ("*************************************************************")
    print ("""\n╔═══════════════════════════════════════════════════════════╗
║ Encryption/Decryption using the Blowfish Cipher.          ║
║ (no Authentification).                                    ║
║                                                           ║ 
║ Blowfish a block cipher, meaning that it divides a        ║
║ message up into fixed length blocks during encryption     ║
║ and decryption.                                           ║
║                                                           ║ 
║ Usage :                                                   ║ 
║ First, you got to specify wich file you want to encrypt,  ║
║ then you specify the name of the output file,             ║
║ last you got to create a key file or use an existant key  ║
║ file.                                                     ║
╚═══════════════════════════════════════════════════════════╝\n""")

    to_do = input ("\n1 - Encrpytion\n2 - Decryption\n\n99 - Return to previous menu\n\n\nPlease enter a number : ")
    if to_do == "1":
        text = input ("Enter the name of the file to crypt :")
        output = input ("\nEnter the output file name :")
        keyfile = input ("\nImport a key file to use or leave empty to create one :")
        if len(keyfile) > 0:
            iv = os.urandom(8)                
            key = os.urandom(56)
            keyfile = keyfile
            try :
                with open (keyfile, 'rb') as f_keyfile:
                    rawkey = f_keyfile.read()
                iv = bytes(rawkey[:8])
                key = bytes(rawkey [8:])
            except EnvironmentError:
                print ("\n")
                input ("Error : Input/Output (press enter to continue)")
                version2cipher()    

        elif len(keyfile) == 0 :
            iv = os.urandom(8)                
            key = os.urandom(56)
            keyfile = input("\nEnter the name of the key file to create : ")
            try:
                with open (keyfile, 'wb') as f_keyfile:
                    f_keyfile.write(iv + key)
            except EnvironmentError:
                print ("\n")
                input ("Error : Invalid filename (press enter to continue)")
                version2cipher()  

    if to_do == "2":
        text = input ("Enter the name of the file to decrypt :")
        output = input ("\nEnter the output file name :")
        keyfile = input ("\nEnter the name of the key file to use : ")
        try:
            with open (keyfile, 'rb') as f_key:
                rawkey = f_key.read()
                iv = bytes(rawkey[:8])
                key = bytes(rawkey [8:])
        except EnvironmentError:
            print ("\n")
            input ("Error : Keyfile not found (press enter to continue)")
            version2cipher()  

    if to_do == "99":
        main()        

    else:
        print ("\n")
        input ("Error : Invalid Option (press enter to continue)")
        version2cipher()

    hashnsalt = blowfish.Cipher(key)
    with open (text, 'rb') as f_file_to_crypt:
        text_block = f_file_to_crypt.read()

    match to_do:   
        case "1":
            data_result = b"".join(hashnsalt.encrypt_cfb(text_block, iv))
            print ("\n")
            print ("################DATA ENCRYPTED################")
            input ("(press enter to continue)")

        case "2":
            data_result = b"".join(hashnsalt.decrypt_cfb(text_block, iv))
            print ("\n")
            print ("################DATA DECRYPTED################")
            input ("(press enter to continue)")

    with open (output, 'wb') as f_output:
        f_output.write(data_result)

    #version 2.6 (modified)



def version3cipher ():
    print ("\n******************AES-256-CBC (cryptodome)*******************")
    print ("*************************************************************")
    print ("""\n╔═══════════════════════════════════════════════════════════╗
║ Encryption/Decryption using AES-256-CBC by pyCryptodome.  ║
║ (no Authentification).                                    ║
║                                                           ║ 
║ The AES algorithm (also known as the Rijndael algorithm)  ║
║ is a symmetrical block cipher algorithm that takes plain  ║
║ text in blocks of 128 bits and converts them to           ║ 
║ ciphertext using different size keys.                     ║
║                                                           ║ 
║ Usage :                                                   ║ 
║ First, you got to specify wich file you want to encrypt,  ║
║ then you specify the name of the output file,             ║
║ last you got to create a key file or use an existant key  ║
║ file.                                                     ║
╚═══════════════════════════════════════════════════════════╝\n""")
    
    to_do = input ("\n1 - Encrpytion\n2 - Decryption\n\n99 - Return to previous menu\n\n\nPlease enter a number : ")
    if to_do == "1":
        text = input ("\nEnter the name of the file to crypt :")
        output = input ("\nEnter the output file name :")
        keyfile = input ("\nImport a key file to use or leave empty to create one :")
        if len(keyfile) > 0:
            try:
                with open (keyfile, 'rb') as f_key:
                    key = f_key.read()
            except:
                print ("\n")
                input ("Error : Keyfile not found (press enter to continue)")
                version3cipher()  
        if len(keyfile) == 0:
            key = get_random_bytes(32)
            keyfile = input("\nEnter the name of the key file to create : ")
            try:
                with open (keyfile, 'wb') as f_keyfile:
                    f_keyfile.write(key)
            except: 
                print ("\n")
                input ("Error : Input/Output (press enter to continue)")
                version3cipher()  
        try:
            with open (text, 'rb') as f_file_to_encrypt:
                text_block = f_file_to_encrypt.read()
        except:
            print ("\n")
            input ("Error : Input/Output (press enter to continue)")
            version3cipher() 

        cipher = AES.new(key, AES.MODE_CBC)
        data_result = cipher.encrypt(pad(text_block, AES.block_size))
        try:
            with open(output, 'wb') as f_output:
                f_output.write(data_result)
                print ("\n")
                print ("################DATA ENCRYPTED################")
                input ("(press enter to continue)")
        except: 
            print ("\n")
            input ("Error : Input/Output (press enter to continue)")
            version3cipher() 

    if to_do == "2":
        text = input ("\nEnter the name of the file to crypt :")
        output = input ("\nEnter the output file name :")
        keyfile = input ("\nImport a key file to use or leave empty to create one :")
        try:
            with open (keyfile, 'rb') as f_key:
                key = f_key.read()
        except:
            print ("Error : Key file not found")
            exit (-1)
        try:
            with open (text, 'rb') as f_file_to_decrypt:
                text_block = f_file_to_decrypt.read()
        except:
            print ("\n")
            input ("Error : Input/Output (press enter to continue)")
            version3cipher() 

        iv = text_block [:16]
        encrypted_data = text_block [16:]
        cipher = AES.new(key, AES.MODE_CBC, iv=iv)
        data_result = unpad(cipher.decrypt(encrypted_data), AES.block_size)
        try:
            with open(output, 'wb') as f_output:
                f_output.write(data_result)
                print ("\n")
                print ("################DATA DECRYPTED################")
                input ("(press enter to continue)")
        except:
            print ("\n")
            input ("Error : Input/Output (press enter to continue)")
            version3cipher() 

    if to_do == "99":
        main() 

    else:
        print ("\n")
        input ("Error : Invalid Option (press enter to continue)")
        version3cipher()

    #Version 3.5 (modified)



def version4cipher ():
    print ("\n***************2x3 (AES + BLOWFISH)(fxckd up)****************")
    print ("*************************************************************")
    print ("""\n╔═══════════════════════════════════════════════════════════╗
║ Encryption/Decryption using three AES-256-CBC key and     ║
║ three more BLOWFISH key.                                  ║
║                                                           ║ 
║ The AES algorithm (also known as the Rijndael algorithm)  ║
║ is a symmetrical block cipher algorithm that takes plain  ║
║ text in blocks of 128 bits and converts them to           ║ 
║ ciphertext using different size keys.                     ║
║                                                           ║ 
║ Blowfish a block cipher, meaning that it divides a        ║
║ message up into fixed length blocks during encryption     ║
║ and decryption.                                           ║
║                                                           ║ 
║ Usage :                                                   ║ 
║ First, you got to specify wich file you want to encrypt,  ║
║ then you specify the name of the output file,             ║
║ last you got to create 6 key file or use existant key     ║
║ file.                                                     ║
║                                                           ║ 
║ Encryption : 3 blowfish then 3 AES                        ║ 
║ Decryption : 3 AES then 3 blowfish        logic.          ║ 
╚═══════════════════════════════════════════════════════════╝\n""")

    to_do = input ("\n1 - Encrpytion\n2 - Decryption\n\n99 - Return to previous menu\n\n\nPlease enter a number : ")

    if to_do == "99":
        main()

    if to_do == "1":
        try:
            da_text_to_do_something_with = input ("\nEnter the name of the file to crypt :")
            with open (da_text_to_do_something_with, 'rb') as f_file_to_crypt:
                text_block = f_file_to_crypt.read()
        except:
            print ("\n")
            print ("Error while reading the file\n")
            input ("(press enter to continue)\n")
            
        some_random_shit_to_make_it_work = ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        some_random_shit_to_make_it_work = some_random_shit_to_make_it_work.encode('utf-8')
        text_block = bytearray(some_random_shit_to_make_it_work + text_block)

    if to_do == "2":
        try:
            text = input ("\nEnter the name of the file to decrypt :")
            with open (text, 'rb') as f_file_to_crypt:
                text_block = f_file_to_crypt.read()
        except:
            print ("\n")
            print ("Error while reading the file\n")
            input ("(press enter to continue)\n")
            exit(-1)

    output = input ("\nEnter the output file name :")

    def blowfish_round_encryption ():

        def blowfish_encryption_get_key_1 ():

            key1_input = input ("\nImport the fisrt BLOW key file to use or leave empty to create one :")

            global iv_1
            global key_1

            if len(key1_input) > 0:
                try:
                    with open (key1_input, 'rb') as f_key1file:
                        rawkey = f_key1file.read()
                    iv_1 = bytes(rawkey[:8])
                    key_1 = bytes(rawkey [8:])
                    print ("\nTarget locked")
                except:
                    print ("\nError : Key file not found")
                    blowfish_encryption_get_key_1 () 

            elif len(key1_input) == 0 :
                    iv_1 = os.urandom(8)                
                    key_1 = os.urandom(56)
                    key1_input = input("\nEnter the name of the first BLOW key file to create : ")
                    with open (key1_input, 'wb') as f_key1file:
                        f_key1file.write(iv_1 + key_1)

        blowfish_encryption_get_key_1 ()

        def blowfish_encryption_get_key_2 ():

            key2_input = input ("\nImport the second BLOW key file to use or leave empty to create one :")

            global iv_2
            global key_2

            if len(key2_input) > 0:

                try:
                    with open (key2_input, 'rb') as f_key2file:
                        rawkey = f_key2file.read()
                    iv_2 = bytes(rawkey[:8])
                    key_2 = bytes(rawkey [8:])
                    print ("\nTarget locked")
                except:
                    print ("\nError : Key file not found")
                    blowfish_encryption_get_key_2 () 

            elif len(key2_input) == 0 :
                    iv_2 = os.urandom(8)                
                    key_2 = os.urandom(56)
                    key2_input = input("\nEnter the name of the second BLOW key file to create : ")
                    with open (key2_input, 'wb') as f_key2file:
                        f_key2file.write(iv_2 + key_2)

        blowfish_encryption_get_key_2 ()

        def blowfish_encryption_get_key_3 ():

            key3_input = input ("\nImport the third BLOW key file to use or leave empty to create one :")

            global iv_3
            global key_3

            if len(key3_input) > 0:

                try:
                    with open (key3_input, 'rb') as f_key3file:
                        rawkey = f_key3file.read()
                    iv_3 = bytes(rawkey[:8])
                    key_3 = bytes(rawkey [8:])
                    print ("\nTarget locked")
                except:
                    print ("\nError : Key file not found")
                    blowfish_encryption_get_key_3 () 

            elif len(key3_input) == 0 :
                    iv_3 = os.urandom(8)                
                    key_3 = os.urandom(56)
                    key3_input = input("\nEnter the name of the third BLOW key file to create : ")
                    with open (key3_input, 'wb') as f_key3file:
                        f_key3file.write(iv_3 + key_3)

        blowfish_encryption_get_key_3 ()

        hashnsalt_1 = blowfish.Cipher(key_1)
        hashnsalt_2 = blowfish.Cipher(key_2)
        hashnsalt_3 = blowfish.Cipher(key_3)

        try:
            data_result_1 = b"".join(hashnsalt_1.encrypt_cfb(text_block, iv_1))
            print ("\nRound 1 : SUCCESS")
        except:
            print ("\nRound 1 : FAILED")
        try:
            data_result_2 = b"".join(hashnsalt_2.encrypt_cfb(data_result_1, iv_2))
            print ("\nRound 2 : SUCCESS")
        except:
            print ("\nRound 2 : FAILED")
        try:
            global final_data_result_1 
            final_data_result_1 = b"".join(hashnsalt_3.encrypt_cfb(data_result_2, iv_3))
            print ("\nRound 3 : SUCCESS")
        except:
            print ("\nRound 3 : FAILED")

    def AES_round_encryption ():

        def aes_encryption_get_key_1 ():

            key1_input = input ("\nImport the fisrt AES key file to use or leave empty to create one :")

            global key_1

            if len(key1_input) > 0:
                try:
                    with open (key1_input, 'rb') as f_key1file:
                        key_1 = f_key1file.read()
                        print ("\nTarget locked")
                except:
                    print ("\nError : Key file not found")
                    aes_encryption_get_key_1 () 
                
            elif len(key1_input) == 0 :    
                key_1 = get_random_bytes(32)
                key1_input = input("\nEnter the name of the first AES key file to create : ")
                with open (key1_input, 'wb') as f_key1file:
                    f_key1file.write(key_1)

        aes_encryption_get_key_1 ()

        def aes_encryption_get_key_2 ():

            key2_input = input ("\nImport the second AES key file to use or leave empty to create one :")

            global key_2

            if len(key2_input) > 0:

                try:
                    with open (key2_input, 'rb') as f_key2file:
                        key_2 = f_key2file.read()
                        print ("\nTarget locked")
                except:
                    print ("\nError : Key file not found")
                    aes_encryption_get_key_2 () 

            elif len(key2_input) == 0 : 
                key_2 = get_random_bytes(32)
                key2_input = input("\nEnter the name of the second AES key file to create : ")
                with open (key2_input, 'wb') as f_key2file:
                    f_key2file.write(key_2)

        aes_encryption_get_key_2 ()

        def aes_encryption_get_key_3 ():

            key3_input = input ("\nImport the third AES key file to use or leave empty to create one :")

            global key_3

            if len(key3_input) > 0:

                try:
                    with open (key3_input, 'rb') as f_key3file:
                        key_3 = f_key3file.read()
                        print ("\nTarget locked")
                except:
                    print ("\nError : Key file not found")
                    aes_encryption_get_key_3 () 

            elif len(key3_input) == 0 :
                key_3 = get_random_bytes(32)
                key3_input = input("\nEnter the name of the third AES key file to create : ")
                with open (key3_input, 'wb') as f_key3file:
                    f_key3file.write(key_3)

        aes_encryption_get_key_3 ()

        try:
            cipher_1 = AES.new(key_1, AES.MODE_CBC)
            data_result_1 = cipher_1.encrypt(pad(final_data_result_1, AES.block_size))
        
            print ("\nRound 1 : SUCCESS")
        except:
            print ("\nRound 1 : FAILED")

        try:    
            cipher_2 = AES.new(key_2, AES.MODE_CBC)
            data_result_2 = cipher_2.encrypt(pad(data_result_1, AES.block_size))
            print ("\nRound 2 : SUCCESS")
        except:
            print ("\nRound 2 : FAILED")

        try:
            cipher_3 = AES.new(key_3, AES.MODE_CBC)    
            global final_data_result_2
            final_data_result_2 = cipher_3.encrypt(pad(data_result_2, AES.block_size))
            print ("\nRound 3 : SUCCESS")
        except:
            print ("\nRound 3 : FAILED")

    def AES_round_decryption ():

        def aes_decryption_get_key_1 ():

            key1_input = input ("\nImport the fisrt AES key file to use :")

            global key_1

            try:
                with open (key1_input, 'rb') as f_key1file:
                    key_1 = f_key1file.read()
                    print ("\nTarget locked")
            except:
                print ("\nError : Key file not found")
                aes_decryption_get_key_1 () 

        aes_decryption_get_key_1 ()        

        def aes_decryption_get_key_2 ():

            key2_input = input ("\nImport the second AES key file to use :")

            global key_2

            try:
                with open (key2_input, 'rb') as f_key2file:
                    key_2 = f_key2file.read()
                    print ("\nTarget locked")
            except:
                print ("\nError : Key file not found")
                aes_decryption_get_key_2 () 

        aes_decryption_get_key_2 ()    

        def aes_decryption_get_key_3 ():

            key3_input = input ("\nImport the third AES key file to use :")

            global key_3

            try:
                with open (key3_input, 'rb') as f_key3file:
                    key_3 = f_key3file.read()
                    print ("\nTarget locked")
            except:
                print ("\nError : Key file not found")
                aes_decryption_get_key_3 () 

        aes_decryption_get_key_3 ()    

        try:
            iv_3 = text_block [:16]
            encrypted_data = text_block [16:]
            cipher_3 = AES.new(key_3, AES.MODE_CBC, iv=iv_3)
            data_result_1 = unpad(cipher_3.decrypt(encrypted_data), AES.block_size)

            print ("\nRound 1 : SUCCESS")
        except:
            print ("\nRound 1 : FAILED")

        try:
            iv_2 = data_result_1 [:16]
            encrypted_data = data_result_1 [16:]
            cipher_2 = AES.new(key_2, AES.MODE_CBC, iv=iv_2)
            data_result_2 = unpad(cipher_2.decrypt(encrypted_data), AES.block_size)

            print ("\nRound 2 : SUCCESS")
        except:
            print ("\nRound 2 : FAILED")

        try:
            iv_1 = data_result_2 [:16]
            encrypted_data = data_result_2 [16:]
            cipher_1 = AES.new(key_1, AES.MODE_CBC, iv=iv_1)
            global final_data_result_1
            final_data_result_1 = unpad(cipher_1.decrypt(encrypted_data), AES.block_size)
            final_data_result_1 = final_data_result_1 [85:]

            print ("\nRound 3 : SUCCESS")
        except:
            print ("\nRound 3 : FAILED")

    def blowfish_round_decryption ():

        def blowfish_decryption_get_key_1 ():

            key1_input = input ("\nImport the fisrt BLOW key file to use :")

            global iv_1
            global key_1

            try:
                with open (key1_input, 'rb') as f_key1file:
                    rawkey = f_key1file.read()
                iv_1 = bytes(rawkey[:8])
                key_1 = bytes(rawkey [8:])
                print ("\nTarget locked")
            except:
                print ("\nError : Key file not found")
                blowfish_decryption_get_key_1 () 

        blowfish_decryption_get_key_1 () 

        def blowfish_decryption_get_key_2 ():

            key2_input = input ("\nImport the second BLOW key file to use :")

            global iv_2
            global key_2

            try:
                with open (key2_input, 'rb') as f_key2file:
                    rawkey = f_key2file.read()
                iv_2 = bytes(rawkey[:8])
                key_2 = bytes(rawkey [8:])
                print ("\nTarget locked")
            except:
                print ("\nError : Key file not found")
                blowfish_decryption_get_key_2 ()

        blowfish_decryption_get_key_2 ()

        def blowfish_decryption_get_key_3 ():

            key3_input = input ("\nImport the third BLOW key file to use :")

            global iv_3
            global key_3

            try:
                with open (key3_input, 'rb') as f_key3file:
                    rawkey = f_key3file.read()
                iv_3 = bytes(rawkey[:8])
                key_3 = bytes(rawkey [8:])
                print ("\nTarget locked")
            except:
                print ("\nError : Key file not found")
                blowfish_decryption_get_key_3 () 

        blowfish_decryption_get_key_3 () 

        hashnsalt_1 = blowfish.Cipher(key_1)
        hashnsalt_2 = blowfish.Cipher(key_2)
        hashnsalt_3 = blowfish.Cipher(key_3)

        try:
            data_result_1 = b"".join(hashnsalt_3.decrypt_cfb(final_data_result_1, iv_3))
            print ("\nRound 1 : SUCCESS")
        except:
            print ("\nRound 1 : FAILED")
        try:
            data_result_2 = b"".join(hashnsalt_2.decrypt_cfb(data_result_1, iv_2))
            print ("\nRound 2 : SUCCESS")
        except:
            print ("\nRound 2 : FAILED")
        try:
            global final_data_result_2
            final_data_result_2 = b"".join(hashnsalt_1.decrypt_cfb(data_result_2, iv_1))
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
                input ("(press enter to continue)\n")
        except: 
            print ("\n")
            input ("Error while encrypting failed (press enter to continue)\n")

    if to_do == "2":
        AES_round_decryption()
        blowfish_round_decryption()
        try:
            with open(output, 'wb') as f_output:
                f_output.write(final_data_result_2)
                print ("\n")
                print ("################DATA DECRYPTED################\n")
                input ("(press enter to continue)\n")
        except: 
            print ("\n")
            input ("Error while decrypting failed (press enter to continue)\n")


if __name__ == "__main__":
    main()

# Version F-app.1.0.4
