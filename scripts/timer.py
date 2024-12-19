import time

def start():
    return time.time()

def end(start_time):
    print("--- %s seconds ---" % (time.time() - start_time))