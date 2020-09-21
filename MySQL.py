from DBHelper import DbHelper

def main():
    db=DbHelper()
    while(True):
        print("*************WELCOME****************")
        print()
        print("1: Insert User")
        print("2: Display User")
        print("3: Delete User")
        print("4: Update User")
        print("0: Exit")
        print()
        try:
            choice=int(input("Enter Your Choice : "))
            if(choice==1):
                uid=int(input("Enter userID : "))
                userName=input("Enter user name : ")
                userPhone=input("Enter user phone : ")
                db.insertUser(uid,userName,userPhone)
                
            elif(choice==2):
                db.fetchAllUser()
                
            elif(choice==3):
                uid=int(input("Enter userID to delete : "))
                db.deleteUser(uid)
                
            elif(choice==4):
                uid=int(input("Enter userID : "))
                userName=input("Enter new user name : ")
                userPhone=input("Enter new user phone : ")
                db.updateUser(uid,userName,userPhone)
            elif(choice==0):
                break
            else:
                print("Invalid Input")
        except Exception as e:
            print(e)
            print("Try Again")

if(__name__=='__main__'):
    main()

        
