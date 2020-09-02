import rarfile
from rarfile import RarWrongPassword
import sys

# unrar tool is required
rarfile.UNRAR_TOOL = "C:\\Program Files\\WinRAR\\UnRaR.exe"

# get rar file by drop it 
try:
    rar_file = sys.argv[1]
    print("Your rar file is :", rar_file)
except:
    print("No rar file found !!")


myrar_file = rarfile.RarFile(rar_file)

passwords = [line.strip() for line in open("wordlist.txt", encoding="utf8")]


for password in passwords:

    try:
        myrar_file.extractall(pwd=password)
        print("RaR Password is :", password)
        break
    
    except RarWrongPassword as err:
        print(err, "Please wait !!")
