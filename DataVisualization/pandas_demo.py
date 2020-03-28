import pandas as pd
import numpy as np

print(pd.Series(np.intersect1d(pd.Series([1,2,3,5,42]).values, pd.Series([1,4,5,6,20,42]).values)))