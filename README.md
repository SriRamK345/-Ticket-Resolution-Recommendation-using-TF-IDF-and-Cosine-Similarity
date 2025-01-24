# End User Issue Resolution Recommendation System

## Overview

This Project demonstrates a End User Issue Resolution Recommendation system using Natural Language Processing (NLP) techniques. The system aims to automatically suggest resolutions for user-submitted tickets based on their descriptions.This Streamlit app is designed to help end users resolve common issues by providing step-by-step resolutions based on the issue description entered by the them.

## Data

The system is trained on a dataset of tickets and their corresponding resolutions.  The data is initially preprocessed, then augmented with synonyms to increase the volume of data and enhance model performance. It then undergoes another preprocessing step to remove noise and unnecessary information. Finally, TF-IDF is applied to numerically represent the processed ticket descriptions.

## Methodology

1. **Data Preprocessing:**
    - Removal of numbers and punctuation from ticket descriptions.
    - Conversion of text to lowercase.
    - Lemmatization of words.
    - Removal of stop words.

2. **Data Augmentation:**
    - Generate synonyms for the given sentences using WordNet.
    - Replace random words with their synonyms and generate new sentences.

3. **TF-IDF Vectorization:**
    - Convert text descriptions into numerical vectors using TF-IDF.
    - This allows for efficient similarity comparisons between tickets.

4. **Cosine Similarity:**
    - Calculate the cosine similarity between the input ticket description and the existing ticket descriptions in the dataset.

5. **Resolution Recommendation:**
    - Identify the ticket description with the highest cosine similarity to the input ticket.
    - Recommend the resolution associated with the most similar ticket.

## Web Application Features

- **User Input**: Users can enter a descriptive issue in the input field.
- **Resolution Generation**: Upon clicking the "Get Resolution" button, the app generates and displays a step-by-step resolution for the entered issue.
- **Step-by-Step Display**: The resolution is split into numbered steps for easy understanding.
- **Validation**: The app validates user input to ensure it is descriptive and not just a number.

## Usage

1. **Enter Issue Description**:
   - Type a descriptive issue in the input field labeled "Enter the issue description:".
2. **Get Resolution**:
   - Click the "Get Resolution" button to generate and display the step-by-step resolution.
3. **View Steps**:
   - The app will display each step of the resolution with step numbers.

## Dependencies

- Python
- pandas
- scikit-learn
- nltk
- numpy
- re
- string

## Installation

To run this app, you need to have Python and Streamlit installed. Here are the steps to set up your environment:

```bash
# Install Streamlit if not already installed
pip install streamlit

# Clone or download this repository
git clone https://github.com/your-username/your-repo-name.git

# Navigate to the repository directory
cd your-repo-name

# Run the Streamlit app
streamlit run app.py

## Example Usage

Here’s an example of how you might use this app:

- Enter an issue description: "My computer won't turn on."
- Click "Get Resolution."
- The app will display steps such as:
  ```
  **Step 1:** Check power cord and ensure it is properly connected
  **Step 2:** Try using a different power outlet or replace the power supply if necessary.
  ```
