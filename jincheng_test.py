from multiprocessing import Pool

import os

import time


def test(name):
    print("进程启动了{}{}".format(name,os.getpgid()))
    time.sleep(5)
    print("进程结束了{}{}".format(name,os.getpgid()))


if __name__ == '__main__':
    p = Pool(3)
    for i in range(3):
        p.apply_async(test,args=(i,))
    p.close()
    p.join()
