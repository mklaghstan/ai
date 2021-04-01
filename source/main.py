
import imageUtil
import ImageFeature
import Classifier
import numpy as np

nb = Classifier.NaiveBayes()
histogramBins = 256
    
imgDict = imageUtil.fetchFilesAndLabels('C:/Users/d064443/Documents/MA/IC_images/learn/outdoor/nature')
for label in imgDict.keys():
    print('building feature vectors for:', label)
    numInstances = len(imgDict[label]) 
    fv = np.empty((0, histogramBins), float) # 0 rows, 8 columns
    for i, img in enumerate(imgDict[label]):
        imgFeature = ImageFeature.ImageFeature(img)
        his = imgFeature.histogram(histogramBins)
        fv = np.append(fv, [his], axis=0)
    nb.learn(label, fv)
#nb.printKnowledgeBase()

numLabels = len(imgDict.keys())
confusionMatrix = np.zeros((numLabels, numLabels), int)

imgDictTest = imageUtil.fetchFilesAndLabels('C:/Users/d064443/Documents/MA/IC_images/test', False)
for i, imgTest in enumerate(imgDictTest['test']):
    actualLabelIndex = imageUtil.getLabelFromFilename(imgDict.keys(), imgTest)
    imgFeatureTest = ImageFeature.ImageFeature(imgTest)
    fv = imgFeatureTest.histogram(histogramBins)
    predictedLabelIndex = nb.classify(fv)
    confusionMatrix[actualLabelIndex][predictedLabelIndex] = confusionMatrix[actualLabelIndex][predictedLabelIndex] + 1

print(confusionMatrix)