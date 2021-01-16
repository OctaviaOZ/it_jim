'''Task 2. Here [https://drive.google.com/drive/folders/1_FTA5l8LNon03NDz4VsNUFu9QdFcsYmH] you can find a set of 
images with blobs (binary large objects) represented by black spots. Please make a function that detects (finds xmin, xmax, ymin, ymax of) black spots on these images. This function should also visualize results by surrounding each spot (blob) with a red rectangle. The input of the function is the path to the folder with images. 
The first output is a list of dicts like this: [{'file': SR1.png, 'coords': [left,right,top,bottom]}, ...] 
Second output: *.png files with a visualization of results.'''

import os
import cv2
import numpy as np

def detect_object(IMAGE_PATH):
    files = os.listdir(IMAGE_PATH)
    len_files = len(files)
    
    if not len_files:
        return [], []
    
    images1 = []
    im1_append = images1.append
    images2 = []
    im2_append = images2.append
    
    for image in files:
        # Blue color in BGR
        color = (0, 0, 255)
        
        img = cv2.imread(IMAGE_PATH+image, 0)
        # Tozero thresholding 
        _, th = cv2.threshold(img, 200, 255, cv2.THRESH_TOZERO)
        # find connected components
        connectivity = 4
        nb_components, _, stats, _ = \
        cv2.connectedComponentsWithStats(th, connectivity, ltype=cv2.CV_32S)

        for i in range(0, nb_components-1):
            name_image = os.path.basename(image).split('.')[0] 
            
            # draw the bounding rectangele around each object
            left_top = (stats[i][0], stats[i][1])
            right_bottom = (stats[i][0]+stats[i][2],stats[i][1]+stats[i][3])
            cv2.rectangle(img, left_top, right_bottom, color, 1)
            cv2.imwrite(name_image+'_box.png', img)
            im2_append(name_image+'_box.png')
                 
            right_top = (stats[i][0]+stats[i][2], stats[i][1])
            left_bottom = (stats[i][0], stats[i][1]+stats[i][3])
            dict_image = {'file': name_image, 'coords': [left_top, right_bottom, right_top, left_bottom]}
            im1_append(dict_image)
        
    if not len(images2)%3:
        for i in range(0, len(images2), 3):
            img1 = cv2.imread(images2[i])
            img2 = cv2.imread(images2[i+1])
            img3 = cv2.imread(images2[i+2])
            w, h, s = img1.shape
            img2 = cv2.resize(img2, (h, w)) # default INTER_LINEAR
            img3 = cv2.resize(img3, (h, w)) # default INTER_LINEAR

            concat_images = np.hstack((img1, img2, img3))
            cv2.imshow(images2[i]+" "+images2[i+1]+" "+images2[i+2], concat_images) 
            cv2.namedWindow(images2[i]+" "+images2[i+1]+" "+images2[i+2], cv2.WND_PROP_VISIBLE)
    else: 
        for i in range(len(images2)):
            img1 = cv2.imread(images2[i])
            cv2.imshow(images2[i], img1) 
            cv2.namedWindow(images2[i], cv2.WND_PROP_VISIBLE)
                    
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
    return images1, images2 
