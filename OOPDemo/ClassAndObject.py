class MathsOperations:
    operation = "add"
    def add_number(self,a,b):
        return a+b

    def sub_number(self,a, b):
        return a-b

    def mult_number(self,a,b):
        return a*b

'''
# Way - 1 to access memebers of the class using classname
ans = MathsOperations.add_number(2,3)
print(ans)
ans1 = MathsOperations.sub_number(10,3)
print(ans1)
print(MathsOperations.operation)
'''

# Way2 - to access memebers of the class using object

ops1 = MathsOperations()
print(ops1)
print(ops1.add_number(10,20))
print(ops1.add_number(10,40))
ops2 = MathsOperations()
print(ops2)
print(ops2.add_number(100,20))
print(ops2.add_number(100,40))
ops3 = MathsOperations()
print(ops3)
ops4 = MathsOperations()
print(ops4)
