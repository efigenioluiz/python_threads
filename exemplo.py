#!/usr/bin/env python3
import sys

# x= random.getrandbits(20)

nome=sys.argv[1]
arq=open(nome,"r")

linhas=[]

for l in arq.readlines():
    linhas.append(l)

print(linhas)
