def rand_elem(array):
    temp_array = array

    import random

    return array[random.randint(0, len(array))-1]

print(rand_elem([2, 1, 3, 7]))