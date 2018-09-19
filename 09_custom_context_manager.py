# f = open('ticker_data.csv')
# data = f.read()
# f.close()

# import threading 
# lock = threading.Lock()
# lock.acquire()
# print('Use the lock')
# lock.release()

# with open('ticker_data.csv') ass f:
#     data = f.read()

# Helpful for resourcing programming to open/close connection 

class Manager(object):
    def __enter__(self):
        print('Entering')
        return 'some value'
    
    def __exit__(self, ty, val, tb):
        print('Exiting')
        print(ty, val, tb)


with m as val:
    print('val') = ',val'

with m as 