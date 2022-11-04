import numpy as np
import cv2


class Detector:
    def __init__(self):
        # Settings
        self.FONT_SIZE = 2
        self.COLOR = (60, 76, 231)
        self.CONTOURS_COLOR = (15, 196, 241)
        self.THICKNESS = 20
        self.TEXT_THICKNESS = 5
        self.TEXT_COLOR = (241, 240, 236)
        self.THRESHOLD = 0.012

    def __drawBoudingBox(self, img, contour):
        cnt_x, cnt_y, cnt_w, cnt_h = cv2.boundingRect(contour)
        cv2.rectangle(img, (cnt_x, cnt_y), (cnt_x + cnt_w,
                                            cnt_y + cnt_h), self.COLOR, self.THICKNESS)

    def __drawContour(self, img, M, area, contour, shape):
        x = int(M['m10'] / M['m00'])
        y = int(M['m01'] / M['m00'])

        cv2.drawContours(img, [contour], 0,
                         self.CONTOURS_COLOR, self.THICKNESS)
        cv2.putText(img, f'{shape} {area}', (x, y), cv2.FONT_HERSHEY_SIMPLEX,
                    self.FONT_SIZE, self.TEXT_COLOR, self.TEXT_THICKNESS)

    def getShape(self, img):
        # Gaussian Blur
        blur = cv2.GaussianBlur(img, (25, 55), 0)

        # Canny Edge Detection
        canny = cv2.Canny(img, 30, 60, 3)

        # converting image into grayscale image
        gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

        # setting threshold of gray image
        _, threshold = cv2.threshold(gray, 134, 255, cv2.THRESH_BINARY)

        # using a findContours() function
        contours, _ = cv2.findContours(
            threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        gray_rgb = cv2.cvtColor(threshold, cv2.COLOR_GRAY2RGB)
        canny_rgb = cv2.cvtColor(canny, cv2.COLOR_GRAY2RGB)

        i = 0

        # list for storing names of shapes
        for contour in contours:

            # here we are ignoring first counter because
            # findcontour function detects whole image as shape
            if i == 0:
                i = 1
                continue

            # cv2.approxPloyDP() function to approximate the shape
            approx = cv2.approxPolyDP(
                contour, self.THRESHOLD * cv2.arcLength(contour, True), True)

            # using drawContours() function

            area = cv2.contourArea(approx)

            if area > 1000:
                # finding center point of shape
                M = cv2.moments(contour)
                if M['m00'] != 0.0:
                    x = int(M['m10'] / M['m00'])
                    y = int(M['m01'] / M['m00'])

                    # putting shape name at center of each shape
                    if len(approx) == 3:
                        # Draw bouding box
                        self.__drawBoudingBox(img, contour)
                        # Draw Contour
                        self.__drawContour(img, M, area, contour, 'Triangle')
                    elif len(approx) == 4:
                        # Draw bouding box
                        self.__drawBoudingBox(img, contour)
                        # Draw Contour
                        self.__drawContour(img, M, area, contour, 'Quadrilateral')
                    elif len(approx) == 5:
                        # Draw bouding box
                        self.__drawBoudingBox(img, contour)
                        # Draw Contour
                        self.__drawContour(img, M, area, contour, 'Pentagon')
                    elif len(approx) == 6:
                        # Draw bouding box
                        self.__drawBoudingBox(img, contour)
                        # Draw Contour
                        self.__drawContour(img, M, area, contour, 'Hexagon')
                    # else:
                    #    cv2.putText(img, 'circle', (x, y),cv2.FONT_HERSHEY_SIMPLEX, FONT_SIZE, COLOR, 2)

        return img, gray_rgb, blur, canny_rgb
