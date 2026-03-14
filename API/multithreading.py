# Multithreading - Multithreading lets you run multiple tasks concurrently in the same program.
#                  It can be useful for tasks that are I/O-bound, such as reading from a file or fetching data from APIs.
#                  threading.Thread(target=function_name)
#                  TO START = threading.Thread(target=function_name, args=(arg1, arg2)).start()

import threading

import time

def walk_dog():
    time.sleep(8)
    print("Finished walking the dog")

def take_out_trash():
    time.sleep(2)
    print("Finished taking out the trash")

def get_mail():
    time.sleep(4)
    print("Finished getting the mail")

# Create threads for each task
chore1 = threading.Thread(target=walk_dog)
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()  

# Here all three tasks will run concurrently, and the output will be printed as each task finishes, regardless of the order they were started.

# .join() is used to wait for a thread to finish before moving on to the next line of code. 
# This ensures that the main thread will wait for all the chores to be completed before it continues executing any further code.
chore1.join()
chore2.join()
chore3.join()

print("All chores are done!")
# This will print "All chores are done!" only after all the threads have completed their tasks.

## Passing args to threads:
def greet(name, times):
    for _ in range(times):
        print(f"Hello, {name}!")
        time.sleep(1)

t = threading.Thread(target=greet, args=("Alice", 3))
t.start()
t.join()

## Thread safety with Lock: When multiple threads access shared resources, it can lead to conflicts. 
# To prevent this, you can use a Lock to ensure that only one thread can access the resource at a time.

counter = 0
lock = threading.Lock()
# In this example, we have a shared counter variable that both threads will increment.

def increment():
    global counter
    for _ in range(1000):
        with lock:        # only one thread can access this at a time
            counter += 1

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()
t1.join()
t2.join()

print(f"Counter: {counter}")  # Always 2000