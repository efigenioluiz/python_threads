#!/usr/bin/env python3
import threading
import time
import random 

def imprime(i):
    time.sleep(random.randint(1,5))
    print("Olá Mundo - {}".format(i))

if __name__=="__main__":
    
    threads=[]

    for a in range(10):
        t=threading.Thread(target=imprime,args=(a,))
        threads.append(t)
        t.start()
        t.join()

    # print("Iniciando processo")
    # print("Criando Threads..")

    # #criando uma thread
    # i=0
    # t1= threading.Thread(target=imprime,args=(i,))

    # #rodando thread
    # t1.start()

    # #aguardando finalização da thread
    # t1.join()

    # print("Finalizando o processo!")