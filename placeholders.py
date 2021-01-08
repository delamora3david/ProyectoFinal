# Author: David De la Mora
# Date: Oct 3, 2020
# Universidad Veracruzana
# placeholders.py


name = "David"
age = "31"
city = "Xalapa"
state = "Veracruz"
country = "Mexico"

message = "name = %s, age = %s \n"
print message%(name, age)

message = "\tMy name is %s \n\tI am %s years old\n\tI am from %s %s, %s"
print message%(name, age, city, state, country)
