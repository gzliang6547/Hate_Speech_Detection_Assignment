import streamlit as st
import nltk
from nltk import NaiveBayesClassifier
from nltk.classify import apply_features
from joblib import load

# Load the trained Naive Bayes classifier
naive_bayes_classifier = load('model.joblib')
tfidf_vector = load('vectorizer.joblib')

# Streamlit app
def main():
    st.title('Hate Speech Detection App')
    st.write('Enter a sentence to detect.')

    # Input for name
    input_text = st.text_input('Sentence:')
    
    if st.button('Detect'):
        if input_name.strip() != '':
	     test_input = tfidf_vector.transform(input_text)
	     res=naive_bayes_classifier.predict(test_input)[0]

	     if res==1:
	         detection="Hateful"
	     elif res==0:
	         detection="Non-Hateful"
            
            # Display prediction
            st.success(f'The sentence {input_text} is a {detection}')
        else:
	    st.warning('Please enter some words.')


if __name__ == '__main__':
    main()
