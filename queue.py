my_queue_list = [1,2,3,4]
print(my_queue_list)

def enqueue(some_list, data): # menambahkan elemen di belakang antrian
    some_list.append(data)

enqueue(my_queue_list, 5)
print(my_queue_list)

def dequeue(some_list):
    if not some_list:
        return None
    else:
        return some_list.pop(0)

deleted_value = dequeue(my_queue_list)
print(deleted_value)

def front(some_list):
    if not some_list:
        return None
    else:
        return some_list[0]

print(front(my_queue_list))

def is_empty(some_list):
    if not some_list:
        return True
    else:
        return False

print(is_empty(my_queue_list))

def size(some_list):
    return len(some_list)

print(size(my_queue_list))