#!/usr/bin/env python
from pwn import *

s = remote('address.com', port) #opens the net cat
s.recv() #whatever the connection returns
s.close() #closes the connection
s.sendline(WHATEVER) #sends whatever