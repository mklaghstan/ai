# Little thoughts in Artificial Intelligence and Machine Learning
## Suppervised image classification
This is a simplified version of a broader classification system that was presented as my master's thesis at the TU Berlin in 2011, and later published as a scientific paper at [IEEE IPTA 2012](https://ieeexplore.ieee.org/abstract/document/6469543).

The workflow is as the following:
1. Learn  
    1. read sample images from the root directory, which contains sub-directories referring to given classes (labels). e.g. root -> ./beach, ./forest, ./desert
    2. build a dictionary of images, each with its corresponding label
    3. Feature extraction:
        1. For simplicity, only a color histogram is extracted
        2. More features are *To-Do*
    3. *To-Do* Dimensionality reduction with PCA
    4. Machine learning:
        1. Naive Bayes ([documented here](doc/nb.md))
        2. *To-Do* K-NN
2. Test
    1. read test images, whose names refer to the correct label
    2. extract features
    3. feed them to the ML class
    4. fetch the result and integrate it into a confusion materix
