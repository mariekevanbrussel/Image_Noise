import cv2
import numpy as np
import math

def myPSNR(orig_image, approx_image):
    
    orig_image = orig_image.astype(np.float32)
    approx_image = approx_image.astype(np.float32)
    
    m, n = orig_image.shape

    diff = orig_image - approx_image
    summ = np.sum(diff**2)
    MSE = 1 / (m * n) * summ

    I_max = np.max(orig_image)
    
    PSNR = 20 * math.log10(I_max / np.sqrt(MSE))

    return PSNR
