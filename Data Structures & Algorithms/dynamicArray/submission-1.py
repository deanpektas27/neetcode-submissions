class DynamicArray:
    
    def __init__(self, capacity: int):
        # STEP 2: save capacity as it could change. This allows us to complete getCapacity function
        self.capacity = capacity
        # STEP 4: assume size (content of array) is empty. ONLY CAPACITY IS PASSED IN CONSTRUCTOR
        self.size = 0
        # STEP 1: initialize an array with provided capacity
        self.arr = [0] * capacity

    def get(self, i: int) -> int:
        # STEP 6:
        # for simplicity, assume index i is ALWAYS valid
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        # set was formally named insert
        # STEP 7 : set n at i-th index
        # (overwrites an existing value)
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        # STEP 8: ADD a new value to end of array
        # (first ensure we have enough space in the capacity of the array)
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        # STEP 10:
        self.size -= 1
        return self.arr[self.size]

    def resize(self) -> None:
        # STEP 9: double capacity, create new array of that new capacity,
        # copy values into new array
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def getSize(self) -> int:
        # STEP 5
        return self.size
    
    def getCapacity(self) -> int:
        # STEP 3
        return self.capacity