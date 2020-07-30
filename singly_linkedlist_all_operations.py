class node:
    def __init__(self,data):
        self.item = data
        self.ref = None
class linkedlist:
    def __init__(self):
        self.start_node = None
    def traverse(self):
        if self.start_node is None:
            print('no elements are there')
            return
        n = self.start_node
        while n is not None:
            print(n.item,'>>',end='')
            n = n.ref
        print()
    def insert_in_emptylst(self,data):
        new_node = node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        else:
            print('the list is not empty')
            return
    def insert_at_beg(self,data):
        new_node = node(data)
        new_node.ref = self.start_node
        self.start_node = new_node
    def insert_at_end(self,data):
        new_node = node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n = n.ref
        n.ref = new_node
    def insert_at_index(self,index,data):
        new_node = node(data)
        if index == 1:
            new_node.ref = self.start_node
            self.start_node = new_node
            return
        n = self.start_node
        i=1
        while n is not None and i<index-1:
            n = n.ref
            i+=1
        if self.start_node is None:
            print('the index is out of bound')
            return
        else:
            new_node.ref = n.ref
            n.ref = new_node
    def count(self):
        if self.start_node is None:
            print('the no of elements are 0')
            return
        else:
            n = self.start_node
            count = 0
            while n is not None:
                count+=1
                n = n.ref
            print(f'the no of elements are {count}')
            return count
    def search(self,x):
        if self.start_node is None:
            print('there are no elements to search')
            return
        n = self.start_node
        i = 0
        while n is not None:
            if n.item == x:
                print(f'element found at {i}')
                return
            n = n.ref
            i+=1
        print('element not found')
        return False
    def delete_at_beg(self):
        if self.start_node is None:
            print('there are no elements to delete')
            return
        self.start_node = self.start_node.ref
    def delete_at_end(self):
        if self.start_node is None:
            print('there are no elements to delete')
            return
        n = self.start_node
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None
    def delete_entire_list(self):
        if self.start_node is None:
            print('there are no elements to delete')
            return
        self.start_node = None
            
    def reverse(self):
        prev = None
        n = self.start_node
        while n is not None:
            next = n.ref
            n.ref = prev
            prev = n
            n = next
        self.start_node = prev
list = linkedlist()
list.insert_in_emptylst(23)
list.insert_at_beg(34)
list.insert_at_end(89)
list.traverse()
list.insert_at_index(2,56)
list.traverse()
list.search(56)
list.search(90)
list.reverse()
list.traverse()
list.count()
list.delete_at_beg()
list.traverse()
list.delete_at_end()
list.traverse()
list.delete_entire_list()
list.traverse()

