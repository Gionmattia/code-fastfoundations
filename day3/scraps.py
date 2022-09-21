import math as m

def aa_something():
    a = float(input("Gimme alfa: "))
    b = float(input("Gimme beta: "))
    g = float(input("Gimme gamma: "))
    result = a**2 + b**2 - 2 * (a * b) * m.cos(g)
    result = m.sqrt(result)
    return result

import random

def mixer_twister():
    my_list = list(range(127, 349))
    random.shuffle(my_list)
    return my_list

def another():
    mlist = ["a", "b", "c"]
    for _ in range(0,10):   # Underscore is a way to create a variable that you don't need to call
        print(random.choice(mlist))
    # ANOTHER WAY TO SOLVE THIS: random.choices(list, k = number times you want to pick)

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("/home/gionmattia/Desktop/code-fastfoundations/day3/FAOSTAT_data_7-23-2022.csv")
# print(df.columns.values.tolist())
df_less = df[["Area", "Year", "Item", "Value"]]
df_cot = df_less.loc[(df_less["Area"] == "Côte d'Ivoire")]
df_ghana = df_less.loc[(df_less["Area"] != "Côte d'Ivoire")]

x_cot = df_cot.Year.values.tolist()
y_cot = df_cot.Value.values.tolist()
x_ghana = df_ghana.Year.values.tolist()
y_ghana = df_ghana.Value.values.tolist()

(m_cot, b_cot) = np.polyfit(x_cot, y_cot, 1)
(m_ghana, b_ghana) = np.polyfit(x_ghana, y_ghana, 1)
print(m_cot, b_cot)
print(m_ghana, b_ghana)

# Looks like Cot is going to surpass, sooner or later.

#if __name__ == "__main__":
    # c = aa_something()
    # c = mixer_twister()
    # another()
    #print(read_data())
    # print(c)