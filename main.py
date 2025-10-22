from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline

df_train = pd.read_csv("dataset/Gungor_2018_VictorianAuthorAttribution_data-train.csv", sep=",", encoding='latin-1')
X_train = df_train["text"].values
y_train = df_train["author"].values
X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.2, random_state=42)
# df_test = pd.read_csv("dataset/Gungor_2018_VictorianAuthorAttribution_data.csv", sep=",", encoding='latin-1')
# X_test = df_test["text"].values

model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LinearSVC(C=1.0))
])

print("*-* Model done")
model.fit(X_train, y_train)
print("*-* Model fit")
y_pred = model.predict(X_test)
print("*-* Acc", accuracy_score(y_test, y_pred))
for i in range(5):
    print(X_test[i][:50], y_pred[i], y_test[i])