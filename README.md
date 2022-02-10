# HKU-UAS-object-detection
This script is used to detect shape and classify shape using the edge detection.


**Quick Start:**
1. Initialize a python virtual environment by `pipenv shell`
2. Install the package by `pip install .`
3. Write your code or test the library by `python demo.py`


**Usage**
```
# Import the Package
from ObjectDetector.detector import *
from ObjectDetector.frame import *
```

**ObjectDetector.detector**
```
detector.getShape(frame)

Args:
    frame (np.array): The input image

Returns:
    frame (np.array): The output image with annotation
    
```

**ObjectDetector.frame**
You can use this object to display a frame of 1,2,4 screen(s) at the same time

```
getFrame(frame)
get2Frame(left_frame,right_frame)
get4Frame(top_left, top_right, bottom_left, bottom_right)
```

**Demo**
Please see the `demo.py` and `demo2.py` file.
```
from ObjectDetector.detector import *
from ObjectDetector.frame import *

import cv2

def runDemo(CAM):
    # Get Webcam
    cap = cv2.VideoCapture(CAM)

    # Initialize Viewer
    screen = Frame()
    detector = Detector()

    while True:
        try:
            ret, frame = cap.read()

            img, gray_rgb, blur, canny_rgb = detector.getShape(frame)
            screen.get4Frame(img,gray_rgb,blur,canny_rgb)

            if cv2.waitKey(1) == ord('q'):
                break
        except Exception as msg:
            print(msg)
            break

if __name__ == "__main__":
    # Run it on your webcam
    runDemo(0)
    # Run the detection on some video file
    # runDemo('video/triangle.MOV')
```

**Requirements**
```
numpy==1.22.2
opencv-python==4.5.5.62
```

# Contents
```
.
├── Pipfile
├── README.md
├── demo.py
├── demo2.py
├── requirements.txt
├── setup.py
├── src
│   ├── ObjectDetector
│   │   ├── __init__.py
│   │   ├── detector.py
│   │   ├── frame.py
│   │   └── utils
│   │       └── __init__.py
│   └── hkuuas_object_detection.egg-info
│       ├── PKG-INFO
│       ├── SOURCES.txt
│       ├── dependency_links.txt
│       ├── not-zip-safe
│       ├── requires.txt
│       └── top_level.txt
├── tests
│   └── test.py
└── video
    ├── circle.MOV
    ├── cross.MOV
    ├── hexagon.MOV
    ├── octagon.MOV
    ├── pentagon.MOV
    ├── quad-circle.MOV
    ├── rectangle.MOV
    ├── semi-circle.MOV
    ├── square.MOV
    ├── trapezoid.MOV
    └── triangle.MOV
```