def display7():
    code = '''a={10,20,30,40,50}
b={30,40,50,60,70}
c={10,20}
d={80,90}
print("set a:",a)
print("set b:",b)
print("set c:",c)
print("set d:",d)
print("\\n 1.union:",a|b)
print("\\n 2.intersection:",a&b)
print("\\n 3.difference:",a-b)
print("\\n 4.difference:",b-a)
print("\\n 5.symmetric difference:",a^b)
print("Is c subset of a:",c.issubset(a))
print("Is a superset of c:",a.issuperset(c))
print("Are a and b disjoint:",a.isdisjoint(d))
a.add(100)
print("\\n after adding 100 to a:",a)
a.remove(10)
print("\\n after removing 10 from a:",a)'''
    print(code)
