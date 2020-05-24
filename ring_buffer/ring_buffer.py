from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if there's no items yet, make the one added the oldest
        if self.storage.length==0:
            self.storage.add_to_head(item)
            self.current = self.storage.head
        # is the capacity has been reached, replace the oldest val w/ the item,
        # and change the oldest to the oldest.next
        elif self.storage.length == self.capacity:
            self.current.value = item 
            if self.current.next: # self.current.next is not none
                self.current = self.current.next
            else:
                self.current = self.storage.head
        # if the capacity hasn't been reached and already a head, then add to tail
        else:
            self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        current = self.storage.head 
        while current:
            list_buffer_contents.append(current.value)
            current = current.next 

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
