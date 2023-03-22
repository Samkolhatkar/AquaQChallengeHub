# Python program to use

def CorrectingList(listA):
    a = 0
    while a < len(listA):
        print(a)
        for b in reversed(range(a+1,len(listA))):#range(a+1,len(listA)):
            if listA[a] == listA[b]:
                del listA[a:b]
                print(listA)
                break
        a = a+1
    return listA
#----------------------------------------------

def list_sum(listB):
    sum = 0
    for element in range(0,len(listB)):
        sum = sum + listB[element]
    print(sum)



# main for function call.
if __name__ == "__main__":
    #Sample input 
    # L = [1, 4, 3, 2, 4, 7, 2, 6, 3, 6]
    # list_sum(L)
    # list_sum(CorrectingList(L))

    # #Answer for the problem
    with open("02.txt", "r") as input_data:
        data = input_data.readlines()
        print(data)

    L = []

    for l in data:
        as_list = l.split(" ")
        for i in as_list:
            L.append(int(i))

    list_sum(CorrectingList(L))
 
