A= [32,1,44,5,427] #test
B= [1,5,44,12,120,260,427] #test

#Algorithim determines duplicates in O(n)
def find_duplicates(A,B):
    duplicates = [0]*1001  # makes 1001 indecies (0 to 1000) of 0 value

    for i in A :   # O(n)
        duplicates[i] = 1   # Sets all the indecies of the values in A to 1

    for j in B:  # O(n)
        if duplicates[j] == 1:  # Check all the indecies of the values in B if their 1
            print (j)  # if it is 1, it's in both lists

# O(n) + O(n) = O(2n) = O(n)
find_duplicates(A,B)
