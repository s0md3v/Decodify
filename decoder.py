#!/usr/bin/python
import hashlib
from urllib.request import urlopen

hash = input("Enter Your Hash Value: ")
Hash = input("Enter your Hash Type: ")

passlist= str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt').read(), 'utf-8'))

hash1 = "sha256"
hash2 = "sha224"
hash3 = "sha512"
hash4 = "blake2c"
hash5 = "blake2b"

for password in passlist.split('\n'):
  if Hash==hash1:
    hashguess = hashlib.sha256(byte(password, 'utf-8')).hexdigest()
    if hashguess == hash:
      print ("[*] Password is: "+str(password))
      quit()
    else:
      print ("[-] Password not matched, Trying anoter Password.............!")
      
  elif Hash == hash2:
    hashguess = hashlib.sha224(byte(password, 'utf-8')).hexdigest()
    if hashguess == hash:
      print ("[*] Password is: "+str(password))
      quit()
    else:
      print ("[-] Password not matched, Trying anoter Password.............!")
      
  elif Hash == hash3:
    hashguess = hashlib.sha512(byte(pasword, 'utf-8')).hexdigest()
    if hashguess == hash:
      print ("[*] Password is: "+str(password))
      quit()
    else:
      print ("[-] Password not matched, Trying anoter Password.............!")
      
  elif Hash == hash4:
    hashguess = hashlib.shablake2s(byte(password, 'utf-8')).hexdigest()
    if hashguess == hash:
      print ("[*] Password is: "+str(password))
      quit()
    else:
      print ("[-] Password not matched, Trying anoter Password.............!")
  elif Hash = hash5:
    hashguess = hashlib.blake2b(byte(pasword, 'utf-8')).hexdigest()
    if hashguess == hash:
      print ("[*] Password is: "+str(password))
      quit()
    else:
        print ("[-] Password not matched, Trying anoter Password.............!")
      
      
      
print ("[-] Password not Found :( :( :( :(")

      
      
    
  
