class Item: # digunakan untuk membuat data atau dokumen baru
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable: # digunakan untuk membuat meja arsip, tempat untuk menyimpan dokumen
    def __init__(self, size): # di bagian metode __init__ digunakan untuk menginisialisasi setiap atribut yang dibutuhkan dalam membuat meja arsip
        self.number_of_drawers = size # argumen 'size' dikirimkan oleh user, kemudian 'size' tersebut disimpan dan akan digunakan sebagai acuan dalam menentukan jumlah laci pada meja arsip yang dibuat dan membantu kita jika suatu saat ingin mengecek jumlah laci yang tersisa
        self.table = [] # menyiapkan meja arsip yang belum memiliki laci
        for i in range (self.number_of_drawers): # menyiapkan laci di dalam meja arsip sesuai dengan jumlah yang diminta
            self.table.append([])

    def hash_function(self, key): # mengkategorikan mana nomor laci yang sesuai dengan dokumen yang ingin disimpan
        return hash(key) % self.number_of_drawers # fungsi hash() adalah fungsi bawaan Python yang digunakan untuk mengubah masukan (key) seperti string menjadi angka integer yang besar, maka modulus (%) number_of_drawers akan menyesuaikan angka tersebut agar berada dalam rentang laci yang kita miliki
    
    '''
    Sistem penomoran otomatis untuk judul-judul dokumen atau data kita. Ketika kita ingin menyimpan atau mencari sebuah dokumen, kita memberikan judul dokumen ke sistem penomoran otomatis. Kemudian, sistem akan memproses judul tersebut melalui sebuah rumus atau perhitungan.
    Sistem akan memberi tahu secara pasti nomor laci mana yang sesuai dengan judul dokumen. Nomor laci yang diberikan oleh sistem akan selalu berada dalam rentang jumlah laci yang kita miliki di meja arsip yang telah kita buat.
    '''

    def add_item(self, key, value):
        drawer_number = self.hash_function(key)
        new_item = Item(key, value)
        key_found = False
        for item in self.table[drawer_number]:
            if item.key == new_item.key:
                item.value = new_item.value
                key_found = True
                break # kamu sudah mengecek apakah key sudah ada, lalu memperbarui nilainya -> lebih efisien langsung break
        if key_found == False:
            self.table[drawer_number].append(new_item)
    
    def get_item(self, key):
        drawer_number = self.hash_function(key)
        for item in self.table[drawer_number]:
            if item.key == key:
                return item.value
        return None
    
    def remove_item(self, key):
        drawer_number = self.hash_function(key)
        for index, item in enumerate(self.table[drawer_number]):
            if item.key == key:
                self.table[drawer_number].pop(index)
                return # untuk menghentikan fungsi lebih cepat setelah pekerjaan selesai -> return digunakan untuk menghentikan fungsi (bisa mengembalikan nilai atau tidak), bedanya dgn break: break menghentikan loop
    
    def check_the_key(self, key):
        drawer_number = self.hash_function(key)
        for item in self.table[drawer_number]:
            if item.key == key:
                return True
        return False

    def get_keys(self):
        all_the_keys = []
        for drawer in self.table:
            for item in drawer:
                all_the_keys.append(item.key)
        return all_the_keys
    
    def get_values(self):
        all_the_values = []
        for drawer in self.table:
            for item in drawer:
                all_the_values.append(item.value)
        return all_the_values
    
    def get_items(self):
        all_the_items = []
        for drawer in self.table:
            for item in drawer:
                all_the_items.append((item.key, item.value))
        return all_the_items
    
    def clear(self):
        for drawer in self.table:
            drawer.clear()

    def is_empty(self):
        for drawer in self.table:
            # if drawer != []: -> benar secara logika, tapi belum cukup alami untuk bahasa Python
            if drawer: # benar secara logika dan alami untuk bahasa Python
                return False
        return True
    
    def total_item(self):
        total = 0
        for drawer in self.table:
            for item in drawer:
                total = total + 1
        return total


archives1 = HashTable(10)
archives1.add_item(1, "Kopi")
archives1.add_item(2, "Teh")
archives1.add_item(3, "Jus")
print(archives1.get_item(3))
archives1.add_item(3, "Milkshake")
print(archives1.get_item(3))
print(archives1.get_item(1))
archives1.remove_item(1)
print(archives1.check_the_key(1))
print(archives1.check_the_key(2))
print(archives1.get_keys())
print(archives1.get_values())
print(archives1.get_items())
print(archives1.is_empty())
print(archives1.total_item())

"""
Momen ketika mencari fungsi mencetak list dalam list yang tepat

def try_looping_list(size):
    first_list = [[]] * size
    return first_list

first_list = try_looping_list(5)
print(first_list)
first_list[0].append("Apple")
print(first_list)

def looping_list(size):
    some_list = []
    for i in range (size):
        some_list.append([])
    return some_list

some_list = looping_list(5)
print(some_list)
some_list[0].append("Apple")
print(some_list)
"""