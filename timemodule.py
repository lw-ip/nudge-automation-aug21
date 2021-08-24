import time

def current_time():
    time_time = time.localtime()
    current_time = time.strftime("%d/%m/%Y-%H:%M:%S", time_time)
    return current_time


def print_time():
    time_time = time.localtime()
    print_time = time.strftime("%Y%m%d_%H%M%S", time_time)
    return print_time