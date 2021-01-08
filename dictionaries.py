# Author: David De la Mora
# Date: Oct 10, 2020
# Universidad Veracruzana
# dictionaries.py

nucleotidos = {
		"A":"Adenina", 
		"C":"Citosina", 
		"G":"Guanina", 
		"T":"Timina"
		 }

print len(nucleotidos)
print nucleotidos

print nucleotidos["A"]
print nucleotidos["C"]
print nucleotidos["G"]
print nucleotidos["T"]

nucleotidos["A"] = "ADENINA"
nucleotidos["C"] = "CITOSINA"
nucleotidos["T"] = "TIMINA"
nucleotidos["G"] = "GUANINA"
# Aqui podemos cambiar todas por mayusculas


print nucleotidos
nucleotidos.pop('T', None)
print nucleotidos
