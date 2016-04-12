#!/usr/bin/python2.7

import subprocess
import os
import sys
import re
import MySQLdb
import string
import ftplib
from fabric.api import *
import urllib2
import smtplib

"""Testing script"""


print "subprocess treatment \n"
subprocess.call(["ls"])

p1 = subprocess.Popen(["dmesg"], stdout=subprocess.PIPE)
p2 = subprocess.Popen(["grep", "sda"], stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()
output = p2.communicate()[0]
print output
print "\n"

#*************************************#

print "os treatment \n"

dir = "/root"
path = "/root/sub.py"
path2 = "/root/test"
path3 = "/root/test2"


print os.path.dirname(path)
print os.path.basename(path)
print os.path.split(path)
print os.path.abspath(".")
print os.listdir("/root")


#for path, dirs, files in os.walk(dir):
#    for filename in files:
#        print filename

if os.path.isdir(path2):
    os.rename(path2, path3)
else:
    os.mkdir(path2)
print "\n"

#*************************************#

print "sys treatment \n"
print sys.path
print "This is the name of the script: ", sys.argv[0]
print "Number of arguments: ", len(sys.argv)
print "The arguments are: ", str(sys.argv)
print "\n"

#*************************************#

print "for treatment \n"
for i in range(0, 10):
    print i
print "\n"

#*************************************#

print "while treatment \n"
i = 0
while i < 10:
    print i
    i += 1
print "\n"

#*************************************#

print "dictionary treatment\n"


class Person(object):
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession
people = [Person("Nick", "Programmer"), Person("Alice", "Engineer")]
professions = dict([(p.name, p.profession) for p in people])
print professions
print "\n"

#*************************************#

print "lists treatment\n"
a = [66.25, 333, 333, 1, 1234.5]
print a.count(333), a.count(66.25), a.count('x')
a.insert(2, -1)
a.append(333)
print a
a.index(333)
a.remove(333)
print a
a.sort()
a.pop()
a[0] = 7
print a
print "\n"

#*************************************#

print "tuples treatment\n"

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)

print "tup1[0]: ", tup1[0]
print "tup2[1:5]: ", tup2[1:5]
print tup1 + tup2
print "\n"

#*************************************#

print "regex treatment\n"

phone = "2004-959-559 # This is Phone Number"

# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print "Phone Num : ", num

# Remove anything other than digits
num = re.sub(r'\D', "", phone)
print "Phone Num : ", num
print "\n"

#*************************************#

print "\n Mysql create database treatment"

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost", "root", "netadmin", "test")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Create table as per requirement
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)

# disconnect from server
db.close()
print "\n"

#*************************************#

print "Mysql insert treatment \n"
# Open database connection
db = MySQLdb.connect("localhost", "root", "netadmin", "test")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
except:
    # Rollback in case there is any error
    db.rollback()

# disconnect from server
db.close()

#*************************************#

print "String treatment \n"

ch = "test"

print ch.lower()
print ch.upper()
print "\n"

sentence = "The cat is brown"
q = "cat"

if q == sentence:
    print('strings equal')

if q in sentence:
    print(q + " found in " + sentence)
print "\n"

s = sentence.replace("cat", "dog")
print s
print "\n"

#************************************

print "Function treatment \n"


def printme(name, age, prof, diploma):
    print "Name: ", name
    print "Age: ", age
    print "Profession: ", prof
    print "Diploma: ", diploma
    return

printme("Haithem", 29, "engineer", "IT engineer diploma")

#***********************************

print "Function 2 treatment \n"


def ajout(x, y):
    print x, "+", y, "=", x + y
ajout(2, 3)
print "\n"

#***********************************


def menu():
    #print what options you have
    print "Welcome to calculator.py"
    print "your options are:"
    print " "
    print "1) Addition"
    print "2) Subtraction"
    print "3) Multiplication"
    print "4) Division"
    print "5) Quit calculator.py"
    print " "
    return input("Choose your option: ")


def add(a, b):  # this adds two numbers given
    print a, "+", b, "=", a + b


def sub(a, b):  # this subtracts two numbers given
    print b, "-", a, "=", b - a


def mul(a, b):  # this multiplies two numbers given
    print a, "*", b, "=", a * b


def div(a, b):  # this divides two numbers given
    print a, "/", b, "=", a / b

# NOW THE PROGRAM REALLY STARTS, AS CODE IS RUN
loop = 1
choice = 0
while loop == 1:
    choice = menu()
    if choice == 1:
        add(input("Add this: "), input("to this: "))
    elif choice == 2:
        sub(input("Subtract this: "), input("from this: "))
    elif choice == 3:
        mul(input("Multiply this: "), input("by this: "))
    elif choice == 4:
        div(input("Divide this: "), input("by this: "))
    elif choice == 5:
        loop = 0

print "\n"
#********************************

print "Exercise \n"


def list_benefits():
    return "More organized code", "More readable code",
    "Easier code reuse",
    "Allowing programmers to share and connect code together"


def build_sentence(info):
    print info + " is a benefit of functions!"


def work():
    liste = list_benefits()
    for list_info in liste:
        build_sentence(list_info)

work()
