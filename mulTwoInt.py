#!/usr/bin/env python3
def mul(a,b):
        return a*b



def main():
        import sys
        entre = sys.argv


        if (len(entre) != 3):
                print("Erreur  inserer 2 valeurs s'il vous plait" )
                a = input("entrez le premier valeur: ")
                b = input("entrez le deuxieme valeur: ")

                try: #il arrive que input ne retourne pas une  valeur "string" mais "int" (ex: kali linux)
                        print(mul(eval(a),eval(b)))


                except:
                        print(mul(a,b))
                return


        print(mul(eval(entre[1]),eval(entre[2])))


if (__name__ == "__main__"):
        main()

