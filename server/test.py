#! /usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import base64
from PIL import Image
import numpy as np
import io
def main():
    video_capture = cv2.VideoCapture(0)
    w = int(video_capture.get(3))
    h = int(video_capture.get(4))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('output2.mp4', fourcc, 30, (w, h))
    i = 0
    while True:
        ret, frame = video_capture.read()  # frame shape 640*480*3
        if ret != True:
            break;
        if i % 5 == 0:
            out.write(frame)
        
        if i % 5 == 0:
            r, buf = cv2.imencode(".jpg",frame)
            print(r)
            #cv2.imwrite("./tmp.jpg",frame)
            if r != True:
                break;
            bytes_img = Image.fromarray(np.uint8(buf)).tobytes()
            print(len(bytes_img))
            if i == 0:
                cv2.imwrite("./tmp.jpg",frame)
        i+=1

if __name__ == '__main__':
    main()