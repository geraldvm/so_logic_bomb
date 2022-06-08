import psutil
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('_mpl-gallery')


def plotPieCPU():
    labels = 'CPU Usage', 'Free'
    usage = psutil.cpu_percent(interval=10, percpu=False)
    sizes = [usage,100 - usage]
    fig1, ax1 = plt.subplots()
    explode = (0.1, 0)  # only "explode" the 1st slice (i.e. 'CPU Usage')
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.subplots_adjust(left=0.12, bottom=0.214, right=1, top=0.912, wspace=1, hspace=1)
    plt.show()

def main():
    plotPieCPU()

main()