import datetime

def default_timer(func):
    def int_time(*args, **kwargs):
        start_time = datetime.datetime.now()  # 程序开始时间
        func()
        over_time = datetime.datetime.now()  # 程序结束时间
        total_time = (over_time - start_time).total_seconds()
        print('Program total %s seconds' % total_time)

    return int_time

from utils import default_timer

@default_timer
def main():
        print('>>>>Starting time')
        for i in range(1000):  # 可以是任意函数  ， 这里故意模拟函数的运行时间
                for j in range(i):
                        print(j)

if __name__ == '__main__':
        main()
