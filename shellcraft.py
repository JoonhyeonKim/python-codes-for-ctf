#!/usr/bin/python3
#Name: shellcraft.py

from pwn import *
context.arch = 'amd64'

code = shellcraft.sh()
print(code)
