
s1 = {"apple","banana","cherry",1,0,True,False}
print(s1)
print(len(s1))

s1.add("pineapple")
print(s1)

s2 = {"orange"}

s1.update(s2)
print(s1)
print(s2)

l1=list(["orange","grapes"])
s1.update(l1);
print(s1)

#s1.remove("berry")
#print(s1)

s1.discard("orange")
print(s1)

print(s1.pop())
print(s1)

s3 = {4,5,"orange"}
s4 = s1.union(s2,s3)

print(s1.union(s2))
print(s4)