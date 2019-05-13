class Node(object):
    """Node"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class SingleLinkList(object):
    def __init__(self, node=None):
        self.__head = node
        if node: 
            node.next = node 

    def is_empty(self):
        return self.__head == None

    def length(self):
        if self.is_empty():
            return 0
        cur = self.__head
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count
        
    def travel(self):
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem, end = " ")
            cur = cur.next
        print(cur.elem)
    
    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            self.__head = node
            cur.next = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            cur.next = node

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < (pos-1):
                count += 1
                pre = pre.next
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        if self.is_empty():
            return
        cur = self.__head
        pre = None
        while cur.next != self.__head:
            if cur.elem == item:
                if cur == self.__head:
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    pre.next = cur.next
                return 
            else:
                pre = cur
                cur = cur.next
        if cur.elem == item:
            if cur == self.__head:
                self.__head = None
            else:
                pre.next = self.__head


    def search(self, item):
        cur = self.__head
        if self.is_empty():
            return False
        while cur.next != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        if cur.elem == item:
            return True
        return False

if __name__ == "__main__":
    ll = SingleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())
          
    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)

    ll.insert(-1,9)
    ll.travel()
    print("")
    ll.insert(2,100)
    ll.travel()
    print("")
    ll.insert(10,299)
    ll.travel()
    print("")
    ll.remove(9)
    ll.travel()
    print("")
    ll.remove(6)
    ll.travel()
    
    print("")
    ll.remove(299)
    ll.travel()
    
    print("")
    ll.remove(3)
    ll.travel()

