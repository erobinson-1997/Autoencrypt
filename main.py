# Created by Ethan Robinson
# Started November 17th, 2023

import sys
import os
from services import password_processor
from services import image_processor
from models import ConvolutionalG

if __name__ == "__main__":
    # TODO: add error checking 
    password = sys.argv[1]
    image_file_path = sys.argv[2]

    print("pwd:", password)
    print("img:", os.path.basename(image_file_path))

    preprocessed_pwd = password_processor.password_processor(password).__call__()
    print("pre-processed:", preprocessed_pwd.shape)

    preprocessed_img = image_processor.image_processor(image_file_path).__call__()
    print("pre-processed img:", preprocessed_img.shape)

    img_width = preprocessed_img.shape[0]
    img_height = preprocessed_img.shape[1]
    
    # get dimensions from input image to pass to ConvG

    


