import streamlit as st #type: ignore
from transformers import pipeline

st.title("Sentiment Analysis Bot")
st.write("This bot analyzes the sentiment of the text you enter.")

@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")

sentiment_analyzer = load_model()

id2label = {
    0: "Negative",  # LABEL_0
    1: "Neutral",   # LABEL_1
    2: "Positive"   # LABEL_2
}

user_input = st.text_area("Please enter your text here")

if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter valid text.")
    else:
        with st.spinner("Analyzing..."):
            result = sentiment_analyzer(user_input)
            label = result[0]['label'] 
            score = result[0]['score']

            label_index = int(label.split('_')[-1])
            human_readable_label = id2label[label_index]

            st.success(f"Sentiment: {human_readable_label}, Trust Score: {score:.2f}")