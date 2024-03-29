import streamlit as st
import requests

st.title("My iris classifier app")

st.write("Select your features")

# Creating four sliders
value1 = st.slider('Select a value for Sepal length', min_value=0, max_value=4, value=1, step=1)
value2 = st.slider('Select a value for Sepal width',  min_value=0, max_value=4, value=1, step=1)
value3 = st.slider('Select a value for Petal length',  min_value=0, max_value=4, value=1, step=1)
value4 = st.slider('Select a value for Petal width',  min_value=0, max_value=4, value=1, step=1)

# TEST LINE
response = requests.get(f"https://mvp15812-tqemn5tozq-ew.a.run.app/predict?sepal_length={value1}&sepal_width={value2}&petal_length={value3}&petal_width={value4}").json()
st.write("The flower belongs to class", str(response['prediction']))


# Create the github repo to connect to streamlit cloud
# cd package_folder
# git init
# gh repo create -> follow instructions#
# git status -> untracked files
# git add commit push (3)
