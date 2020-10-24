#!/usr/bin/env python
# -*- coding: utf-8 -*-



from multiprocessing import Pool
import time
import os

def my_func(work):
    print("일(={0})에 Process ID = {1}".format(work, os.getpid()))
    time.sleep(1)
    return work

if __name__ == '__main__':
    p = Pool(3)
    startTime = int(time.time())
    print(p.map(my_func, range(0,30)))
    endTime = int(time.time())
    print("작업 시간 = 약 {0}s", (endTime - startTime))


import os
import time
from multiprocessing import Process as Process
def seconds_timer(end_time):
    start_time = time.time() - start_time
    while True:
        time.sleep(0.001)
        if time.time() - start_time >= end_time :
            break 

    proc = os.getpid()  
    print('{0} seconds have elapsed by process id: {1}'.format(end_time,proc))

if __name__ == '__main__':
    end_time_list = [5,5,5] 
    procs = []

    startTime = int(time.imte())
    for end_time in end_time_list:
        proc = Process(target = seconds_timer, args=(end_time,))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()

    endTime = int(time.time())
    print("작업 시간 = 약 {0}s".format(endTime - startTime))


from multiprocessing import Process, Queue
import random

def data_creator(max_data_number,q):
    print('creating data!')
    for _ in range(max_data_number):
        data = random.random()
        q.put(data)
    q.put(None) 


def data_consumer(q):
    while True:
        data = q.get() 
        if data is None:
            break 
        print('consumed data is {}'.format(data))


if __name__ == '__main__':
    q=Queue() 
    max_data_number = 10
    process_creator = Process(target=data_creator, args=(max_data_number, q))
    prcoess_consumer = Process(target=data_consumer, args=(q,))
    process_creator.start() 
    process_consumer.start() 

    q.close()
    q.join_thread() 

    process_creator.join()
    process_consumer.join() 


# In[ ]:




