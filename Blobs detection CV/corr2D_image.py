import numpy as np
import matplotlib.pyplot as plt



def corr2d_mat(image_1, image_2):
    def mean_x(x):
        y = np.sum(x) / np.size(x)
        return y

    def std_x(x, x_mean):
        y = np.sqrt(np.sum((x - x_mean) ** 2) / np.size(x))
        return y

    try:
        # convert data-type to "float"
        im_float_1 = image_1.astype('float')
        im_float_2 = image_2.astype('float')
    except:
        print("Put images in, please")
        return None

    n_pixels = im_float_1.shape[0] * im_float_1.shape[1]

    # Compute mean and standard deviation of both images
    im1_mean = mean_x(im_float_1)
    im1_std = std_x(im_float_1, im1_mean)
    im2_mean = mean_x(im_float_2)
    im2_std = std_x(im_float_2, im2_mean)

    # Compute covariance and correlation coefficient
    covar = ((im_float_1 - im1_mean).T).dot(im_float_2 - im2_mean) / n_pixels
    correl = covar / (im1_std * im2_std)

    plt.figure(figsize=(16, 9))
    plt.axis("off")
    plt.imshow(correl)
    name = 'corr.png'
    plt.savefig(name, format='png')
    plt.title(name)
    plt.show()
    print("File saved "+name)
    return name
