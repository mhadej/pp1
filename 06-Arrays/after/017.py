def bubblesort(array):
    buffer = 0
    shift = 1

    while(shift):
        shift = 0
        for i in range(len(array)-1):
            if array[i+1] > array[i]:
                buffer = array[i+1]

                array[i+1] = array[i]
                array[i] = buffer
                shift += 1
    return array

print(bubblesort([2,1,3,7]))
print(bubblesort([-200,1,300,7]))
print(bubblesort([4,2,0,69]))