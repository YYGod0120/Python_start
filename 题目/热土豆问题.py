from 包.Queue1 import Queue
def hotPotato(names,num):
    names_queue = Queue()
    for name in names:   #导入名字到队列中
        names_queue.enqueue(name)


    while names_queue.size() > 1:  #测队列长度
        for i in range(num):
            names_queue.enqueue(names_queue.dequeue())  #从队首排到队尾
        names_queue.dequeue()  #删除队首

    return names_queue.dequeue()

print(hotPotato(['bill','jahn','yww','lwx','night'],4))