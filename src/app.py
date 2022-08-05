import streamlit as st
import pandas as pd
import pandas as pd
import numpy as np
import altair as alt
import streamlit as st

# Reuse this data across runs!
read_and_cache_csv = st.cache(pd.read_csv)

BUCKET = "https://streamlit-self-driving.s3-us-west-2.amazonaws.com/"
data = read_and_cache_csv(BUCKET + "labels.csv.gz", nrows=1000)
desired_label = st.selectbox('Filter to:', ['car', 'truck'])
st.write(data[data.label == desired_label])

age = st.selectbox("Choose your age:", np.arange(18, 66, 1))
age = st.slider("Choose your age: ", min_value=16,   
                       max_value=66, value=35, step=1)
artists = st.multiselect("Who are your favorite artists?", 
                         ["Michael Jackson", "Elvis Presley",
                         "Eminem", "Billy Joel", "Madonna"])

st.sidebar.checkbox("Show Analysis by State", True, key=1)

df = pd.DataFrame(np.random.randn(200, 3), columns=['a', 'b', 'c'])
c = alt.Chart(df).mark_circle().encode(x='a', y='b', size='c',  
                                       color='c')
st.altair_chart(c)