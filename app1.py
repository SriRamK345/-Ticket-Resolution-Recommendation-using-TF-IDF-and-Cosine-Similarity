# Data Preprocessing
import pandas as pd
# Data Manipulation
import numpy as np
# Text Preprocessing
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import string
import re
import random
# Ignore Warning
import warnings
warnings.filterwarnings("ignore")
# Vectorization
from sklearn.feature_extraction.text import TfidfVectorizer
# Cosine Similarity 
from sklearn.metrics.pairwise import cosine_similarity
# Web App
import streamlit as st

# Download NLTK data
# nltk.download('wordnet')
# nltk.download('punkt_tab')
# nltk.download('stopwords')
# nltk.download('wordnet')

# Load the data
df = pd.read_csv("G:\VS Code\Test\melted_df.csv")

# Function to Preprocess the data
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()
number_pattern = re.compile(r"\d+")

def preprocess_test(text):
  text = number_pattern.sub("", text)  # Remove numbers
  text = text.translate(str.maketrans("", "", string.punctuation)).lower()  # Remove punctuation and lowercase
  text = [lemmatizer.lemmatize(word) for word in text.split() if word not in stop_words] # Lemmatization & stop word removal
  return " ".join(text)

# Apply the preprocessing function to the 'Description' column
df['Cleaned Description'] = df['Description'].apply(preprocess_test)

# Create a TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Fit the vectorizer to the issue descriptions and transform them into vectors
X_issues = vectorizer.fit_transform(df['Cleaned Description'])

# Transform the resolutions into vectors using the same vectorizer
X_resolutions = vectorizer.transform(df['Description'])

# Function to find the most similar resolution
def find_resolution(input_issue):

    # Preprocess the input issue
    preprocessed_test = preprocess_test(input_issue)
    # Transform into a vector
    input_vector = vectorizer.transform([preprocessed_test])
    # Calculate cosine similarity between the input vector and all resolution vectors
    similarities = cosine_similarity(input_vector, X_resolutions).flatten()   
    # Find the index of the most similar resolution
    closest_resolution_index = np.argmax(similarities)
    # Return the most similar resolution
    return df['Possible Resolution'].iloc[closest_resolution_index]

# Streamlit App

st.title(":red[End user Issue Resolution App]")
# User input   
input_issue = st.text_input("**:violet[Enter the issue description:]**")
# Button
if st.button("Get Resolution"):
    if input_issue:
        if re.match("^[0-9]+$", input_issue):
            st.warning("Please enter a descriptive issue, not just a number.")
        else:
            resolution = find_resolution(input_issue)
            steps = resolution.split(";")
            # Display each step
            for i, step in enumerate(steps, start=1):
                st.write(f"**Step {i}:** {step.strip()}")

    else:
        st.warning("Please enter an issue.")
