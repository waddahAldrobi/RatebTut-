class Range:
    def __init__(self,start,stop = None,step=1):
        if step == 0:
            raise ValueError('step can not be 0')
        if stop is None:
            start,stop = 0,start

        self._length=max(0,((stop-start+step-1)//step))
        self._start = start
        self._step = step
        self._stop = stop

    def __len__(self):
        return self._length

    def __getitem__(self, k):
        if k<0:
            k += len(self)

        if not 0 <= k < len(self):
            raise IndexError('index out of range')
        return self._start+ k*self._step


class ModifiedRange(Range):
    def __contains__(self, item):
        #if item is greater than stop or less than start (out of range)
        if self._stop-1 < item or item < self._start : return False
        
        #if in range
        for i in range(self._length):
            if self._start + self._step*i == item :  #keeps checking, taking step into consideration
                return True
    
        #if not found, return False
        return False

#test
#a = ModifiedRange(0,7,2)
#print 3 in a  => returns False

