# Python program to use

# def (map_a,) 
#----------------------------------------------



# main for function call.
if __name__ == "__main__":

    num_key_map = {
                2 : ' abc' ,
                3 : ' def' ,
                4 : ' ghi' ,
                5 : ' jkl' ,
                6 : ' mno' ,
                7 : ' pqrs',
                8 : ' tuv' ,
                9 : ' wxyz',
                0 : '  '
        }

    #Answer for the problem
    with open("00.txt", "r") as input_data:
        data = input_data.readlines()

    M = ""
    for l in data:
        num, seq = map(int, l.split())
        # print(num , seq)
        M += (num_key_map[num][seq])

    print(M, end=' \n')
 
