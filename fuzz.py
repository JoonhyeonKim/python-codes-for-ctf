#! /usr/bin/python2
import sys, socket
from time import sleep
from pwn import *

buffer = "A" * 100

while True:
    try:
        p = process('./rao')
        
        p.send((buffer))
        p.close()
        sleep(1)
        buffer = buffer + "A"*100
        
    except:
        print ("Fuzzing crashed at %s bytes" % str(len(buffer)))
        sys.exit()
