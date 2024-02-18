class LinkedList(object):
    def __init__(self):
        self.head = None
    def append(self, value):
        pass
    def get(self,idx):
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value 