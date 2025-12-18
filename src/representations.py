import numpy as np
from scipy.ndimage import sobel

def raw_representation(img):
    return img.flatten()

def edge_representation(img):
    gx = sobel(img, axis=0)
    gy = sobel(img, axis=1)
    mag = np.sqrt(gx**2 + gy**2)
    mag = mag / (mag.mean() + 1e-6)  # local contrast normalization
    return mag.flatten()
