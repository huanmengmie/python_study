# -*- coding:UTF-8 -*-
import math
import os

import cv2


def video_to_image():
    count = 0
    cap = cv2.VideoCapture("test.mp4")  # capturing the video from the given path
    frame_rate = cap.get(cv2.CAP_PROP_FPS)  # frame rate
    x = 1
    while cap.isOpened():
        frameId = cap.get(1)  # current frame number
        ret, frame = cap.read()
        if not ret:
            break
        if frameId % math.floor(frame_rate) == 0:
            filename = os.path.join(os.path.dirname(__file__), "img", "frame%d.jpg" % count)
            count += 1
            cv2.imwrite(filename, frame)
    cap.release()
    print("Done!")


if __name__ == '__main__':
    video_to_image()