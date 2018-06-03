python: 
print <var>,
print "Turn", turn + 1  # multiple prints

not # and # or

#good already their functions
.isalpha() # checks if only letters, space gives false
len(<var>) # array length 
.upper() , .lower() 

str(<var>) # changes var into a string 

#conditional logic
if <condition> : 

#functions
def <fucn> () :
def biggest_number(*args):   # when you don’t know how many arguments you have  



s = "Charlie"
print s[0]
# will print "C"

print s[1:4] #not including 4
# will print "har"


%s is stirring
%d is int
%f float
'%s in %s' % (unicode(self.author),  unicode(self.publication))



A module is a file that contains definitions—including variables and functions—that you can use once it is imported.
import this

import math
print math.sqrt(25)
or sqrt = math.sqrt

import math # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print everything # Prints 'em all!

from math import *

type() # returns type of function 

Lists # can have more more than 1 type of variables
animals = ["ant", "bat", "cat"]
animals.append(“whatever”) # adds to list
animals.index(“whatever”) # gives the index of
animals.insert(1, "dog") # add to a specific index
square_list.sort() # sorts
NEVER x = square_list.sort()   #sort then store

for <var> in <list>:
	# assigns var to what’s in list NOT THE INDEX
for index in <dict>:
	#assign index to the keys in dict

del dict_name[key_name] #and lists
.remove(item)

#dictionaries as JSON
my_dict = {
  "fish": ["c", "a", "r", "p"],
  "cash": -4483,
  "luck": "good"
}
print my_dict["fish"][0]


n.pop(index) # will remove the item at index from the list and return it to you
n.remove(item) # will remove the actual item if it finds it
del(n[1]) #is like .pop in that it will remove the item at the given index, but it won't return it

LOOPING IN RANGE
for i in range(0, len(n)):   
      print n[i]
#     range(stop)             
        range(start, stop)
        range(start, stop, step)
range(6)  # [0, 1, 2, 3, 4, 5]
range(1, 6) # [1, 2, 3, 4, 5]
range(1, 6, 3) # [1, 4]
#if x not in range(8)

#LIST OF LISTS
n = [ [1,2] , [3,4] ]

print ["O"] * 5 # ['O', 'O', 'O', 'O', 'O']

letters = ['a', 'b', 'c', 'd']
print " ".join(letters)	       #a b c d
print "---".join(letters)   #a---b---c---d


from random import randint
dice = randint(1, 6)  # 1 to 6 inclusive

raw_input("Guess Row: ")   # for input, takes in a string. Cast as needed


#An alternate way to make our counting loop exit and stop executing is with the break statement.

while/else is similar to if/else, #but there is a difference: the else block will execute anytime the loop condition is evaluated to False. This means that it will execute if the loop is never entered or if the loop exits normally. If the loop exits as the result of a break, the else will not be executed.

.items() #returns an array of tuples with each tuple consisting of a key/value pair from the dictionary
.keys() #method returns a list of the dictionary's keys
.values() #method returns a list of the dictionary's values

list comprehension var = [x**3 for x in range(1, 11) if (x ** 3) % 4 == 0] #no need for if, iff not required
message = filter(lambda x: x != "X", garbled) # filters x out of var

list slicing [start:end:stride]
* start describes slice start (inclusive)
* end is where it ends (exclusive)
* stride describes the space between items in the 

to_five[::2]  #changes strifes
to_five[:2] # starts from beginning
to_five[2:] # ends at end

backwards = my_list[::-1]  #Reverses a list


lambda x: x % 3 == 0, <parameter>  same as   def by_three(x):
  										return x % 3 == 0
Difference: If you plan on creating a function you'll use over and over, you're better off using def and giving that function a name.

f = lambda x,y: x +3 +y
print f(2,5)

#When we pass the lambda to filter, filter uses the lambda to determine what to filter, and the second argument

tuple # essentially a list with static info

#Binary
prints binary: print 0b1,    #1 / print 0b10,   #2 / print 0b11,   #3   # so 0b will give the int of the binary
print a number in its binary representation, you can use the bin() , hex() for hexadecimal #strings
int("110", 2) #gives it as an int instead of string

Left Bit Shift (<<)   # Multiplies by 2 (rounds like an int)
Right Bit Shift (>>) #Divides by 2 (rounds like an int)
&, |
~ #(NOT) will change the sign of the number -1

#Classes
class Animal(object):
  pass		# Pass does not do anything

__init__() # initializer , always has self as a parameter

class Animal(object):
	is_alive = True   #is_alive is accessible by any instance and is not called as a parameter in functions or calls

Inheritance: object can access members of super class
 class SubClass(SuperClass):

# Accessing an overwritten method from SuperClass the .m() {because if overwritten you cant call it, so need to create a new function for it}
class Derived(Base):
  def m(self):
    return super(Derived, self).m()

def __repr__(self):  #represent this object in a format


#File Input/Output
= open("output.txt", "w")   #mode “w” means write ; “r” is read ; “r+” is read and write
.write(“some string”) # method takes a string argument
my_file.close() # if not closed, python will not write to properly
my_file.closed # will return true or false to check if the file is closed or not
print my_file.read() # shows you what’s in the file
.readline() #first line  ; subsequent calls # successive lines
#Automatically closes for you
with open("file", "mode") as variable:
  # Read or write to the file
