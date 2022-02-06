import time

mylist = [1]
for k in mylist:
    mylist.append(1)
    print(len(mylist))
    time.sleep(10)
