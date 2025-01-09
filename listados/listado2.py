# instruciones simples 
a=10
b=12
c= a + b
print(a,b,c)

# instruciones complejas
if a > b:
    print("a es mayor que b") 
elif a == b:
    print("a es igual que b")  
else:
    print("a es menor que b")

valores = range(5)
for i in valores:
    print(i)

lenguajes=["python","java","c++","c#"]
for lenguaje in lenguajes:
    print(lenguaje)

a = 1
b = 5
while a <= b:
    print(a)
    a= a+1
else:
    print("procesados los 5 elementos")