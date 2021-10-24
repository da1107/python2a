import sys
import time

FILENAME = "eng_vocab.txt"
#FILENAME = "dogcat.txt"

class MyFileContextManager():
    def __init__(self,filename,operation):
        try:
            self._file=open(filename,operation)
        except:
            print('File not found')
            sys.exit()   

    def __enter__(self):
        return self._file

    def __exit__(self,type,value,traceback):
        self._file.close()

def timer_decorator(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        time_elapsed = end-start
        print(f'Execution time: {time_elapsed: .7f} seconds ({func.__name__})')
        return result
    return wrapper

@timer_decorator
def read_list(file):
    return file.read().splitlines()

def my_generator(file):
    for line in file:
        yield line.strip()

@timer_decorator
def read_generator(generator):
    for item in generator:
        pass


def main():
    with MyFileContextManager(FILENAME,"r") as f:
        text_list = read_list(f)
        print(sys.getsizeof(text_list), "Bytes are used by the list")

    with MyFileContextManager(FILENAME,"r") as f:
        gen = my_generator(f)
        read_generator(gen)
        print(sys.getsizeof(read_generator), "Bytes are used by the generator")
    

if __name__ == "__main__":
    main()
