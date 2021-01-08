# Author: David De la Mora
# Universidad Veracruzana
# Este codigo corresponde al codigo fuente
# necesario para encontrar la proteina E del genoma del
# SARS-CoV-2.

# En esta seccion se definen las variables a usar, que corresponden
# a los 4 nucleotidos.
nucleotides = ["A", "C", "T", "G"]

# En esta parte se crea un diccionario donde cada nucleotido
# se aparea con su complemento segun el apareamiento de Watson-Crick.
nucl_complement = {
               "A":"T", 
               "C":"G", 
               "T":"A",
               "G":"C" 
	      }

# Durante la transcripcion de DNA a RNA, la Timina se sustituye
# por Uracilo. Sin embargo, aunque esta es la realidad biologica, 
# normalmente en bases de datos se mantiene la T como T.
rna_transcription = {
	       "A":"A",
	       "C":"C",
               "T":"U",
               "G":"G"
	      }

# Este diccionario largo codifica cada codon del codigo genetico,
# esto es, cada secuencia de tres nucleotidos continuos, en un
# aminoacido, los cuales son los bloques que forman las proteinas.
codons = {
  "UUU": "Fenilalanina",
  "UUC": "Fenilalanina",
  "UUA": "Leucina",
  "UUG": "Leucina",
  "UCU": "Serina",
  "UCC": "Serina",
  "UCA": "Serina",
  "UCG": "Serina",
  "UAU": "Tirosina",
  "UAC": "Tirosina",
  "UAA": "STOP Ocre",
  "UAG": "STOP Ambar",
  "UGU": "Cisteina",
  "UGC": "Cisteina",
  "UGA": "STOP Opalo",
  "UGG": "Triptofano",
  "CUU": "Leucina",
  "CUC": "Leucina",
  "CUA": "Leucina",
  "CUG": "Leucina",
  "CCU": "Prolina",
  "CCC": "Prolina",
  "CCA": "Prolina",
  "CCG": "Prolina",
  "CAU": "Histidina",
  "CAC": "Histidina",
  "CAA": "Glutamina",
  "CAG": "Glutamina",
  "CGU": "Arginina",
  "CGC": "Arginina",
  "CGA": "Arginina",
  "CGG": "Arginina",
  "AUU": "Isoleucina",
  "AUC": "Isoleucina",
  "AUA": "Isoleucina",
  "AUG": "Metionina",
  "ACU": "Treonina",
  "ACC": "Treonina",
  "ACA": "Treonina",
  "ACG": "Treonina",
  "AAU": "Asparagina",
  "AAC": "Asparagina",
  "AAA": "Lisina",
  "AAG": "Lisina",
  "AGU": "Serina",
  "AGC": "Serina",
  "AGA": "Arginina",
  "AGG": "Arginina",
  "GUU": "Valina",
  "GUC": "Valina",
  "GUA": "Valina",
  "GUG": "Valina",
  "GCU": "Alanina",
  "GCC": "Alanina",
  "GCA": "Alanina",
  "GCG": "Alanina",
  "GAU": "Acido aspartico",
  "GAC": "Acido aspartico",
  "GAA": "Acido glutamico",
  "GAG": "Acido glutamico",
  "GGU": "Glicina",
  "GGC": "Glicina",
  "GGA": "Glicina",
  "GGG": "Glicina"
}

# Este diccionario cambia el nombre completo del aminoacido codificado
# por cada codon, en su respectiva abreviatura de una letra. Los codones
# de paro se encuentran vacios. 
aminoacidos = {
  "UUU": "F",
  "UUC": "F",
  "UUA": "L",
  "UUG": "L",
  "UCU": "S",
  "UCC": "S",
  "UCA": "S",
  "UCG": "S",
  "UAU": "Y",
  "UAC": "Y",
  "UAA": "",
  "UAG": "",
  "UGU": "C",
  "UGC": "C",
  "UGA": "",
  "UGG": "W",
  "CUU": "L",
  "CUC": "L",
  "CUA": "L",
  "CUG": "L",
  "CCU": "P",
  "CCC": "P",
  "CCA": "P",
  "CCG": "P",
  "CAU": "H",
  "CAC": "H",
  "CAA": "Q",
  "CAG": "Q",
  "CGU": "R",
  "CGC": "R",
  "CGA": "R",
  "CGG": "R",
  "AUU": "I",
  "AUC": "I",
  "AUA": "I",
  "AUG": "M",
  "ACU": "T",
  "ACC": "T",
  "ACA": "T",
  "ACG": "T",
  "AAU": "N",
  "AAC": "N",
  "AAA": "L",
  "AAG": "L",
  "AGU": "S",
  "AGC": "S",
  "AGA": "R",
  "AGG": "R",
  "GUU": "V",
  "GUC": "V",
  "GUA": "V",
  "GUG": "V",
  "GCU": "A",
  "GCC": "A",
  "GCA": "A",
  "GCG": "A",
  "GAU": "D",
  "GAC": "D",
  "GAA": "E",
  "GAG": "E",
  "GGU": "G",
  "GGC": "G",
  "GGA": "G",
  "GGG": "G"
}

nucl_codon = [];
frames = [];
proteins = [];

dna = ""
dna_complement = ""
rna = ""

# Aqui se especifica el archivo de entrada, el cual se encuentra ya
# en la carpeta y que contiene el genoma completo del virus
# SARS-CoV-2. Hay que destacar que CoViD-19 es el nombre de la enfermedad
# y, por lo tanto, el virus se llama SARS-CoV-2.
f = open("GenomaSARSCoV2.txt", "r")
for x in f:
  dna = dna + x
dna = dna.replace("\n","")


# Se obtiene primero la secuencia complementaria a los datos de entrada 

for x in dna:
  dna_complement = dna_complement + nucl_complement[x]
  
# Estas dos salidas permiten ver la longitud en pares de bases
# del genoma analizar, que deberia ser de 29 903 bp.
n = len(dna)
print " dna length  = ", n

n = len(dna_complement)
print " dna length complementary  = ", n

# Esta seccion corresponde a como si se hiciera una transcripcion
# de DNA a RNA del gen

for x in dna:
  rna = rna + rna_transcription[x]


# En esta seccion se crearan los codones

n = len(rna)

codon = ""
myframe = ""
frame_start = 0

print "ORFs: "

# En cada genoma, existen en realidad hasta 6 marcos de lectura.
# El siguiente codigo sirve unicamente para leer los tres que
# corresponden a la cadena sentido del genoma. Es por ello que el
# codigo esta disenado para encontrar los codones de inicio AUG
# iniciando en el indice [0] y hara la busqueda de tres en tres
# en este ORF, y posteriormente se ira recorriendo por 1 para
# hacer la busqueda en los 2 posibles ORF que podrian existir en
# esta cadena. El codigo tambien imprime los indices de inicio y
# final de las posibles proteinas que encuentre. Es decir, que en el
# mismo marco de lectura se encuentre un codon de inicio AUG y alguno
# de los tres de finalizacion. Al final indica el numero encontrado.

for c in range(0, 3):
  print "***"
  print c, rna[c]

  myframe = ""
  frame_start = 0

  for i in range(c, n, 3):
    codon = rna[i:i+3]
    nucl_codon.append(codon)
# Este es el codon de inicio
    if (codon == "AUG") and (frame_start == 0):
      frame_start = 1
      myframe = "AUG"
      print "Inicio ", i
    else:
      if (frame_start == 1):
# Estos son los tres posibles codones de finalizacion
        if (codon == "UAA") or (codon=="UAG") or (codon=="UGA"):
          frame_start = 0
          frames.append(myframe)
          myframe = ""
          print "Fin ", i
        else:
          myframe = myframe + codon

n = len(frames)


# En realidad, todo lo anterior no sirve de mucho. Es decir,
# se deberia especificar un limite para el numero minimo de codones
# que podrian codificar para una proteina real, lo cual podria
# ser <10 aa. El resultado hasta este punto indica todos los posibles
# indices donde en el mismo ORF hay un inicio y un fin, pero
# podria unicamente corresponder a 2 o 3 aminoacidos, por ejemplo.
# Lo que nos podria permitir observar es el numero de peptidos
# teoricamente posibles que existen y la posicion en el genoma.
# Sin embargo, en pasos posteriores se imprimira unicamente la
# informacion que nos interesa, la cual es la que corresponda a la
# proteina E del virus.

# Este codigo no solo indica las posiciones de inicio y termino de una
# posible proteina, sino que tambien pueden proporcionar la secuencia
# primaria del peptido encontrado. Para esto se crearon los
# diccionarios al inicio del codigo.


myprotein = ""
for i in range(0,n):
  y = len(frames[i])
  myprotein = ""
  myframe = frames[i]

  for j in range(0, y, 3):
    codon = myframe[j:j+3]
    myprotein += aminoacidos[codon]
  proteins.append(myprotein)



# La siguiente seccion del codigo deberia imprimir el resultado
# de todos los posibles peptidos encontrados en los ORF.
# Esto si es posible hacerlo, sin embargo, ya que se sabe que
# la proteina E es un peptido de 75 aa, es posible unicamente
# imprimir y definir que unicamente el resultado sean aquellos
# que cumplan con el criterio de dar una proteina de 75 aa, 
# que, en este caso, deberia ser la proteina E.


print '\nSecuencia genomica y de aminoacidos de la proteina E:'

for i in range(0,n):
# Criterio de los 75 aa que corresponden a la proteina E
  if (len(proteins[i]) ==  75):

    print frames[i], len(frames[i])
    print "\n"
    print proteins[i], len(proteins[i])
