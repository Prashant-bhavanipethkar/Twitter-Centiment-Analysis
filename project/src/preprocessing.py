# Import libraries
import numpy as np
import pandas as pd

import re
import string
import emoji
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer

import nltk
import emoji

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

lemmatizer = WordNetLemmatizer()


# Clean text
def clean_text(text):

    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'#', '', text)
    text = emoji.demojize(text)
    punct = string.punctuation.replace("!", "").replace("?", "")
    text = text.translate(str.maketrans("", "", punct))
    text = re.sub(r'\d+', '', text)
    text = text.lower().strip()
    tokens = word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return ' '.join(tokens)


# data preprocessing  
def data_preprocessing(input_csv, output_dir):

    # importing csv file
    df = pd.read_csv(input_csv, encoding='latin1')

    # label encoder
    le = LabelEncoder()
    df['target'] = le.fit_transform(df['target'])

    # data cleaning
    df = df[['cleaned_text','target']]
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)

    df['cleaned_text'] = df['cleaned_text'].apply(clean_text)

    train, temp = train_test_split(df, test_size=0.2, random_state=42, stratify=df['target'])
    val,test = train_test_split(temp, test_size=0.5, random_state=42, stratify=temp['target'])

    train.to_csv(f"{output_dir}/train.csv", index=False)
    val.to_csv(f"{output_dir}/val.csv", index=False)
    test.to_csv(f"{output_dir}/test.csv", index=False)

    print('Data preprocessing completed')

input_csv = r'/home/prashant/Twitter-Centiment-Analysis/project/data/raw_data/sentiment140_cleaned.csv'
output_dir = r'/home/prashant/Twitter-Centiment-Analysis/project/data/processed_data'

data_preprocessing(input_csv, output_dir)
