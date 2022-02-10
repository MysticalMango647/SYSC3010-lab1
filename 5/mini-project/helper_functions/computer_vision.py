# Write your code here :-)
from PIL import Image
#python3 -m pip install --upgrade pip
#python3 -m pip install --upgrade Pillow
import numpy as np

def person_detected(image1_file, image2_file, t1):
    personThereStatus = false

    image1 = Image.open(image1_file);
    image2 = Image.open(image2_file);
    buffer1 = np.asarray(image1);
    buffer2 = np.asarray(image2);
    buffer3 = buffer1 - buffer2;
    differenceImage = Image.fromarray(buffer3);

    return personThereStatus


