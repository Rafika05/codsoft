import sys
while(True):
    print("\n Arithmetic Operations:")
    print(" 1.Addtion \n 2.Subtraction \n 3.Multiplication \n 4.Division \n 5.Modulus \n 6.Exponent \n 7.floor Division \n 8.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        a=int(input("Enter the First number:"))
        b=int(input("Enter the Second number:"))
        c=a+b
        print("\nAddition result:",c)
    elif choice==2:
        a=int(input("Enter the First number:"))
        b=int(input("Enter the Second number:")) 
        if a>b:
            c=a-b
            print("\n Subtraction result(First number>Second number):",c)
        else:
            c=b-a
            print("\n Subtraction result(Second number>First number):",c)
    elif choice==3:
        a=int(input("Enter the First number:"))
        b=int(input("Enter the Second number:")) 
        c=a*b
        print("\n Multiplication  result:",c)
    elif choice==4:
        a=int(input("Enter the First number:"))
        b=int(input("Enter the Second number:"))
        c=a/b
        print("\n Division result:",c)
    elif choice==5:
        a=int(input("Enter the First number:"))
        b=int(input("Enter the Second number:"))
        c=a%b
        print("\n Modulus  result:",c)
    elif choice==6:
        a=int(input("Enter the First number:"))
        b=int(input("Enter the Second number:"))
        c=a**b
        print("\n Exponentiation result:",c)
    elif choice==7:
        a=int(input("Enter the First number:"))
        b=int(input("Enter the Second number:"))
        c=a//b
        print("\n Floor Division result:",c)
    elif choice==8:
        sys.exit(0)
    else:
        print("Your have entered an invalid choice")
    menu=input("\n Do you need the menu Yes/No:")
    if menu=="no" or menu=="No":
        break

        
    
            
        
    
    
