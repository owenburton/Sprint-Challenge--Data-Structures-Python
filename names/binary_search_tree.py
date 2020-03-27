import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None 

    ## PLAN FOR INSERT
    # create a new instance of BinarySearchTree w/ the new value 
    # if there's no Queue, then initialize one 
    # initialize variable current as the queue head
    # if new value is less than current.value, current becomes current.left
    # if new val < current.value & current.left==None, then current.left==BinarySearchTree(val) & break
    # if the new value is greater than current.value, current becomes current.right
    # if new val > current.value & current.right==None, then current.right==BinarySearchTree(val) & break

    # Insert the given value into the tree
    def insert(self, value): 
        if value < self.value:
            if self.left==None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

        if value >= self.value:
            if self.right==None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

        
    ## PLAN FOR CONTAINS
    # initialize var current as queue head
    # if target==current.value, return 1
    # if current==None, return 0
    # if target < current.value, current becomes current.left 
    # if target > current.value, current becomes current.left 
    # return True if total > than 0 else False

    # Return True if the tree contains the value
    # False if it does not
    # def contains(self, target): 
    #     if self.value==target:
    #         return 1
    
    #     return 1 in (self.left.contains(target) if self.left else 0, \
    #                  self.right.contains(target) if self.right else 0)

    def contains(self, target):
        if self.value==target: 
            return True 
        if target < self.value: 
            if self.left: 
                return self.left.contains(target) 
        if target > self.value: 
            if self.right: 
                return self.right.contains(target)
        
        
        
        
    ## PLAN FOR GET_MAX
    # start at the root 
    # intialize var current as head/root
    # while current is not None
    # current = current.right
    # if current is None, return no max/NA, or maybe just return (do nothing)
    # else return current.value

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            return self.value
        return self.right.get_max()
        

    ## PLAN FOR FOR_EACH
    # initialize current as head 
    # base case is None, so
    # if current is None, stop/do nothing/maybe return None 
    # call the function recursively in the return statement

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
        
        


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            node.left.in_order_print(node.left)
        print(node.value)
        if node.right: 
            node.right.in_order_print(node.right)
        

    ## PLAN FOR DFT
    # initialize a queue 
    # enqueue root to queue 
    # while queue not empty 
    # dequeue top item out of queue to temp 
    # apply a function to temp 
    # if temp has right, put right in queue 
    # if temp has left, put left in queue

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue() 
        q.enqueue(node)
        while q.size > 0:
            temp = q.dequeue()
            print(temp.value)
            if temp.right:
                q.enqueue(temp.right)
            if temp.left:
                q.enqueue(temp.left)


    ## PLAN FOR DFT
    # initialize a stack 
    # push root to stack 
    # while stack not empty 
    # pop top item out of stack to temp 
    # apply a function to temp 
    # if temp has right, put right in stack 
    # if temp has left, put left in stack

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        s = Stack() 
        s.push(node)
        while s.size > 0:
            temp = s.pop() 
            print(temp.value) 
            if temp.right:
                s.push(temp.right) 
            if temp.left: 
                s.push(temp.left) 

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
