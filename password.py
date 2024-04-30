#password generator
import random
def pwd_generator():
    psd_sym = int(input("Enter the number of symbols in the password: "))
    psd_num = int(input("Enter the number of numbers in the password: "))
    psd_ltr = int(input("Enter the number of letters in the password: "))
    
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "0123456789"
    sym = "!~@#$%&*?"

    pw1 = ''.join(random.choices(sym, k=psd_sym))
    pw2= ''.join(random.choices(num, k=psd_num))
    pw3= ''.join(random.choices(alphabet, k=psd_ltr))
    password=pw1+pw2+pw3
    
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    print("Generated_password:", password)

pwd_generator()
