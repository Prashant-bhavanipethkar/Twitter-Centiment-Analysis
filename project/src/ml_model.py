import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib


train = pd.read_csv(r'/home/prashant/Twitter-Centiment-Analysis/project/data/processed_data/train.csv')
test = pd.read_csv(r'/home/prashant/Twitter-Centiment-Analysis/project/data/processed_data/test.csv')

train.dropna(inplace=True)
test.dropna(inplace=True)

# Step 1: Vectorize text data
vectorizer = TfidfVectorizer(max_features=30000, ngram_range=(1,3),sublinear_tf=True)
X_train_tfidf = vectorizer.fit_transform(train['cleaned_text'])
X_test_tfidf = vectorizer.transform(test['cleaned_text'])

y_train = train['target']
y_test = test['target']

print('TF-IDF vectorization done')


# Step 2: Train Logistic Regression
model = LogisticRegression(
    C=2,
    class_weight='balanced',
    solver='liblinear',
    max_iter=2000
)

model.fit(X_train_tfidf, y_train)


# Step 3: Save model and vectorizer
joblib.dump(model, r'/home/prashant/Twitter-Centiment-Analysis/project/src/logistic_model.pkl')
joblib.dump(vectorizer, r'/home/prashant/Twitter-Centiment-Analysis/project/src/tfidf-vectorizer.pkl')


# Step 4: Evaluate
y_pred = model.predict(X_test_tfidf)
print(classification_report(y_test,y_pred))