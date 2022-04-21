
IDENTITY = lambda x: x
class SortedList:
    
    def __init__(self, sequence=None, key=None):
        self.__key = key or IDENTITY
        assert hasattr(self.__key, "__call__")
        if sequence is None:
            self.__list = []
        elif (isinstance(sequence, SortedList)) and sequence.key == self.__key:
            self.__list = sequence.__list[:]
        else:
            self.__list = sorted(list(sequence), key=self.__key)
    
    @property
    def key(self):
        return self.__key
    
    def add(self, value):
        index = self.__bisect_left(value)
        if index == len(self.__list):
            self.__list.append(value)
        else:
            self.__list.insert(index, value)
    
    def __bisect_left(self, value) -> int:
        key = self.__key(value)
        left, right = 0, len(self.__list)
        while left < right:
            middle = (left + right) // 2
            if self.__key(self.__list[middle]) < key:
                left = middle + 1                             
            else:
                right = middle
        return left
    

    def remove(self, value):
        index = self.__bisect_left(value)
        if index < len(self.__list) and self.__list[index] == value:
            del self.__list[index]
        else:
            raise ValueError(f"{self.__class__.__name__}.remove(x): x not in list")
    
    def remove_every(self, value) -> int:
        index = self.__bisect_left(value)
        count = 0
        while (index < len(self.__list) and self.__list[index] == value):
            del self.__list[index]
            count += 1
        return count
    
    def count(self, value) -> int:
        index = self.__bisect_left(value)
        count = 0
        while (index < len(self.__list) and self.__list[index] == value):
            index += 1
            count += 1
        return count
    

    def index(self, value) -> int:
        index = self.__bisect_left(value)
        if index < len(self.__list) and self.__list[index] == value:
            return index
        raise ValueError(f"{self.__class__.__name__}.index(x): x not in list")
    

    def __delitem__(self, index):
        del self.__list[index]
    

    def __getitem__(self, index):
        return self.__list[index]
    

    def __setitem__(self, index, value):
        raise TypeError("use add() to insert a value and rely on the list to put it in the right place")
    
    
    def __iter__(self):
        return iter(self.__list)
    

    def __reversed__(self):
        return reversed(self.__list)
    

    def __contains__(self, value):
        index = self.__bisect_left (value)
        return (index < len(self.__list) and self.__list[index] == value)


    def clear(self):
        self.__list = []
    

    def pop(self, index=-1):
        return self.__list.po(index)
    
    
    def __len__(self):
        return len(self.__list)
    

    def __str__(self):
        return str(self.__list)
    

    def copy(self):
        return SortedList(self, self.__key)
    
    __copy__ = copy