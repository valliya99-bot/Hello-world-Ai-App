from sklearn.linear_model import LinearRegression

import numpy as np

## Training
def train():
    ## realtionship will follow this equation y=2x+3
    # data creation
    x=np.array([[1],[2],[3],[4],[5]]) ##2d array as sklearn expects the input to be a 2d array(n_samples, n_features)
    y=np.array([5,7,9,11,13])

    model=LinearRegression()
    model.fit(x,y)

    return model





