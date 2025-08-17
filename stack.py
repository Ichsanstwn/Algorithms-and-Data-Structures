my_stack_list = [1,2,3]
print(my_stack_list)

def append(some_list, data): # menambahkan elemen ke atas stack
    some_list.append(data)

append(my_stack_list, 4)
print(my_stack_list)

def pop(some_list): # menghapus dan mengembalikan elemen dari atas stack
    if not some_list:
        return None
    else:
        return some_list.pop()

deleted_value = pop(my_stack_list)
print(deleted_value)
print(my_stack_list)

def peek(some_list): # melihat elemen teratas stack
    if not some_list:
        return None
    else:
        return some_list[-1]

print(peek(my_stack_list))

def is_empty(some_list): # memeriksa apakah stack kosong
    if some_list == []:
        return True
    else:
        return False

print(is_empty(my_stack_list))

def get_length(some_list): # mengetahui berapa banyak elemen di dalam stack
    return len(some_list)

print(get_length(my_stack_list))