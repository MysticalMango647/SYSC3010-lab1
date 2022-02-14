# Write your code here 
from PIL import Image
import numpy as np


def person_detected(image1_file, image2_file, t1):
    image1 = Image.open(image1_file)
    image2 = Image.open(image2_file)
    #The buffer 1,2,3 and 3 code we found something from stack overflow but we integrated it into making it work for us
    #cannot find the link the the stack :( but we have to adapte it
    buffer1 = np.array(image1.convert('RGB')).ravel()
    buffer2 = np.asarray(image2.convert('RGB')).ravel()
    buffer3 = np.sum(np.abs(np.subtract(buffer1, buffer2, dtype=np.float))) / buffer1.shape[0]

    print(buffer3)

    if(buffer3 > t1):
        personThereStatus = True
    else:
        personThereStatus = False
    return personThereStatus