print("DICTIONARY FUNCTIONS")
d1={1:"Hello",2:"Hi",3:"Welcome"}
print("PRINT KEYS")
print(d1.keys())
print("PRINT VALUES")
print(d1.values())
print("PRINT KEY VALUES")
print(d1.items())
print("TO GET KEY VALUES")
print(d1.get('Welcome'))
print("TO CREATE COPY OF ")
newd=d1.copy()
print(newd)
print("REMOVES SPECIFIC ELEMENT")
print(d1.pop(1))
print(d1)
print("REMOVES LAST ELEMENT")
print(d1.popitem())
print(d1)
print("TO ADD DATA")
d2={4:"welcome"}
d1.update(d2)
print(d1)
d1.update({5:"Hi"})
d1.clear()
print(d1)
d3={'a','b','c','d'}
d4=dict. fromkeys(d3,1)
print(d4)