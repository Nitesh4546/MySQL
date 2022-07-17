#Importing the required libraries
import pyautogui as p
import time as t
import os

#User inputs
named=input('Enter the database name =') #Takes database name from user
namet=input('Enter the table name =')    #Takes database table from user
a=int(input('Enter the no. of column ='))#Takes database no. of columns from user

#Empty dictionaries
col={}  #dictonary for storing column name
da={}   #dictonary for storing data type
con={}  #dictonary for storing constraints

#Instruction
print('For no constraint please enter ,<null>')  
print('For column name use <_> instead of space')
print("Don't use symbols in column name")

#Loop for inserting values in the empty dictionaries 
for i in range(1,a+1):

    #User inputs
    value1=input('Enter the column name=')#Takes database column name from user
    value2=input('Enter the data type=')  #Takes database column data type from user
    value3=input('Enter constraint=')     #Takes database column constraints from user
    key1=key2=key3=i

    #Adds the values in dictionaries
    col[key1]=value1
    da[key2]=value2
    con[key3]=value3

# Automation code begins from here: -

#Enter the path to MySQL Command Line Client.lnk
os.startfile(r"C:\Users\nites\Desktop\MySQL 8.0 Command Line Client.lnk")
t.sleep(2)
#p.typewrite('password')#enter the password
t.sleep(0.8)
p.press('enter')
t.sleep(0.8)

#Shows databases
p.typewrite('show databases;')
p.press('enter')
t.sleep(0.13)

#Creates database with the provided name
p.typewrite('create database {};'.format(named))
p.press('enter')
t.sleep(0.05)
p.typewrite('use {};'.format(named))
p.press('enter')

#Shows databases
p.typewrite('show databases;')
p.press('enter')
t.sleep(0.1)

#Creats table
p.typewrite('create table {} ('.format(namet))
p.press('enter')


for io in range(1,a+1):
    if io<len(col):
        p.typewrite('{} {} {},'.format(col[io],da[io],con[io]))
        p.press('enter')
    else:
        p.typewrite('{} {} {}'.format(col[len(col)],da[len(da)],con[len(con)]))
p.press([')',';','enter'])

#Shows the structure of the table created
p.typewrite('desc {};'.format(namet))
p.press('enter')