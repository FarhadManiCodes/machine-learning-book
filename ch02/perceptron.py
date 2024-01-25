import numpy as np
from numpy._typing import NDArray
class Perceptron:
    """
    Parameters
    --------------
    eta : float
        Learning rate (between 0.0 and 1.0)
    n_iter : int
        Passes over the training dataset.
    random_state: int
        Random number generator seed for random weight initilization
    
    Attributes
    -------------
    w_ : np.array
        Weights after fitting.
    b_ : 
        Bias unit after fitting
    """
    def __init__(self, eta:float=0.01,n_itter:int=50, random_state:int=1):
        self.eta = eta
        self.n_itter = n_itter
        self.random_state = random_state
    
    def fit(self, X: NDArray, y: NDArray):
        """Fit training data

        Parameters
        -----------
        X : {array-like}, shape = [n_example, n_features]
            Training vectors, where n_example is the number of examples 
            and n_features is the is the number of features.
        y : array-like, shape = [n_example] 
            Target values.
        Returns
        --------
        self : object
        """
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=X.shape[1])
        self.b_ = np.float_(0.)
        self.errors_ = []

        for _ in range(self.n_itter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_ += update * xi
                self.b_ += update
                errors += int(update != 0,0)
            self.errors_.append(errors)
        return self

    def net_input(self, X: NDArray):
        """Calculate net input"""
        return np.dot(X, self.w_) + self.b_
    def predict(self, X: NDArray):
        """ Return class label after unit ste[ """
        return np.where(self.net_input(X) > 0.0, 1, 0)
