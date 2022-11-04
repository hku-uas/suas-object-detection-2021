# HKU UAS Object Detection 2021

---

This script is used to detect shape and classify shape using the edge detection.

[![ezgif.com-gif-maker2b1cc5a5dbbb6df2b.gif](https://s10.gifyu.com/images/ezgif.com-gif-maker2b1cc5a5dbbb6df2b.gif)](https://gifyu.com/image/SzmFM)

## Run demo

There are 2 demo programs, `src/demo.py` opens a window that shows your live webcam view. `src/demo2.py` takes in a
video file
(compatible with opencv2).

To try out `src/demo.py`, follow the steps below.

1. Install the required packages by `pip install .`
2. Run `python src/demo.py`

Tip: Press `Q` to close the window.

## API Usage (Deprecated)

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