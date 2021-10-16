from timeit import timeit
from simplequeue import SimpleQueue


SIZE = 10**6
TIMES = 10

def measure(function):

    time = timeit(function, number = TIMES)
    time_str = f"Execution time: {time / TIMES: .7f} seconds"
    settings = f"(SIZE: {SIZE}, TIMES: {TIMES}, {function.__name__})"
    print(time_str, settings)



def fifo_deque():
    a_queue = SimpleQueue()
    for message in range(SIZE):
        a_queue.append(message)
    for i in range(SIZE):
        a_queue.popleft()

measure (fifo_deque)
