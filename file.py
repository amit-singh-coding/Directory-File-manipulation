import os
def creat_file(name):
    try:
        f=open(name+".txt","x")
        return "🟩🟩"+name+"-> File Created Sucessfully"
    except:
        return name+" Name-🙃🙃 File Already in Your PC"            
def read_fiel(name):
    try:
        f=open(name+".txt","r")
        x=f.read()
        f.close()
        return "😍😍-> ",x
    except:
        return "❌❌"+name+" File Not Available- Please Creat First..!"
def write_in_file(name):
    if os.path.isfile(name+".txt"):
        f=open(name+".txt","a")
        f.write(input("Enter data-> ")+',')
        return "✍🏻✍🏻-> File Written sucessfully....!"
    else:
        return "❌❌"+name+" File Not Available- Please Creat First..!"
def rename_file(name):
    try:
        os.rename(name+".txt",input("Enter New Name-> ")+".txt")
        return " ☑️☑️-> File Rename sucessfully....!"  
    except:
        return "❌❌"+name+" File Not Available..!"     
def delete_file(name):
    try:
        os.remove(r""+name)
        return "✔️✔️-> File Deleted sucessfully....!"
    except:
        return "❌❌"+name+" File Not Available- Please Creat First..!"
print("💻💻--> Wellcome to File manipulation <--💻💻")    
while True:        
    print("""🔴 Options:
Enter: 00- Close Function....!          
Enter: 1- Creat File
Enter: 2- Write in File
Enter: 3- Read File
Enter: 4- Delete File
Enter: 5- Rename File""")
    user_input=input("Enter here-> ")
    if user_input=="00":
        break
    elif user_input=="1":
        c=creat_file(input("Enter file name-> "))
        print(c)
        print()
    elif user_input=="2":
        w=write_in_file(input("Enter file name-> "))
        print(w)
        print()
    elif user_input=="5":
        rn=rename_file(input("Enter file name-> ")) 
        print(rn)
        print()   
    elif user_input=="3":
        r=read_fiel(input("Enter file name-> "))
        print(r)
        print()
    elif user_input=="4":
        d=delete_file(input("🛑🛑🛑Enter file Path-> "))
        print(d)
        print()    
    else:
        print("❌❌❌❌-->Input in Wrong..Enter currect Input") 
        print()               
print("😃 Thanks Your Function has Closed...!")





