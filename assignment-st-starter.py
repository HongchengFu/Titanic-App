# import packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# show the title
st.title('Titanic App by HongchengFu')

# read csv and show the dataframe
df_train = pd.read_csv('train.csv')
df_train

# create a figure with three subplots, size should be (15, 5)
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below

fig, ax = plt.subplots(1, 3, figsize=(15,5))
df_train[(df_train.Pclass == 1)].Fare.plot.box(ax=ax[0])  
df_train[(df_train.Pclass == 2)].Fare.plot.box(ax=ax[1]) 
df_train[(df_train.Pclass == 3)].Fare.plot.box(ax=ax[2]) 

ax[0].set_xlabel('Pclass = 1')
ax[0].set_ylabel('Fare')

ax[1].set_xlabel('Pclass = 2')

ax[2].set_xlabel('Pclass = 3')

st.pyplot(fig)
