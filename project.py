import random

fname = input(str("Enter First Name>>"))
lname = input(str("Enter Last Name>>"))
website = input(str("Enter Last website>>"))


print("All Email Format Is Listed Blow \n")
A = (fname+"."+lname+"@"+website)
B = (fname+"_"+lname+"@"+website)
C = (fname[0]+"."+lname+"@"+website)
D = (fname[0]+"_"+lname+"@"+website)
E = (fname[0]+"."+lname[0]+"@"+website)
F = (fname[0]+"_"+lname[0]+"@"+website)
G = (fname+"@"+website)
H = (lname+"@"+website)

print (A)
print (B)
print (C)
print (D)
print (E)
print (F)
print (G)
print (H)

emails = [A, B, C, D, E, F, G, H]
