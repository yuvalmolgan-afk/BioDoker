import pandas as pd
import numpy as np

df = pd.DataFrame({
    "id": range(1, 6),
    "value": np.random.randn(5)
})

df.to_csv("/data/results.csv", index=False)
print("File written to volume")