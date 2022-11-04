import cv2
import numpy as np

class Frame():
    def __getHalf(self, img):
        return cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

    def getFrame(self, CAM):
        cv2.imshow('frame', CAM)

    def get2Frame(self, left, right):
        if left.shape == right.shape:
            # Split 2 images
            height, width, channel = left.shape

            image = np.zeros((height//2, width, 3), np.uint8)

            # Top Left
            image[:, :width//2] = self.__getHalf(left)

            # Top Right
            image[:, width//2:] = self.__getHalf(right)

            cv2.imshow('frame', image)
        else:
            raise Exception("[Error] Frame dimension not match")

    def get4Frame(self, top_left, top_right, bottom_left, bottom_right):
        if top_left.shape == top_right.shape == bottom_left.shape == bottom_right.shape:
            # Split 4 images
            height, width, channel = top_left.shape

            image = np.zeros((height, width, 3), np.uint8)

            # Top Left
            image[:height//2, :width//2] = self.__getHalf(top_left)

            # Bottom Left
            image[height//2:, :width//2] = self.__getHalf(bottom_left)

            # Top Right
            image[:height//2, width//2:] = self.__getHalf(top_right)

            # Bottom Right
            image[height//2:, width//2:] = self.__getHalf(bottom_right)

            cv2.imshow('frame', image)
        else:
            raise Exception("[Error] Frame dimension not match")
