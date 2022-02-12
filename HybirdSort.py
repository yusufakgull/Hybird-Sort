def quickSort (dataList, start, end):
    if (start<end):
        if((end-start)<9):
            insertionSort(dataList,start,end+1)
        else:
            part=partition(dataList,start,end)
            quickSort(dataList,start,part-1)
            quickSort(dataList,part+1,end)

def insertionSort(dataList,start,end):
    for i in range(start+1,end):
        current=dataList[i]
        position =i-1
        while position>=0 and current < dataList[position]:
            dataList[position+1] = dataList[position]
            position-=1
        dataList[position+1] = current

def partition(dataList,leftIndex,rightIndex):
    left = leftIndex
    right = rightIndex
    pivot = dataList[leftIndex]
    while left<right :
        if dataList[left] < pivot:
            left+=1
            continue
        if dataList[right] >pivot:
            right-=1
            continue
        temp =dataList[left]
        dataList[left] = dataList[right]
        dataList[right] =temp
        left+=1
    return left


newlist = [5,3,2,1,0,11,24,55,66,22,77,101,55]
quickSort(newlist,0,len(newlist)-1)
print(newlist)