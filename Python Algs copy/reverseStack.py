class Stack:
    def __init__ (self):
        self._data = []

    def len (self):
         return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e) # new item stored at end of list

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self._data.pop()

#Q6
def insertTop(S, element):
    if S.is_empty():
        S.push(element)
    else:
        temp = S.pop()
        insertTop(S, element)
        S.push(temp)


def reverse(S):
    # if stack has elements
    if not S.is_empty():
        temp = S.pop()  # store and remove last element
        reverse(S)  # reverse all stack except last
        insertTop(S, temp) # add it again

#Test
a = Stack()
a.push(1)
a.push(2)
a.push(3)
reverse(a)
print(a.pop()),
print(a.pop()),
print(a.pop())
#output : 1 2 3  ; so it's been reversed