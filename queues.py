# -*- coding: utf-8 -*-
# @Date    : 2022-07-24 10:43:10
# @Author  : DENCODER (hetcjoshi1684@gmail.com)
# @GitHub    : (https://github.com/D-ENCODER)
# @Twitter    : (https://twitter.com/Hetjoshi1684)
# @Version : 1.0.0

from queue import Queue
q = Queue(maxsize=3)
print(q.qsize())
q.put('a')
q.put('b')
q.put('c')
print("Full: ", q.full())
print("Elements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())
print("Empty: ", q.empty())
q.put(1)
print("Empty: ", q.empty())
print("Full: ", q.full())
