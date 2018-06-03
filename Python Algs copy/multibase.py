def binary(x):
    if x>1:
        binary(x//2)
    #else
    print(x%2,end='')

# test
# binary(83)
# 1010011
        
