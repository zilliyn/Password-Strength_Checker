import string

password = input ("enter the password")
score =0
lower = any( c in string.ascii_lowercase for c in password )
upper = any(c in string.ascii_uppercase for c in password)
digit = any( c in string.digits for c in password)
symbol = any( c in string.punctuation for c in password)

length =len(password)

if length > 8:
    score +=1
if length > 12:
    score +=1
if length > 17:
    score+=1
if length > 20:
    score +=1

types =[lower,upper,digit,symbol]
score +=sum(types)-1

with open("common.txt","r") as file:
    common_password = file.read().splitlines()

if password in common_password:
   score=0
if score <= 2:
    print("Weak Password")
elif score <= 4:
    print("Okay Password")
elif score <= 6:
    print("Pretty Good Password")
else:
    print("Strong Password")
