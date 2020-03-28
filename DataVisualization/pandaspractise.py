import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html

ts = pd.Series(np.random.randn(1000),index=pd.date_range('1/1/2000', periods=1000))
# ts = ts.cumsum()
# ts.plot()
# plt.show()


df = pd.DataFrame(np.random.randn(1000, 4),index=ts.index, columns=list('ABCD'))
df = df.cumsum()
plt.figure()
df.plot()

plt.show()