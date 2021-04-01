import numpy as np
from math import sqrt, exp

class Classifier(object):
    def __init__(self):
        self.kBase = {}
        self.labels = []
        
    def learn(self):
        pass
    
    def classify(self, newFV):
        pass
    
    
class NaiveBayes(Classifier):
    def learn(self, label, featureVectors):
        '''
        :param str label: current category to learn
        :param arr featureVectors: matrix of k instances of n-dimensional feature vectors
        '''
        self.k = featureVectors.shape[0]
        self.n = featureVectors.shape[1]
        self.kBase[label] = {'mu': np.zeros(self.n), 'stdv': np.zeros(self.n)}
        self.labels.append(label)
        
        # mean and stdv are calculated for each feature element => column-wise in the matrix of feature vectors => loop over transposed 
        for i, col in enumerate(featureVectors.T):
            self.kBase[label]['mu'][i] = col.mean()
            self.kBase[label]['stdv'][i] = col.std()
            
        return self.kBase
    
    def printKnowledgeBase(self):
        for label in self.kBase:
            print(label)
            print('mu', self.kBase[label]['mu'])
            print('stdv', self.kBase[label]['stdv'])
        
    def _gaussianProbability(self, mu, stdv, f):
        var = stdv**2
        p1 = ((f-mu)**2) / (-2*var)
        p2 = var * sqrt(2 * np.pi)
        print(p1,p2, exp(p1) / p2)
        return exp(p1) / p2
    
    def classify(self, fv):
        numLabels = len(self.labels)
        posterior = np.ones(numLabels)  # evaluate each class then take the maximum
        for cIndex, c in enumerate(self.labels):
            for fIndex, f in enumerate(fv):
                pFiC = self._gaussianProbability(self.kBase[c]['mu'][fIndex], self.kBase[c]['stdv'][fIndex], f)
                posterior[cIndex] = posterior[cIndex] * pFiC #/ numLabels
            print('posterior of (', c, ') =', posterior[cIndex])
                
        maxPosterior = np.argmax(posterior) # returns the index
        return maxPosterior