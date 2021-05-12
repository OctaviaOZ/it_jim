import os
import cv2
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.max_open_warning': 0})


def detect_object(image_path):
    files = os.listdir(image_path)
    len_files = len(files)

    if not len_files:
        return [], []

    images1 = []
    im1_append = images1.append
    images2 = []
    im2_append = images2.append

    # red color in BGR
    color = (255, 0, 0)

    for image in files:

        # gray image
        img = cv2.imread(image_path + image, 0)

        # image to draw rectangle
        grayBGR = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        # Tozero thresholding
        _, th = cv2.threshold(img, 177, 255, cv2.THRESH_TOZERO)
        # find connected components
        connectivity = 4
        nb_components, _, stats, _ = \
            cv2.connectedComponentsWithStats(th, connectivity, ltype=cv2.CV_32S)

        for i in range(0, nb_components - 1):
            name_image = image.split('.')[0]

            # draw the bounding rectangele around each object
            left_top = (stats[i][0], stats[i][1])
            right_bottom = (stats[i][0] + stats[i][2], stats[i][1] + stats[i][3])
            cv2.rectangle(grayBGR, left_top, right_bottom, color, 1)
            plt.figure(figsize=(16, 9))
            plt.axis("off")
            plt.imshow(grayBGR)
            plt.savefig(name_image + '_b.png', format='png')
            plt.title(name_image + '_b.png')
            im2_append(name_image + '_b.png')

            right_top = (stats[i][0] + stats[i][2], stats[i][1])
            left_bottom = (stats[i][0], stats[i][1] + stats[i][3])
            dict_image = {'file': name_image, 'coords': [left_top, right_bottom, right_top, left_bottom]}
            im1_append(dict_image)

    plt.show()
    return images1, images2
