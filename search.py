#-------------------------------
def binarySearch(data, item):
    low = 0
    hight = len(data)-1
    while (low <= hight) :
        mid = (low+hight)//2
        guess = data[mid]
        if guess == item:
            return mid
        if guess < item:
            low = mid+1
        else:
            hight = mid-1
    return None

def binarySearchRecursive_Impl(data, item, low, hight):
    if (low <= hight):
        mid = (low+hight)//2
        if (data[mid] == item):
            return mid
        elif (data[mid] < item):
            return binarySearchRecursive_Impl(data, item, mid+1, hight)
        else:
            return binarySearchRecursive_Impl(data, item, low, mid-1)
    else:
        return None

def binarySearchRecursive(data, item):
    return  binarySearchRecursive_Impl(data, item, 0, len(data)-1)
    

#-------------------------------
def sortSimple(data):
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[j] < data[i]:
                tmp = data[j]
                data[j] = data[i]
                data[i] = tmp
#-------------------------------
def sortByInsert(data):
    for i in range(1,len(data)):
        j = i-1
        key = data[i]
        while (j >= 0 and data[j] > key):
            data[j+1] = data[j]
            j-=1
        data[j+1] = key
#-------------------------------
            
def sortBubbles(data):
    for i in range(len(data)):
        for j in range(len(data)-i-1):
            if (data[j] > data[j+1]):
                tmp = data[j+1]
                data[j+1] = data[j]
                data[j] = tmp
#-------------------------------
def sum_impl (data, index):
    if index == len(data) -1 :
      return data[index]
    return data[index] + sum_impl(data, index+1)
def sum(data):
    return sum_impl(data, 0) 
#-------------------------------
def quickSort(data):
    if len(data) < 2:
        return data
    pivot = data[0]
    less = [i for i in data[1:] if i <= pivot]
    greater = [i for i in data[1:] if i > pivot]
    return quickSort(less) + [pivot] + quickSort(greater)

