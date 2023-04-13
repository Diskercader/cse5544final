import pandas as pd
import numpy as np
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
from joypy import joyplot

from clean import clean

np.random.seed(42)
x = np.random.rand(1000)
y = np.random.normal(x, 0.1)
cat = ['cat1'] * 5 + ['cat2'] * 5
x2 = [1, 2, 2, 2, 1, 4, 4, 4, 5, 5]

df = pd.read_csv("../data/music.csv")
df = cleanData(df)

df2 = pd.DataFrame({'x': x, 'y': y})
df3 = pd.DataFrame({'cat': cat, 'x': x2})

container1 = st.container()

with container1:
    col1, col2 = st.columns([4500, 3000])

    with col1:
        fig, ax = joyplot(data=df3,
                          by='cat',
                          figsize=(10,4))
        st.pyplot(fig)

        fig, ax = plt.subplots()
        fig.tight_layout()
        sns.scatterplot(data=df2, x='x', y='y')
        st.pyplot(fig)
    
    with col2:
        fig, ax = plt.subplots(figsize=(5,8))
        fig.tight_layout()
        sns.violinplot(data=df2, y='y')
        st.pyplot(fig)

container2 = st.container()

with container2:
    subcol4, subcol5 = st.columns(2)

    # These 2 plots are broken as they reference
    # a column in the real data but not the Mock
    with subcol4:
        fig, ax = plt.subplots()
        fig.tight_layout()
        pd.plotting.parallel_coordinates(
        df2, 'Album_type', color=('#1DB954', '#FF0000')
)
        st.pyplot(fig)

    with subcol5:
        fig, ax = plt.subplots()
        fig.tight_layout()
        sns.lmplot(data=df2, x="xAxis", y="yAxis", hue="Album_type")
        st.pyplot(fig)
