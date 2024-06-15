# Line detection  
I need to develop an algorithm for a drone line tracking school project.  
The goal of this part of the project is to detect the nearest and biggest line of a photo.  

## Used libraries  
OpenCV is used to detect line shapes of a photo.  
Some shape filtering are processed with Numpy.  
Matplotlib is used to analyse the results.  

# Example of a line detection  

Filtering criterias have been defined to make line detection more reliable.  
Instead of switching lines frequently during the same flight, the algorithm analyses the green lines accurately and chooses the red one as the right line to track based on the chosen criteria.  

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

### Configuration

```json
{
    "names" : {
        "LINES" : 0,
        "FILTERED_LINES" : 1,
        "LONG_LINES" : 2
    },
    "values" : [
        "lines",
        "filtered_lines",
        "long_lines"
    ],
    "criterias" : {
        "MIN_LENGTH" : 250,
        "MAX_VERTICAL_POSITION" : 200,
        "MAX_CENTER_DISTANCE" : 150,
        "MIN_ANGLE" : 1
    },
    "filters" : {
        "LENGTH" : 0,
        "FORWARD" : 1,
        "BOTTOM" : 2
    }
}
```

<strong>MIN_LENGTH</strong> is the minimum length of the line to be detected.  
<strong>MAX_VERTICAL_POSITION</strong> corresponds to the maximum position the bottom end of the line can appear.  
<strong>MAX_CENTER_POSITION</strong> defines distance that separates the line from the center.  

## How to use ?
```bash
  pip install -r requirements.txt
  bash init.sh
  python3 detection.py
```
