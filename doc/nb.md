# Naive Bayes Classifier

Bayes decision theory tries to statistically solve the problem of classiﬁcation, by assuming that the problem can be expressed in a probabilistic manner: given an image I, look for the probability to detect a category c. This is formulated as a conditional probability P(c|I). Then, among m categories, the right category would be the one that maximizes the conditional property:  
* **argmax<sub>m</sub> P(c<sub>m</sub>|I)**

However, an image is not represent by its raw data, but by an n-dimensional feature-vector f, so:
* **P(c|I) = P(c|f)**

Joint probability distribution yields that 
* **P(c, f) = P(c|f) P(f) = P(f|c) P(c)**
* => **P(c|f) = P(f|c) P(c) / P(f)**
* In English: **Posterior = likelihood * prior / evidence**

The `evidence` is a constant value that serves only as a scale factor to guarantee that posterior probabilities sum to one, whereas `prior` refers to how often each category tends to appear among other categories. So, if there is no knowledge about that in a prior, then this factor is distributed equally among all categories. Hence, both factors can be ignored for the categorization functionality, and the problem is shortened to finding P(f|c). 

By splitting f into its components:
* **P(f|c) = P(f<sub>1</sub>, .., f<sub>n</sub>|c) = P(f<sub>1</sub>|c) . P(f<sub>2</sub>,..,f<sub>n</sub>|c,f<sub>1</sub>)**

The naïve Bayes assumption assumes that the occurrence of a particular feature is conditionally independent of any other feature, so
* **P(f<sub>i</sub>|c, f<sub>j</sub>) = P(f<sub>i</sub>|c)**
* => **P(f<sub>1</sub>, .., f<sub>n</sub>|c) = P(f<sub>1</sub>|c) . P(f<sub>2</sub>|c) .. P(f<sub>n</sub>|c) = ∏ P(f<sub>i</sub>|c)**  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; _Equation(1)_

Now the problem is simplified to finding P(f<sub>i</sub>|c) of single feature elements f<sub>i</sub>. This can be solved by different ways, like discretization or distribution estimation. One of the simplest ways is to assume a Gaussian distribution, which yields:

This way, the learning algorithm is only about calculating the mean value `µ` and the standard-deviation `σ` for each class `c` and feature dimension `i`.

### Example:
Given `m` images, from which we extract 4-dimensional feature vectors, naïve Bayes classifier keeps track of 4 mean and standard-deviation values. This can be depicted as the following:

When a new image I<sub>x</sub> arrives to be classified:
1. it will be represented by its 4-dimensional feature-vector: [f<sub>x,1</sub>  f<sub>x,2</sub>  f<sub>x,3</sub>  f<sub>x,4</sub>]  
2. for i=1→4, apply µ<sub>i</sub>, σ<sub>i</sub> and f<sub>x,i</sub> in equation (2)
3. calculate the `posterior` (or effectively `likelihood`) for each class from equation (1)
4. pick the class with the max `posterior`
