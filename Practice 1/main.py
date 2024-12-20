import threading
from typing import List

def arr_sum(arr: List[int], results, ind):
    print(f'start thread {threading.current_thread().name}')
    results[ind] = sum(arr)
    print(f'end thread {threading.current_thread().name}')

if __name__ == '__main__':
    array = [i for i in range(100)]
    t = [None] * 4
    results = [None] * 4
    total_sum = 0
    
    for i in range(4):
        t[i]=(threading.Thread(target=arr_sum, args = ([array[i*25:(i+1)*25]]),
                        kwargs={'results': results,'ind': i}, 
                        name=f'{i}'))
        t[i].start()
    for i in range(4):
        t[i].join()
    
    print(results, sum(results))