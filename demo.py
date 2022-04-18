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
            # screen.get4Frame(img,gray_rgb,blur,canny_rgb)
            screen.getFrame(img)

            if cv2.waitKey(1) == ord('q'):
                break
        except Exception as msg:
            print(msg)
            break

if __name__ == "__main__":
    # Run it on your webcam
    runDemo('rtsp://admin:1qaz!QAZ@192.168.1.64')
    # Run the detection on some video file
    # runDemo('video/triangle.MOV')