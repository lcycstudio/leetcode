def merge_sort(list1, list2):
    i = 0
    j = 0
    a = []
    while (i < len(list1) and j < len(list2)):
        if list1[i] <= list2[j]:
            a.append(list1[i])
            i += 1
        elif list2[j] < list1[i]:
            a.append(list2[j])
            j += 1
        print(i)
        print(j)
    for i in range(i,len(list1)):
        a.append(list1[i])
    for j in range(j,len(list2)):
       a.append(list2[j])
    return a


if __name__ == "__main__":
    a = [2,3,5,7,9,12]
    b = [1,4,6,8,10,11]
    merge_sort(a,b)
    print(merge_sort(a,b))