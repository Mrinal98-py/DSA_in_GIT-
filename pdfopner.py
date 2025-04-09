import pikepdf
from tqdm import tqdm
passwords = [line.strip() for line in open("wordlist.txt")]
for password in tqdm(passwords, "Decrypting PDF"):
    try:
        # with pikepdf.open("C:\Users\mrina\Downloads\tanvi\4108202501076304698805.pdf", password=password) as pdf:
        with pikepdf.open(r"C:\Users\mrina\Downloads\tanvi\4108202501076304698805.pdf", password=password) as pdf:
 
            print("\n[+] Password:",password)
            break
    except pikepdf._qpdf.PasswordError as e:
        continue