import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

data2 = []
for i in range(len(lst)):
    if lst[i] == 'human':
        human = 1
        robot = 0
        
    elif lst[i] == 'robot':
        human = 0
        robot = 1
        
    data2 +=[{"human": human, "robot": robot}]
df = pd.DataFrame(data2)
print(df)