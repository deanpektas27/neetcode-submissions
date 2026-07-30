class DynamicArray:
    
    def __init__(self, capacity: int):
        # create a new array with passed in capacity
        self.arr = [0] * capacity
        # save the capacity
        self.capacity = capacity
        # create a variable to hold length (amount of values), initializes to 0
        self.length = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        # check if length equals to capacity, resize if need-be
        if(self.capacity == self.length):
            self.resize()

        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        self.length -= 1
        return self.arr[self.length]

    def resize(self) -> None:
        # double the current capacity
        self.capacity = 2 * self.capacity
        # create new array thats twice capacity of current arr
        new_arr = [0] * self.capacity
        # create loop up to the length of old arr that transfers values from old to new arr
        for i in range(len(self.arr)):
            new_arr[i] = self.arr[i]
        # set new arr to old arr
        self.arr = new_arr

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity