import mysql.connector

mydb = mysql.connector.connect(
  host="0.0.0.0",
  user="root",
  passwd="password",
  db="todolist"
)
mycursor = mydb.cursor()

def createDatabase():
    dbname = null
    cmd = "CREATE DATABASE IF EXISTS "+db
    mycursor.execute(cmd)

def CreateTable();
    table=null
    cmd = 'create table '+table+'(id int auto_increment primary key not null, name text)'
    mycursor.execute(cmd)
