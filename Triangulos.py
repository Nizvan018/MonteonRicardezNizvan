asteriscos = "*"
i = 0

print()
print("Primer triángulo:")
print()

for i in range(1,6):
    print(asteriscos*i)

print()
print("Segundo triángulo:")
print()

for j in range(1,6):
    print(asteriscos*i)
    i = i - 1

print()
print("Tercer triángulo")
print()

for i in range(1,6):
    print(asteriscos*i)

for j in range(1,6):
    i = i - 1
    print(asteriscos*i)

print()
print("Cuadrado")
print()

for i in range(0,6):
    print(asteriscos*6)
