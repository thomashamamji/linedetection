# Line detection
## Why do I need this ?
I need to develop an algorithm for a drone line tracking school project.
The goal of this part of the project is to detect the nearest and biggest line of a photo.

## How will it be implemented ?
OpenCV is used to detect rectangle shapes of a photo.
Some shape filtering are processed with Numpy.
Matplotlib is used to analysis the results.

### First tests show the following results
![localImage](https://github.com/Thomas7997/linedetection/tree/main/doc/results/first.png)
    
### Results with some filtering (horizontal)
![localImage](https://github.com/Thomas7997/linedetection/tree/main/doc/results/horizontal.png)

### Results with some filtering (vertical)
![localImage](https://github.com/Thomas7997/linedetection/tree/main/doc/results/vertical.png)
