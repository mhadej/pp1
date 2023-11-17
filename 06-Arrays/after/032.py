def second_largest(array):
    temp_array = array.copy()
    sorted1 = sorted(temp_array)

    return sorted1[len(temp_array)-2]

def amplitude(array):
    temp_array = array.copy()
    return max(temp_array) - min(temp_array)

def median(array):
    temp_array = array.copy()

    shuffle = 1
    buffer = 0

    while(shuffle):
        shuffle = 0
        for i in range(len(temp_array)-1):
            if temp_array[i+1] > temp_array[i]:
                buffer = temp_array[i]

                temp_array[i] = temp_array[i+1]
                temp_array[i+1] = buffer

                shuffle += 1
    
    if len(temp_array)%2:
        return temp_array[int(len(temp_array)/2)]
    else:
        return (temp_array[int(len(temp_array)/2)] + temp_array[int((len(temp_array)/2)+1)])/2 

def twos(array):
    temp_array = array.copy()
    new_array = [min(temp_array), max(temp_array)]

    return temp_array 

def string(array):
    temp_array = array.copy()

    end_string = str(temp_array[0])
    for i in range(1, len(temp_array)):
        end_string += "-" + str(temp_array[i]) 
    
    return end_string

array2 = [7, 3, 8, 5, 2]

print("2nd largest:",second_largest(array2))
print("Amplitude:", amplitude(array2))
print("Median:", median(array2))
print("Two-two:", twos(array2))
print("String:", string(array2))