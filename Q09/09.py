#Q09 

def MultiplyLargeList(listA):
    ans = 1
    for elem in range(0, len(listA)):
        ans = ans * listA[elem]

    print(ans)
    return ans




# main for function call.
if __name__ == "__main__":

    with open("09.txt") as f:
        lines = [line.rstrip('\n') for line in f]

    Listfinal = [eval(i) for i in lines]

    MultiplyLargeList(Listfinal)

