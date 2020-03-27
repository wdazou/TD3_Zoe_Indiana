#!/usr/bin/env python3

import sys

def add(x,y):
        return x + y

if len(sys.argv) > 3 :
        print (" trop d'arguments")

elif (len(sys.argv) == 3) :
        x=int(sys.argv[1])
        y=int(sys.argv[2])
        print("Le resultat est : ",add(x,y))

else :
	print ("argument insuffisant")
	print ("entre les valeurs manquantes : ")
	x = int(sys.argv[1])
	y = int(input())
	print ("Le resultat est : ",add(x,y))

