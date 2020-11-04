from myPSNR import myPSNR
from denoise import denoise
import cv2
import matplotlib.pyplot as plt

#Importing images
path_salt_pep = 'images/image1_saltpepper.jpg'
path_gauss = 'images/image1_gaussian.jpg'
path_orig = 'images/image1.jpg'
salt_pep = cv2.imread(path_salt_pep, 0) 
gauss = cv2.imread(path_gauss, 0) 
orig = cv2.imread(path_orig, 0)

#Box and Median with different kernels sizes filtering applied on Salt and Pepper noise image
kernels = [3, 5, 7]
filtering_methods = ['box', 'median']

fig1, ax = plt.subplots(len(filtering_methods), len(kernels), figsize=(30, 20))
plt.suptitle('Salt and Pepper noise', size=20)
for filter in filtering_methods:
    for kernel in kernels:
        col_index = kernels.index(kernel)
        row_index = filtering_methods.index(filter)
        k = kernel if filter=='median' else (kernel,kernel)
        ax[row_index, col_index].imshow(denoise(salt_pep, filter, ksize=k), cmap='gray')
        ax[row_index, col_index].set_title('Kernel size: ' + str(kernel) + ", Filter: " + str(filter))
        ax[row_index, col_index].axis('off')
plt.show()

#Box and Median with different kernels sizes filtering applied on Gaussion Noise image
kernels = [3, 5, 7]
filtering_methods = ['box', 'median']

fig2, ax = plt.subplots(len(filtering_methods), len(kernels), figsize=(30, 20))
plt.suptitle('Gaussian Noise', size=20)
for filter in filtering_methods:
    for kernel in kernels:
        col_index = kernels.index(kernel)
        row_index = filtering_methods.index(filter)
        k = kernel if filter=='median' else (kernel,kernel)
        ax[row_index, col_index].imshow(denoise(gauss, filter, ksize=k), cmap='gray')
        ax[row_index, col_index].set_title('Kernel size: ' + str(kernel) + ", Filter: " + str(filter))
        ax[row_index, col_index].axis('off')
plt.show()

#Guassian Filtering with different kernels sizes and sigmas applied on image with Gaussian Noise
kernels = [3,5,7,11]
sigmas = [0.5, 0.8, 1, 2, 3]

fig3, ax = plt.subplots(len(kernels), len(sigmas), figsize=(20, 30))
plt.suptitle('Gaussian Noise and Gaussian filtering', size=15)
for k in kernels:
    for sig in sigmas:
        img = denoise(gauss, 'gaussian', ksize=(k,k), sigma=sig)
        PSNR = round(myPSNR(orig, img), 2)
        
        title = 'kernel: ' + str(k) + ", sigma: " + str(sig) + ", PSNR: " + str(PSNR)
        ax[kernels.index(k), sigmas.index(sig)].imshow(img, cmap='gray')
        ax[kernels.index(k), sigmas.index(sig)].set_title(title, size=7.5)
        ax[kernels.index(k), sigmas.index(sig)].axis('off')
plt.show()
     

