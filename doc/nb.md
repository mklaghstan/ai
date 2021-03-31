# Naive Bayes Classifier

Bayes decision theory tries to statistically solve the problem of classiﬁcation, by assuming that the problem can be expressed in a probabilistic manner: given an image I, look for the probability to detect a category c. This is formulated as a conditional probability P(c|I). Then, among m categories, the right category would be the one that maximizes the conditional property:  
* **argmax<sub>m</sub> P(c<sub>m</sub>|I)**

However, an image is not represent by its raw data, but by an n-dimensional feature-vector f, so:
* **P(c|I) = P(c|f)**

Joint probability distribution yields that 
* **P(c, f) = P(c|f) P(f) = P(f|c) P(c)**
* => **P(c|f) = P(f|c) P(c) / P(f)**
* In English: **Posterior = likelihood * prior / evidence**
