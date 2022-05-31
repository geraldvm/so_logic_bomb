import psutil
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('_mpl-gallery')

# make data:
def getCPU_usage():
    list_y=[]
    list_x=[]
    for x in range(5):
        list_y+=[psutil.cpu_percent(interval=10, percpu=False)]
        list_x+=[x*10]
    print(list_y)
    return list_x, list_y


def plotCPU(listX, listY):
    # plot
    fig, ax = plt.subplots()
    ax.bar(listX, listY, width=7, edgecolor="red", linewidth=0.7)
    ax.set_xlabel('CPU Time')
    ax.set_ylabel('CPU Usage')
    ax.set_yticks(np.arange(0,100,10))

    plt.show()

def plotPieCPU():
    labels = 'CPU Usage', 'Free'
    usage = psutil.cpu_percent(interval=10, percpu=False)
    sizes = [usage,100 - usage]
    fig1, ax1 = plt.subplots()
    explode = (0.1, 0)  # only "explode" the 1st slice (i.e. 'CPU Usage')
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()

def main():
    #x_axis, y_axis = getCPU_usage()
    #plotCPU(x_axis,y_axis)
    plotPieCPU()

main()