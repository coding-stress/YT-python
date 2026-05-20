# Create a empty dictionary. Allow 4 friends to enter their favorite language as value and use kay as their names. Assume that names are unique.

d = {}

name = input("enter friends name : ")
lang = input ("enter language name :")
d.update({name: lang})
name = input("enter friends name : ")
lang = input ("enter language name :")
d.update({name: lang})
name = input("enter friends name : ")
lang = input ("enter language name :")
d.update({name: lang})
name = input("enter friends name : ")
lang = input ("enter language name :")
d.update({name: lang})

print(d)