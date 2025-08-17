print("Algoritma Searching:")
my_list = [1,3,4,2,7,6,5,9,8]
print("1) Linear Search")
print("="*16)

value = 6 # int(input("Berapa nilai yang kamu ingin cari? "))
value_found = False
print(f"List: {my_list}")

for index, item in enumerate(my_list):
    if item == value:
        print(f"Nilai {value} berada di index ke-{index}\n")
        value_found = True
        break

if not value_found:
    print(f"Nilai {value} tidak ditemukan!\n")

print("2) Binary Search")
print("="*16)

my_list = [2,5,3,1,4,8,6,7,9,11,10,13,12,15,14]
my_list.sort()
value = 16

print(f"List: {my_list}")
start = 0
end = len(my_list) - 1

while start <= end:
    mid = (start + end) // 2
    if value == my_list[mid]:
        print(f"Nilai {value} berhasil ditemukan pada index ke-{mid}")
        break
    elif value < my_list[mid]:
        end = mid - 1
    elif value > my_list[mid]:
        start = mid + 1
else:
    print(f"Nilai {value} tidak ada di dalam list")