#Q04

def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b); 

def CoprimeList(n):
    L = []
    for i in range(1,n+1):
        if ( gcd(n,i) == 1 ):
            L.append(i)    
    return L


def list_sum(listB):
    sum = 0
    for element in range(0,len(listB)):
        sum = sum + listB[element]
    print(sum)
    return sum

# main for function call.
if __name__ == "__main__":
    # n = 15
    n = 987820
    list_sum(CoprimeList(n))
