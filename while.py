# Author: David De la Mora
# Date: Oct 10, 2020
# Universidad Veracruzana
# while.py
# Por alguna raz�n, este es el mismo c�digo que conditionals.py


nucleotide = raw_input("Input nucleotide A, C, T, G :")
print nucleotide

if (nucleotide == "A"):
 print ("ADENINA")
elif (nucleotide == "C"):
 print ("CITOSINA")
elif (nucleotide == "T"):
 print ("TIMINA")
elif (nucleotide == "G"):
 print("GUANINA")
else:
 print("ERROR in input")
