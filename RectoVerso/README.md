### RectoVerso

RectoVerso is a sub-tool of CryptSIS that list and then a full targeted folder, and put the encrypted version to another one.
This script can get very useful when you got to encrypt more than 50 files.

### Usage

Tree structure : 

```
+-- Folder to encrypt
|   |
|   +-- file1.txt
|   | 
|   +-- file2.txt
|
+-- Destination folder
|   |
|   +-- file1.txt (if encrypted or decrypted)
|   |
|   +-- file2.txt (if encrypted or decrypted)
|
+-- Key.key
|
+-- Recto.py or Verso.py

```
## Recto (encryptor)

Just enter the folder name to crypt, then the destination folder, it's all !!!

data gonna be encrypted using AES-256-CBC cipher.

your key file must be named key.key.


## Verso (decryptor)

Just enter the folder name to decrypt; then the destination folder, then the key file name it's all !!!
