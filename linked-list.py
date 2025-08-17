class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None # diinisialisasi sebagai node pertama dan dianggap masih kosong
    
    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            '''
            self.head = new_node -> head menunjuk new_node sebagai node pertamanya (mengubah struktur list, head pindah ke node baru)
            kalau new_node = self.head -> hanya menyalin informasi dari head ke new_node
            '''

        else:
            current_node = self.head
            while current_node.next_node != None:
                current_node = current_node.next_node
            current_node.next_node = new_node
    
    def print_list(self):
        if self.head == None:
            return None
        else:
            current_node = self.head
            while current_node != None:
                print(current_node.data, end=" -> ") # hanya untuk estetika
                current_node = current_node.next_node
            print(None)
    
    def delete_node(self, data):
        if self.head == None:
            return None
        elif self.head.data == data:
            self.head = self.head.next_node
        else:
            current_node = self.head
            previous_node = None
            while current_node != None and current_node.data != data:
                previous_node = current_node
                current_node = current_node.next_node
            if current_node == None:
                return None
            else:
                previous_node.next_node = current_node.next_node
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next_node = self.head # node baru akan menunjuk ke head lama
        self.head = new_node # head baru adalah node baru, sekaligus mengubah titik masuk dari head yang lama ke head yang baru (node baru)

    def insert_after(self, data, key):
        new_node = Node(data)
        current_node = self.head
        while current_node != None and current_node.data != key:
            current_node = current_node.next_node
        if current_node == None:
            return None
        else:
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node

    def get_length(self):
        current_node = self.head
        length = 0
        while current_node != None:
            length += 1
            current_node = current_node.next_node
        return length
    
    def search(self, data):
        current_node = self.head
        while current_node != None and current_node.data != data:
            current_node = current_node.next_node
        if current_node == None:
            return False
        else:
            return True


node1 = LinkedList()
node1.append(1)
node1.append(2)
node1.append(3)
node1.print_list()
node1.prepend(0)
node1.print_list()
node1.insert_after(4,2)
node1.print_list()
node1.insert_after(4,5)
print(node1.get_length())
print(node1.search(3))