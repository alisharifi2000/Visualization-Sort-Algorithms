import matplotlib.pyplot as plt
import numpy as np
import imageio


def SelectionSort(arr):
    n = len(arr)
    counter = 1
    BarPlot(arr, 0, 'Selection Sort Start', 0, 0)
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                text = 'elements ' + str(j) + ' and elements ' + str(i) + ' are going to swap!!'
                BarPlot(arr, counter, text, j, i)
                counter = counter + 1
                min = arr[j]
                arr[j] = arr[i]
                arr[i] = min
                text = 'elements ' + str(j) + ' and elements ' + str(i) + ' swap!!'
                BarPlot(arr, counter, text, j, i)
                counter = counter + 1
    BarPlot(arr, counter, 'Selection', 0, 0)
    counter = counter + 1
    MakeGif(n , counter)

def MakeGif(n, counter):
    images = []
    for i in range(0,counter):
        path = '\\'+str(i)+'.png'
        images.append(imageio.imread(path))
    imageio.mimsave('\\movie.gif', images, duration=n/6)


def BarPlot(arr, counter, text, x1, x2):
    color = []
    if x1 == x2:
        for k in range(0, len(arr)):
            color.append('red')
    else:
        for k in range(0, len(arr)):
            if k == x1:
                color.append('black')
            elif k == x2:
                color.append('black')
            else:
                color.append('red')

    x = np.arange(len(arr))
    plt.style.use('ggplot')
    plt.title(text)
    plt.bar(x, arr, color=color)
    plt.xlim(-1, len(arr))
    path = '\\' + str(counter) + '.png'
    plt.savefig(path)
    plt.close()


arr = [40,30,20,15,10,5]

SelectionSort(arr)

print("Sorted array is:")
print(arr)
