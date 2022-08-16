#!/usr/bin/python3
#Name: asm.py

from pwn import *
context.arch = 'amd64' # exploit target is 'x86-64'

code = shellcraft.sh() # it will launch the shell
code = asm(code)
print(code)
