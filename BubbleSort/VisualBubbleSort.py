import matplotlib.pyplot as plt
import numpy as np
import imageio

# implement Bubble Sort algorithm
def BubbleSort(arr):
    n = len(arr)
    counter = 1
    # start frame of gif
    BarPlot(arr, 0, 'Bubble Sort Start', 0, 0)
    # run bubble sort
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # make bar plot to show which elements are going to swap
                text = 'elements ' + str(j) + ' and elements ' + str(j + 1) + ' are going to swap!!'
                BarPlot(arr, counter, text, j, j+1)
                counter = counter + 1
                # make bar plot to show the swap of two elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                text = 'elements ' + str(j) + ' and elements ' + str(j + 1) + ' swap!!'
                BarPlot(arr, counter, text, j, j+1)
                counter = counter + 1
    # end frame of gif
    BarPlot(arr, counter, 'BubbleSort', 0, 0)
    counter = counter + 1
    # make gif
    MakeGif(n , counter)

# make gif with package imageio
def MakeGif(n, counter):
    images = []
    # make list of path for images of plot
    for i in range(0,counter):
        path = '\\'+str(i)+'.png'
        images.append(imageio.imread(path))
    # build gif with set the speed of it
    # you can change speed of gif by changing 'duration'
    imageio.mimsave('\\movie.gif', images, duration=n/6)

# plot barchart of array 
def BarPlot(arr, counter, text, x1, x2):
    color = []
    # make list of colors for first and last frame of gif
    if x1 == x2:
        for k in range(0, len(arr)):
            color.append('red')
    # make list of colors for other frame of gif
    else:
        for k in range(0, len(arr)):
            if k == x1:
                color.append('black')
            elif k == x2:
                color.append('black')
            else:
                color.append('red')
    # set title and color and range of x label and x label in bar plot
    x = np.arange(len(arr))
    plt.style.use('ggplot')
    plt.title(text)
    plt.bar(x, arr, color=color)
    plt.xlim(-1, len(arr))
    path = '\\' + str(counter) + '.png'
    plt.savefig(path)
    plt.close()


# run the code with sample input
arr = [40,30,20,15,10,5]

BubbleSort(arr)

print("Sorted array is:")
print(arr)
