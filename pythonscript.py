import pandas as pd

data = pd.read_csv('/path/to/input.csv')
data.to_csv('/path/to/output.csv', index=False)
