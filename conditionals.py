# Author: David De la Mora
# Date: Oct 10, 2020
# Universidad Veracruzana
# conditionals.py

nucleotide = raw_input("Input nucleotide A, C, T, G :")
print nucleotide

if (nucleotide == "A"):
 print ("Adenina")
elif (nucleotide == "C"):
 print ("Citosina")
elif (nucleotide == "T"):
 print ("Timina")
elif (nucleotide == "G"):
 print("Guanina")
else:
 print("ERROR in input")
