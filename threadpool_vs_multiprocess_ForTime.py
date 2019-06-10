import threadpool
import multiprocessing
import time
import os,sys
import traceback

threadsNum = 5


def fun1(num):
	sum_num = 0
	for i in range(num):
		sum_num += i
	print(sum_num)


paraList = [[10000000],[10000000],[10000000]]
print('start multiprocessing')
time1 = time.time()
pool = multiprocessing.Pool(threadsNum)
pool.starmap(fun1, paraList)
pool.close()
pool.join()
time2 = time.time()
print(time2-time1)
print('end')


paraList = []
paraList.append(([10000000], None))
paraList.append(([10000000], None))
paraList.append(([10000000], None))
print('start threadpool')
time3=time.time()
pool = threadpool.ThreadPool(threadsNum)
requests = threadpool.makeRequests(fun1, paraList)
[pool.putRequest(req) for req in requests]
pool.wait()
time4=time.time()
print(time4-time3)
print('end')

	


