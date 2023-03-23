# Python program to use

def goodnumbercount(a):
    count = 0 
    for i in range(1,a+1):
        lista = numbertolist(i)
        num_count = 0
        for a in range(0,len(lista)-1):
            if lista[a] <= lista[a+1]:
                num_count = num_count+1

        if num_count == len(lista)-1:
            count = count + 1

    print(count)        
    return count            


def numbertolist(a):
    digitlist = [int(x) for a,x in enumerate(str(a))]
    return digitlist


# main for function call.
if __name__ == "__main__":
    goodnumbercount(520185742) +1 