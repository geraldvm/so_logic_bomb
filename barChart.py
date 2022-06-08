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
    plt.subplots_adjust(left=0.12, bottom=0.214, right=1, top=0.912, wspace=1, hspace=1)
    ax.set_xlabel('CPU Time')
    ax.set_ylabel('CPU Usage')
    ax.set_yticks(np.arange(0,100,10))

    plt.show()


def main():
    x_axis, y_axis = getCPU_usage()
    plotCPU(x_axis,y_axis)

main()