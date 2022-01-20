import streamlit as st
import pickle
import numpy as np

from urllib.request import urlopen  
log_model= cp.load(urlopen('https://drive.google.com/file/d/13wGtV807fq6tZAsHjRmuq6v-WlJsPPu5/view/log_model.pkl', 'rb'))


def classify(num):
    if num == 0:
        return 'NO'
    else:
        return 'YES'


def main(hl=None):
    st.title("CURN RATE PREDICTION")
    html_temp = """
    """

    st.markdown(html_temp, unsafe_allow_html=True)
    activities = ['Logistic Regression']
    option = st.sidebar.selectbox('Which model you would like to use?', activities)
    st.subheader(option)
    st.spinner("Hello")
    hl = st.selectbox('Resort', 'City Hotel')
    lt = st.slider('Lead Time', )
    WN = st.slider('stays in weekend nights', )
    wn = st.slider('stays in week nights', )
    ad = st.slider('Select Adults', )
    ch = st.slider('Select Children', )
    ba = st.slider('Select Babies', )
    inputs = [[hl, lt, WN, wn, ad, ch, ba]]
    if st.button('Classify'):
        if option == 'Logistic Regression':
            st.success(classify(log_reg.predict(inputs)))
        else:
            return 'none'    


if __name__ == '__main__':
    main()
