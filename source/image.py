import cv2
import os
from source.model_detection import object_detection
os.environ['PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION'] = 'python'

def image_source(image:str):
    try:
        image = cv2.imread(image)

        image = object_detection(image)

        cv2.imshow("image", image)
        cv2.waitKey(0)
    except Exception as e:
        raise Exception("Images Error")