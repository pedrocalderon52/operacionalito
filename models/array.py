from myqueue import Queue, Node

class ArrayDeFilas():
    def __init__(self):
        self.p1 = Queue()
        self.p2 = Queue()
        self.p3 = Queue()
        self.p4 = Queue()
        self.p5 = Queue()




print([None] * 7)




class Array:
    def __init__(self, size):
        self.size = size
        self.data = self._create_empty_data(size)

    def _create_empty_data(self, size):
        # Creates a linked list of 'size' number of empty nodes.
        if size <= 0:
            return None
        
        root = Node(None)
        current = root
        
        i = 1
        while i < size:
            current.next = Node(None)
            current = current.next
            i += 1
        return root

    def __getitem__(self, index):
        if index < 0 or index >= self.size:
            return None
        current = self.data
        i = 0
        while i < index and current is not None:
            current = current.next
            i += 1
        
        return current.valor
        

    def __setitem__(self, index, value):
        if index < 0 or index >= self.size:
            return
        current = self.data
        i = 0
        while i < index and current is not None:
            current = current.next
            i += 1
        if current is not None:
            current.valor = value

    def add(self, data):
        # Adds data to the first empty slot.
        i = 0
        while i < self.size:
            if self.get(i) is None:
                self.set(i, data)
                return
            i += 1

    def get(self, index):
        return self.__getitem__(index)

    def set(self, index, value):
        self.__setitem__(index, value)

    def __str__(self):
        result = "["
        current = self.data
        first = True
        while current is not None:
            if not first:
                result += ", "
            result += repr(current.valor)
            first = False
            current = current.next
        result += "]"
        return result

    def __repr__(self):
        return f"Array(size={self.size}, data={self})"

