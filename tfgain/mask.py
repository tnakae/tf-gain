import numpy as np
import pandas as pd

class MissingMask(object):
    """Class indicating positions of missing value.
    """
    def __init__(self, m):
        """
        Parameters
        ----------
        m : array like (2d array of np.bool)
            missing flags (if True, observed)
        """
        self.m = np.array(m)

    def inject(self, x):
        """inject missing value into data frame based on mask.

        Parameters
        ----------
        x : pd.DataFrame
            target data frame

        Returns
        -------
        y : pd.DataFrame
            data frame into which missing values were injected.
        """
        y = x.where(self.m, np.nan)
        return y

    def fill(self, x):
        """fill missing cell of input data frame by zero value.

        Parameters
        ----------
        x : pd.DataFrame
            target data frame

        Returns
        -------
        y : pd.DataFrame
            data frame into which missing values were filled by zeros.
        """
        y = x.where(self.m, 0)
        return y

    @staticmethod
    def extract(x):
        """Extract mask from data frame with missing values

        Parameters
        ----------
        x : pd.DataFrame
            target data frame

        Returns
        -------
        mask : MissingMask
            mask object extracted
        """
        m = ~np.isnan(x)
        mask = MissingMask(m)
        return mask

    @staticmethod
    def generate(x, rate):
        """Generate random mask with same size as x

        x : pd.DataFrame
            data frame based on which mask object is generate
        rate : float
            missing rate (0-1)
        """
        z = np.random.uniform(size=x.shape)
        m = rate < z
        mask = MissingMask(m)
        return mask
