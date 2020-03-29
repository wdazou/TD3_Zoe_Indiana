#!/usr/bin/env python
import sys


def mull(x,y):
        return x*y
if __name__ =="__main__" :
        print ("vous voulez multiplier quelques  valeur,?" )
        z  = str(input())

        if (z =="oui"):
                if len(sys.argv) > 3:
                        print ("beaucoup d'argument")

                elif(len(sys.argv) == 3):
                        x = int(sys.argv[1])
                        y = int(sys.argv[2])
                        print("le resultat est : ", mull(x,y))

                elif (len(sys.argv)==2): 
                        print("entrer les valeurs que vous voulez  ")
                        x = int(sys.argv[1])
                        y = int(input())
                        print("le resultat est : ", mull(x,y))

                else : 
                        print("entre deux valeur:  ")

                        x=int(input())
                        y=int(input())
                        print("le resultat est : ", mull(x,y))

