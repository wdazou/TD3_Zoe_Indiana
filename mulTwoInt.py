#!/usr/bin/env python3
import sys

def mul(x,y):
	return x * y

if len(sys.argv) <= 2 :
	print (" manque arguments")

elif (len(sys.argv) == 3) :
	x=int(sys.argv[1])
	y=int(sys.argv[2])
	print("Le resultat est : ",mul(x,y))

else :
	print ("trop d'arguments")

