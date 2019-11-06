class Deque:
    def __init__(self):
        self.items = []
        self.n = 8
        self.back = None
        self.front = None

    # def __str__(self):
    #     return '%s' % self.items

    def is_empty(self):
        return self.items == []
        
    def push_front(self, item):
        if self.size_chank() < self.n:
            self.items.append(item)
        elif self.front:
            self.front.push_front(item)
        else:
            self.front = Deque()
            self.front.push_front(item)
            self.front.back = self

    def pop_front(self):
        chank = self.get_first_front()
        if chank.is_empty():
            return -1
        pop_item = chank.items.pop()
        if chank.is_empty() and chank.back:
            chank.back.front = None
            del chank
        return pop_item

    def push_back(self, item):
        if self.size_chank() < self.n:
            self.items.insert(0, item)
        elif self.back:
            self.back.push_back(item)
        else:
            self.back = Deque()
            self.back.push_back(item)
            self.back.front = self

    def pop_back(self):
        chank = self.get_first_back()
        if chank.is_empty():
            return -1
        pop_item = chank.items.pop(0)
        if chank.is_empty() and chank.front:
            chank.front.back = None
            del chank
        return pop_item

    def size_chank(self):
        return len(self.items)

    def get_first_back(self):
        if self.back:
            return self.back.get_first_back()
        return self

    def get_first_front(self):
        if self.front:
            return self.front.get_first_front()
        return self

    # def print_deq(self):
    #     chank = self.get_first_back()
    #     while chank:
    #         print(chank, end='')
    #         if chank.front:
    #             print('<-->', end='')
    #         chank = chank.front
    #     print('\n')

d = Deque()
# print(d.pop_front())
# d.push_front(3)
# d.push_front(2)
# d.push_front(1)

# d.push_back(5)
# d.push_back(7)
# d.push_back(90)
# d.push_back(14)

# d.push_front(2)
# d.print_deq()

# d.pop_back()
# d.print_deq()
# d.pop_front()
# d.print_deq()
# d.pop_front()
# d.print_deq()

n = 1000000
count_cmd = int(input(''))

if count_cmd <= n:
    result = 'YES'
    for i in range(count_cmd):
        cmd, item = input().split()
        if cmd == '1':
            d.push_front(int(item))
        elif cmd == '2':
            pop_item = d.pop_front()
            if pop_item != int(item):
                result = 'NO'
        elif cmd == '3':
            d.push_back(int(item))
        elif cmd == '4':
            pop_item = d.pop_back()
            if pop_item != int(item):
                result = 'NO'

    print(result)
else:
    print('NO')