a = "hello ya baba"

def reverse_a_string_more_slowly(a_string):
    temp = ""
    i=len(a_string)-1
    while (i>=0):
        temp += a_string[i]
        i-=1



    return temp

print (reverse_a_string_more_slowly(a))





