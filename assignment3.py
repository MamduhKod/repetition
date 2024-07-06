original_list = [1,56,2,77,33,6]

def add_elements(element):
    original_list.append(element)
    return

add_elements(1)

print(original_list)

def remove_elements(element):
    original_list.remove(element)
    return

remove_elements(1)

print(original_list)

def find_smallest():
    smallest = min(original_list)
    print("the smallest value is", smallest)
    return

find_smallest()

def find_largest():
    largest = max(original_list)
    print("the largest value is",largest)
    return

find_largest()



    