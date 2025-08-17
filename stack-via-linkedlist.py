# Implementasi Stack Menggunakan Linked List

class Item:
    def __init__(self, data):
        self.data = data
        self.next_data = None # untuk menunjuk data yang ada di bawahnya


class Stack:
    def __init__(self):
        self.top = None # inisialisasi item pertama yang berada paling atas -> dianggap masih kosong
    
    def push(self, data): # seperti metode prepend pada linked list, karena konsep menambahkan item baru pada stack adalah item baru selalu berada di atas item lama
        new_item = Item(data)
        new_item.next_data = self.top
        self.top = new_item
    
    def pop(self):
        if self.top == None:
            return None
        else:
            deleted_value = self.top.data # menyimpan nilai yang akan dihapus
            self.top = self.top.next_data
            return deleted_value
        
    def peek(self):
        if self.top == None:
            return None
        else:
            return self.top.data
        
    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False
        
    def size(self):
        current_node = self.top
        size = 0
        while current_node != None:
            size += 1
            current_node = current_node.next_data
        return size


item1 = Stack()
item1.push(1)
item1.push(2)
item1.push(3)
print(item1.pop())