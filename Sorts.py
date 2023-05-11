

#Some sorts, if I needed some


#bubble_sort
def bubble(array):
    swapped = False
    n = len(array) - 1

    while not swapped:
        swapped = True
        for i in range(0,n):
            if array[i] > array[i+1]:
                swapped = False
                array[i], array[i+1] = array[i+1], array[i]

    return array

#selection_sort
def selection_sort(array):
    n = len(array)
    for i in range(n-1):
        min_value = i
        
        for j in range(i+1,n):
            if array[j] < a[min_value]:
                min_value = j
        if min_value != i:
            a[min_value], a[i] = a[i], a[min_value]
            
    return array


#insertion_sort
def insertion_sort(array):
    n = len(array)
    for i in range(1,n):
        value_2_sort = array[i]
    
        while a[i-1] > value_2_sort and i > 0:
            array[i], array[i-1] = array[i-1], array[i]
            i -= 1
    return(array)
    

#quick_sort
def quicksort(array):
    lenght = len(array)
    if lenght <= 1:
        return array
    else:
        pivot = array.pop()

    greater = []
    lower = []

    for i in array:
        if i > pivot:
            greater.append(i)
        else:
            lower.append(i)
    return quicksort(lower) + [pivot] + quicksort(greater)



#merge_sort
def merge(array):
    lenght = len(array)
    if lenght < 20:
        return sorted(array)

    result = []

    mid = int(lenght / 2)
    y = merge(array[:mid])
    z = merge(array[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1
    result += y[i:]
    result += z[j:]
    return result    



