print("SET FUNCTIONS")
print("*******add*******")
s={'a','b','c','d'}
s.add('e')
print(s)
print("TO REMOVE ELEMENT")
s.discard('b')
print(s)
s.remove('c')
print(s)
s.pop()
print(s)
s.clear()
print(s)
s1={1,2,99}
s2={2,3,4,105,499}
print("INTERSECTION")
print(s1.intersection(s2))
print("UNION")
print(s1.union(s2))
print("SYMMETRIC DIFFERENCE")
print(s1.symmetric_difference(s2))
s1.update(s2)
print(s1)
print("*******CONVERT LIST TO SET*******")
l1=[1,2,3,4,5]
s1=set(l1)
print(s1)
