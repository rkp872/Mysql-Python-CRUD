import mysql.connector as connector
class DbHelper:
    def __init__(self):
        self.con=connector.connect(host='localhost',port='3306',user='root',password='76448',database='test')
        query='create table if not exists user(UserID int primary key,UserName varchar(200),Phone varchar(12));'
        cur=self.con.cursor()
        cur.execute(query)
        print('Created')

    #insert
    def insertUser(self,userID,userName,userPhone):
        query="insert into user (UserID,UserName,Phone) values({},'{}','{}');".format(userID,userName,userPhone)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("User saved")

    #Fetch all
    def fetchAllUser(self):
        query='select * from user'
        cur=self.con.cursor()
        cur.execute(query)
        print("-------------------------------------")
        print("UserID\tUserName\tUserPhone")
        print("-------------------------------------")
        for row in cur:            
            print(row[0],'\t'+row[1]+'\t\t'+row[2])
        print("-------------------------------------")

    #delete user
    def deleteUser(self,userId):
        query="delete from user where userID={}".format(userId)
        cur=self.con.cursor()
        cur.execute(query)
        print("User Deleted")
        self.con.commit()

    #update
    def updateUser(self,userId,newName,newPhone):
        query="update user set UserName='{}',Phone='{}' where UserID={}".format(newName,newPhone,userId)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Updated")
