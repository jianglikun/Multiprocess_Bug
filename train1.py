import multiprocessing
import time
import os,sys
import traceback

threadsNum = 5


def fun(a):
    if not os.path.exists('/xxxx/xxxx'): #测试一个不存在的文件
        raise Exception("File does not exist")

def analysisPipeline(par1):
    try:
       fun(par1)
    except:
       traceback.print_exc()
       sys.exit(1)


paraList = []
paraList.append([1])
paraList.append([3])
paraList.append([2])
print('start multiprocessing')
pool = multiprocessing.Pool(threadsNum)
pool.starmap(analysisPipeline, paraList)
pool.close()
pool.join()
print('end')
