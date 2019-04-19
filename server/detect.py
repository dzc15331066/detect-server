#! /usr/bin/env python
# -*- coding: utf-8 -*-

import io
import cv2
import numpy as np
from PIL import Image
from yolo import YOLO
from tools import generate_detections as gdet
import sys
sys.path.append('..')

from example.ttypes import FeaturesResult

class FeaturesHandler(object):
    def __init__(self):
        self.model_filename = 'model_data/mars-small128.pb'
        self.encoder = gdet.create_box_encoder(self.model_filename,batch_size=1)
        self.yolo = YOLO()
    def get_features(self, jpg_img):
        #receive jpg image and transfer to frame
        #print("get")
        bs = io.BytesIO(jpg_img)
        frame = Image.open(bs)
        frame = cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)
        image = Image.fromarray(frame)
        #print(image.size)
        #print(frame.shape)
        boxes = self.yolo.detect_image(image)
        features = self.encoder(frame,boxes)
        if len(boxes)!=len(features):
	   print("error")
        boxes = np.int32(np.array(boxes))
        features = np.array(features)
        print(boxes.shape,features.shape)
        print(type(boxes[0][0]))
        #print(type(features[0][1]))
        return FeaturesResult(features.tobytes(),boxes.tobytes())

