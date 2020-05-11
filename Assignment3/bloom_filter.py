import mmh3
from bitarray import bitarray
import math

class BloomFilter(object):
    def __init__(self, NUM_KEYS, FALSE_POSITIVE_PROBABILITY):
        self.FALSE_POSITIVE_PROBABILITY = FALSE_POSITIVE_PROBABILITY
        self.size = self.bitarray_size(NUM_KEYS, FALSE_POSITIVE_PROBABILITY)
        self.k_times_hash = self.numbers_of_hash(self.size, NUM_KEYS)
        self.bitarray_lst = bitarray(self.size)
        self.bitarray_lst.setall(0)

    def bitarray_size(self,n,p): 
        m = -(n * math.log(p))/(math.log(2)**2) 
        m = int(m)
        return m 

    def numbers_of_hash(self, m, n): 
        k = (m/n) * math.log(2) 
        k = int(k)
        return k

    def add(self, item):
        for i in range(self.k_times_hash):
            x = mmh3.hash(item , i) % self.size
            self.bitarray_lst[x] = 1
    
    def is_member(self, item):
        for i in range(self.k_times_hash):
            x = mmh3.hash(item, i) % self.size
            if self.bitarray_lst[x] == 0:
                return False
        return True

