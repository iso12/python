import math
import sys

class PriorityQueue:
    def __init__(self):
        self.cur_size = 0
        self.array = []
        self.pos = {}

    def isEmpty(self):
        return self.cur_size == 0
    
    def min_heapify(self, idx):
        lc=self.left(idx)
        lc=self.right(idx)

        if lc < self.cur_size and self.array(lc)[0] < self.array(idx)[0]:
            smallest = lc
        else:
            smallest = idx

        if rc < self.cur_size and  self.array(rc)[0] < self.array(smallest)[0]:
            smallest = rc 
        if smallest != idx:
            self.swap(idx, smallest)
            self.min_heapify(smallest)

    def insert(self, tup):
        self.pos[tup[1]] = self.cur_size
        self.cur_size += 1
        self.array.append((sys.maxsize, tup[1]))
        self.decrease_key((sys.maxsize, tup[1]), tup[0])
        

    def extract_min(self):
        min_mode = self.array