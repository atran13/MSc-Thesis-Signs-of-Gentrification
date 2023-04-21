import os
import glob
import numpy as np
import cv2 # opencv 4.5.0 ; opencv-python 4.7.0.72
import easyocr

# Specify language to identify from images
reader = easyocr.Reader(['en','nl'], gpu = False)

# Function
def extract_text(origin, destination):
    """
    :origin: Folder with original images
    :destination: Destination folder; sub-folders will be made to contain text instances per image.
    """
    no_text = 0
    num_file = 0
    instances = 0
    for file in glob.glob(os.path.join(origin,'*.jpg')):
        num_file += 1
        filename = os.path.split(file)[1] # {name}.jpg
        dir = os.path.join(destination, filename)

        # Read img
        img = cv2.imread(file)
        
        # Detect texts
        # Output: horizontal_list, free_list
        # horizontal_list is a list of regtangular text boxes.
        # free_list is a list of free-form text boxes.
        result = reader.detect(img, add_margin=0)

        # Crop & save text regions
        if not any([result[0][0], result[1][0]]): # if no text detected
            no_text += 1
        else:
            os.makedirs(dir) # make folder for image with text
            
            # for rectangular text boxes
            for i, box in enumerate(result[0][0]):
                instances += 1
                tl = (max(0,box[0]), max(0,box[2]))
                br = (max(0,box[1]), max(0,box[3]))
                cropped_rec = img[tl[1]:br[1], tl[0]:br[0]]
                
                des_path = os.path.join(dir, f'rec-{i}.jpg')
                if cropped_rec is not None:
                    cv2.imwrite(des_path, cropped_rec)
                else:
                    pass
            
            # for free-form text boxes
            # source: https://jdhao.github.io/2019/02/23/crop_rotated_rectangle_opencv/
            for i, box in enumerate(result[1][0]):
                instances += 1
                rect = cv2.minAreaRect(np.array(box, dtype=np.int32))
                
                width = int(rect[1][0])
                height = int(rect[1][1])

                bound = cv2.boxPoints(rect) ; bound = np.int0(bound)
                src_pts = bound.astype("float32")

                if width > height:
                    dst_pts = np.array([[0, height-1],
                                        [0, 0],
                                        [width-1, 0],
                                        [width-1, height-1]],
                                        dtype="float32")
                    perspective_matrix = cv2.getPerspectiveTransform(src_pts, dst_pts)
                    cropped_poly = cv2.warpPerspective(img, perspective_matrix, (width, height))
                else:
                    dst_pts = np.array([[0, 0],
                                        [height-1, 0],
                                        [height-1, width-1],
                                        [0, width-1]],
                                        dtype="float32")
                    
                    perspective_matrix = cv2.getPerspectiveTransform(src_pts, dst_pts)
                    cropped_poly = cv2.warpPerspective(img, perspective_matrix, (height, width))
                
                des_path = os.path.join(dir, f'poly-{i}.jpg')
                if cropped_poly is not None:
                    cv2.imwrite(des_path, cropped_poly)
                else:
                    pass
    
    print(f"Number of text instances: {instances}")
    print(f"Number of images without text: {no_text} ({(100 * no_text/num_file):.2f}%)")