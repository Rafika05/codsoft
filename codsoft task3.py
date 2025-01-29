import sys
import random
import string
passlength=int(input("Enter the length of the password:"))
print("1.Alphabets+numbers+symbols \n2.Alphabets+number \n3.Numbers+sysmbols \n4.only Alphabets \n5.only numbers \n6.Alphabets+number+underscore \n7.Exit")
choice=int(input("Enter your choice:"))

def password_generator(passlength):
    password=''.join(random.choices(characters,k=passlength))
    return password

if choice==1:
    characters=string.ascii_letters+string.digits+string.punctuation
    password=password_generator(passlength)
elif choice==2:
    characters=string.ascii_letters+string.digits
    password=password_generator(passlength)
elif choice==3:
    characters=string.digits+string.punctuation
    password=password_generator(passlength)
elif choice==4:
    characters=string.ascii_letters
    password=password_generator(passlength)
elif choice==5:
    characters=string.digits
    password=password_generator(passlength)
elif choice==6:
    characters=string.ascii_letters+string.digits+"_"
    password=password_generator(passlength)
else:
    sys.exit()


print("Your password is :",password)


    
