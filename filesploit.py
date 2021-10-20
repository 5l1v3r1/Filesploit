import os
import time

os.system("clear")
os.system("figlet Filesploit")
print(" ")
print("[UYARI] Lütfen Önce install.py Dosyasını Çalıştırın.")
print("Coded By Xale - GitHub: @xaletr - v1.3 Beta")
print(" ")
cmd = input("filesploit>> ")

if cmd == "help":
 print("7 saniye içerisinde help bölümü kapatılacaktır.")
 print("read file : Dosya Okur.")
 print("new file : Dosya Oluşturur.")
 print("write file : Belirtilen Dosyaya Belirtilen Mesajı Yazar.")
 print("delete file : Belirtilen Dosyayı Siler.")
 time.sleep(7)
 os.system("python3 filesploit.py")

elif cmd == "read file":
 readfile = input("Okunacak Dosya Adı: ")
 dosya = open(readfile,"r",encoding="utf-8")
 oku = dosya.read()
 print(oku)
 time.sleep(1)
 os.system("python3 filesploit.py")

elif cmd == "delete file":
 delfile = input("Silinecek Dosyanın Adı: ")
 os.system("rm -r " + delfile)

elif cmd == "new file":
 newfile = input("Oluşturulacak Dosya Adı: ")
 dosya2 = open(newfile,"w",encoding="utf-8")
 time.sleep(1)
 os.system("python3 filesploit.py")

elif cmd == "write file":
 writefile = input("Yazılacak Dosya Adı: ")
 dosya3 = open(writefile,"w",encoding="utf-8")
 text1 = input("Dosyanın 1. Satırına Ne Yazmak İstersiniz: ")
 dosya3.write(text1)
 time.sleep(1)
 os.system("python3 filesploit.py")
 os.system("python3 filesploit.py")
elif cmd == "exit":
 os.system("exit")
else:
 print("Tanımsız İfade: ", cmd)
 time.sleep(1)
 os.system("python3 filesploit.py")
