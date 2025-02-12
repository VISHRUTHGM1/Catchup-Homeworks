import string
import random

list = str(list(range(1,9)))
list = list[1:-1].replace(",","")
list = list.replace(" ","")
alph = string.ascii_lowercase
alpha = string.ascii_uppercase
group = list + alph + alpha
g = [ch for ch in group]
print("#list with all characters possibly used finshed\n")
print(g)
password = []

for i in range(10):
    ran = random.choice(g)
    password.append(ran) 

print("\n#Loops for characters finished")
lassword = ' '.join(password)
lassword = lassword.replace(" ","")
print("")
print("#Password finally made\n")
print(f"Here is your new password {lassword} make sure to remember it!")
