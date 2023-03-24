# Python program to use

def to_hex_chars(string_a):
    new_string = ""
    for a in range(0,len(string_a)):
        if string_a[a] not in "0123456789abcdef":
            new_string += '0'
        else:
            new_string += string_a[a]
    return new_string

def to_three_times_length (string_b):
    l = len(string_b)
    if (l%3 == 1):
        string_b += "00"
    if (l%3 == 2):
        string_b += "0"
    return string_b
        
def convert_to_hex(string_c):
    n = len(string_c)
    k = 0
    hex_string = ""
    size_new = n/3
    for char in string_c:
        if k% size_new == 0 or k% size_new == 1:
            # print()
            hex_string += char
        k +=1
    print(hex_string)
    return hex_string 

def hex_code(string_input):
    return convert_to_hex(to_three_times_length(to_hex_chars (string_input)))

#----------------------------------------------



# main for function call.
if __name__ == "__main__":

    # input_string = "kdb4life"
    input_string = "do you think that maybe like, 1 in 10 people could be actually robots?"
    hex_code(to_three_times_length(to_hex_chars (input_string)))

