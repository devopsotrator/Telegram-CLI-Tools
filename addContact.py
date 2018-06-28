import sys
from random import randint
from time import sleep
from subprocess import Popen, PIPE

telegram = Popen(["telegram-cli"], stdin=PIPE, stdout=sys.stdout)

while True:
    num = randint(79000000000,79990000000)
    line = "add_contact {} {} {}\r".format(num, "Deanon", num)
    telegram.stdin.write(line)
    sleep(1)