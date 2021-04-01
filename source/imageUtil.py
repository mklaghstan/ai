import os

def fetchFilesAndLabels(path, fetchLabel=True):
    dwalk = os.walk(path)
    dict = {}
    for root, dirs, files in dwalk:
        if(len(files)==0): # no files => we have the directories referring to the labels
            dict = {k:[] for k in dirs}
            print('dictionary initialized', dict)
        else:
            label = root.split('\\')[1] if fetchLabel else 'test' 
            if not fetchLabel: # in the test case, dict is not initialized in the previous IF statement
                dict[label] = []
            for file in files:
                if file.endswith('.jpg'):
                    dict[label].append( os.path.join(root, file) )
    
    return dict

def getLabelFromFilename(labels, fname):
    for i, label in enumerate(labels):
        if fname.find(label) > 0:
            return i