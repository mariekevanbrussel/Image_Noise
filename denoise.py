import cv2
import matplotlib.pyplot as plt
import numpy as np

def denoise(image, kernel_type, **kwargs):    

    if kernel_type == 'box':
        ksize = kwargs.get('ksize')
        imOu = cv2.blur(image, ksize)

    elif kernel_type == 'median':
        ksize = kwargs.get('ksize')
        imOu = cv2.medianBlur(image, ksize)
        
    elif kernel_type == 'gaussian':
        ksize = kwargs.get('ksize')
        sigma = kwargs.get('sigma')
        imOu = cv2.GaussianBlur(image, ksize, sigma)

    else:
        print('Operatio Not implemented')
        imOu=""

    return imOu

