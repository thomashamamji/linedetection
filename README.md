# Line detection
## Why do I need this ?  
I need to develop an algorithm for a drone line tracking school project.  
The goal of this part of the project is to detect the nearest and biggest line of a photo.  

## How will it be implemented ?
OpenCV is used to detect line shapes of a photo.  
Some shape filtering are processed with Numpy.  
Matplotlib is used to analyse the results.  

# Example of a line detection
## Without filtering  
![1](https://github.com/Thomas7997/linedetection/assets/45339466/bea02402-fcaf-4c34-b0e3-fa52dd0eab67)

## After applying the LENGTH filter  
![325](https://github.com/Thomas7997/linedetection/assets/45339466/4eb8e5e5-a76b-4d17-8525-68c21775fe69)

The LENGTH filter is simply based on the distance between the lines' ends.  
The distance calculus is focused on the Y axis.  

## After applying the FORWARD filter  
![319](https://github.com/Thomas7997/linedetection/assets/45339466/930d1927-8eef-448b-8703-e5b4723b4080)

The result of the FORWARD filter is likely to be a short and straight line.  
This filter is based on the comparison of the line ends' positions on the X axis to be sure the line is not too oriented.  
