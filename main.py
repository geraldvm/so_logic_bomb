import psutil

#print(psutil.pids())
#print(psutil.test())
#print(psutil.cpu_percent(interval=10))
#print(psutil.cpu_count())
#print(psutil.cpu_stats())
"""
for x in range(3):
    print(psutil.cpu_percent(interval=10, percpu=True))



    p.cpu_percent() / psutil.cpu_count()"""

p = psutil.Process()
pids=psutil.pids()
for x in pids:
    p = psutil.Process(x)
    percentage=p.cpu_percent(interval=10)
    if(percentage>0):
        print(percentage)
    


    """
#print(p)
with p.oneshot():
    p.name()  # execute internal routine once collecting multiple info
    p.cpu_times()  # return cached value
    print(p.cpu_percent())  # return cached value
    p.create_time()  # return cached value
    p.ppid()  # return cached value
    p.status()  # return cached value

    """