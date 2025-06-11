n = int(input())
count = 0
for _ in range(n):
    shape = input()
    if shape == "Tetrahedron":
        count += 4
    elif shape == "Cube":
        count += 6
    elif shape == "Octahedron":
        count += 8
    elif shape == "Dodecahedron":
        count += 12
    elif shape == "Icosahedron":
        count += 20

print(count)