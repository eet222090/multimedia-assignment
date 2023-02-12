class Node:
    def __init__(self, freq, char, left=None, right=None):
         self.freq = freq

         self.char = char

         self.left = left

         self.right = right

         self.code = ''

    def __lt__(self, next):
        return self.freq < next.freq

class MinHeap:

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.heap = [Node(0, '\0')]*(self.maxsize + 1)
        self.heap[0] = Node(-1 * 30000, '\0')
        self.front = 1


    def parent(self, pos):
        return pos//2

    def left_child(self, pos):
        return 2 * pos

    def right_child(self, pos):
        return (2 * pos) + 1

    def is_leaf(self, pos):
        return 2 * pos > self.size

    def swap(self, fpos, spos):
        self.heap[fpos], self.heap[spos] = self.heap[spos], self.heap[fpos]

    def min_heapify(self, pos):

        if not self.is_leaf(pos):
            if (self.heap[pos] > self.heap[self.left_child(pos)] or self.heap[pos] > self.heap[self.right_child(pos)]):

                if self.heap[self.left_child(pos)] < self.heap[self.right_child(pos)]:
                    self.swap(pos, self.left_child(pos))
                    self.min_heapify(self.left_child(pos))

                else:
                    self.swap(pos, self.right_child(pos))
                    self.min_heapify(self.right_child(pos))

    
    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.heap[self.size] = element

        curr = self.size

        while self.heap[curr] < self.heap[self.parent(curr)]:
            self.swap(curr, self.parent(curr))
            curr = self.parent(curr)

    def print_heap(self):
        for i in range(1, (self.size//2) + 1):
            print("parent: " + str(self.heap[i].freq) + " left child: " +
                                str(self.heap[2 * i].freq) + " right child: " +
                                str(self.heap[2 * i + 1].freq))

    def min_heap(self):
        for pos in range(self.size//2, 0, -1):
            self.min_heapify(pos)

    def remove(self):
        if self.size > 0:
            popped = self.heap[self.front]
            self.heap[self.front] = self.heap[self.size]
            self.size -= 1
            self.min_heapify(self.front)
            return popped

if __name__ == "__main__":

    # print('The min heap is')
    minHeap = MinHeap(15)
    minHeap.insert(Node(3,"a"))
    minHeap.insert(Node(17,"b"))
    minHeap.insert(Node(10,"c"))
    minHeap.insert(Node(84,"d"))
    minHeap.insert(Node(19,"a"))
    minHeap.insert(Node(6,"f"))
    minHeap.insert(Node(22,"a"))
    minHeap.insert(Node(9,"a"))
    minHeap.min_heap()

while(minHeap.size > 1):
    minHeap.print_heap()
    first = minHeap.remove()
    second = minHeap.remove()
    minHeap.insert(Node((first.freq + second.freq), first.char + second.char))
    minHeap.min_heap()
    print("------------------end------------------")
    print(minHeap.size)
