'''array1 = [1,2,3]
print(array1)

array1.append(4)
print(array1)

print(array1[1])

array1[1] = 5
print(array1[1])

print(array1)

array1.pop(2)
print(array1)'''

data_angka = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
panjang_data = len(data_angka)

# mencetak semua elemen yang berada di indeks ganjil
for a in range(panjang_data):
    if a % 2 == 1:
        print(data_angka[a])
print()

# ganti setiap elemen yang merupakan kelipatan 3 dengan nilai 0
for a in range(panjang_data):
    if data_angka[a] % 3 == 0:
        data_angka[a] = 0

print(data_angka)

# sisipkan angka 55 di antara elemen 50 dan 60
for a in range(panjang_data):
    if a == 5:
        data_angka.insert(a, 55)

print(data_angka)