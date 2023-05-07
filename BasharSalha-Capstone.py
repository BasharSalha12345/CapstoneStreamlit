from textblob import TextBlob
import pandas as pd
import streamlit as st
import cleantext


st.header('Sentiment Analysis')
with st.expander('Analyze Text'):
    text = st.text_input('Text here: ')
    if text:
        clean_text = cleantext.clean(text, clean_all= False, extra_spaces=True ,
                                 stopwords=True ,lowercase=True ,numbers=True , punct=True)
        blob = TextBlob(clean_text)
        st.write("Clean Text: ", clean_text)
        st.write('Polarity: ', round(blob.sentiment.polarity,2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity,2))



#
    def analyze(x):
        if x >= 0:
            return 'Positive'
        elif x < 0:
            return 'Negative'
        else:
            return 'Neutral'
