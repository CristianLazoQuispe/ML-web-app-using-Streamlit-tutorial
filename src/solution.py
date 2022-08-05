import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

#data = pd.read_csv('https://raw.githubusercontent.com/4GeeksAcademy/random-forest-project-tutorial/main/titanic_train.csv', sep=',')

@st.cache(ttl=60*5, max_entries=20)
def load_data():
    data = sns.load_dataset("titanic")
    return data




data = load_data()

st.markdown('<style>description{color:blue;}</style>', unsafe_allow_html=True)
st.title('Titanic survival prediction')
st.markdown("<description>The sinking of the Titanic is one of the most infamous shipwrecks in history. " + 
"On April 15, 1912, during her maiden voyage, the widely considered “unsinkable” RMS Titanic sank after colliding" +
"with an iceberg. Unfortunately, there weren’t enough lifeboats for everyone onboard, resulting in the death of " +
"1502 out of 2224 passengers and crew. While there was some element of luck involved in surviving, it seems some" +
" groups of people were more likely to survive than others. </description>", unsafe_allow_html=True)
st.sidebar.title('Select the parameters to analyze survival prediction')


Embarked_list = list(data['sex'].unique())

desired_label = st.selectbox('Filter sex to:', Embarked_list)
st.write(data[data.sex == desired_label][:20])

sub_data = data[data.sex == desired_label]

if st.checkbox("Seaborn Pairplot",value=True):
    fig = sns.catplot(x="deck", y="survived", hue="class",
     kind="bar", data=sub_data, height=4.27, aspect=8.7/4.27)
    plt.title('Filter sex to:'+str(desired_label))
    st.pyplot(fig)

    fig = sns.catplot(x="deck", kind="count", palette="ch:.25", data=sub_data)
    plt.title('Filter sex to:'+str(desired_label))
    st.pyplot(fig)