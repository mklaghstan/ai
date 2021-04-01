from PIL import Image
import numpy as np

class ImageFeature():
    def __init__(self, imgFile):
        self.img = Image.open(imgFile)
        print('processing image:', imgFile)
        
    def histogram(self, size):
        # change the image from RGB to index
        imgIndex = self.img.quantize(size)
        #imgIndex.show()
        featureVector = np.ones(size) 
        data = np.asarray(imgIndex)
        for row in data:
            for color in row:
                featureVector[color] = featureVector[color] + 1
                
        #featureVector = featureVector / (256*256) # normalize
        return featureVector