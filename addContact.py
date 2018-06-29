import sys
from random import randint
from time import sleep
from subprocess import Popen, PIPE

telegram = ''

def addNumber(num):
    global telegram

    if telegram == '':
        telegram = Popen(["telegram-cli"], stdin=PIPE, stdout=sys.stdout)
    
    line = "add_contact {} {} {}\r".format(num, "Deanon", num)
    telegram.stdin.write(line)
    sleep(1)

def fromFile():
    file_name = raw_input("File: ")
    numbers = open(file_name).read().split('\n')

    for num in numbers:
        addNumber(num)

def rndGenerator():
    r0 = int(raw_input("From (ex. 150000000000): "))
    r1 = int(raw_input("To (ex. 150099999999): "))

    while True:
        addNumber(randint(r0,r1))

def inRange():
    a = int(raw_input("From (ex. 150000000000): "))
    b = int(raw_input("To (ex. 150099999999): "))

    while a != b:
        addNumber(a)
        a += 1

select = raw_input("Adding from:\n1 - file\n2 - random generation\n3 - 'brutoforce' numbers\nSelect: ")

if select == "1":
    fromFile()
elif select == "2":
    rndGenerator()
elif select == "3":
    inRange()
else:
    print "Invalid input!"