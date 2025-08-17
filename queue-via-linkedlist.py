# Implementasi Queue Menggunakan Linked List

class Item:
    def __init__(self, item):
        self.item = item
        self.next_item = None


class Queue:
    def __init__(self):
        self.front = None # diinisialisasi sebagai item atau antrian pertama dan dianggap masih kosong
        self.rear = None # inisialisasi item terakhir -> dianggap masih kosong
        '''
        Fungsi label item paling belakang (rear) di queue murni 'hanya' digunakan untuk membuat proses penambahan item atau orang baru jadi lebih cepat -> masalah efisiensi waktu
        Berbeda dengan linked list, yang harus satu per satu mencari sambungan dari node pertama hingga terakhir, sebelum menambahkan item baru
        '''
    
    def enqueue(self, item): # salah satu yang membedakan antara linked list dengan queue
        new_item = Item(item)
        if self.front == None:
            self.front = new_item
            self.rear = new_item
        else:
            self.rear.next_item = new_item
            self.rear = new_item
    
    def dequeue(self):
        if self.front == None:
            return None
        else:
            deleted_value = self.front.item
            self.front = self.front.next_item
            if self.front == None:
                print("List kosong!")
                self.rear = None
            return deleted_value
    
    def peek(self):
        if self.front == None:
            return None
        else:
            return self.front.item
        
    def is_empty(self):
        if self.front == None:
            return True
        else:
            return False

    def size(self):
        current_item = self.front
        size = 0
        while current_item != None:
            size += 1
            current_item = current_item.next_item
        return size


item1 = Queue()
item1.enqueue(1)
item1.enqueue(1)
item1.enqueue(1)
print(item1.size())
item1.dequeue()
print(item1.size())
print(item1.is_empty())
print(item1.peek())