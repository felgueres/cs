def list_search(r,k):
    while r and r.key != k:
        r = r.next
    return r

class Data:
    def __init__(self,key):
        self.key = key 
        self.prev = None
        self.next = None

root = Data(9)
root.next = Data(16)
root.next.next = Data(4)
root.next.next.next = Data(1)
