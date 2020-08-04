dict1 = {"name": 123, "age": 12}
print(dict1.items())
print(dict1.values())
print(dict1.fromkeys(dict1, dict1))
# print(dict1.fromkeys(dict1,for value in dict1))
print(dict1.setdefault("sex", 1))
print(dict1)
# import numpy as np
import seaborn as sns

# import pandas as pd
iris = sns.load_dataset("iris")
print(iris.head())
g = sns.PairGrid(iris)
