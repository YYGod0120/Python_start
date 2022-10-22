class Queue:
    def __init__(self):
        self.items = []
    #检验队列是否为零
    def isEmpty(self):
        return self.items == []
    #在队列中排上一个元素
    def enqueue(self,item):
        self.items.insert(0,item)
    #在队列中删除一个元素
    def dequeue(self):
        return self.items.pop()
    #算队列的长度
    def size(self):
        return len(self.items)

