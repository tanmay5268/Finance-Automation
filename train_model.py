import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer#this ia a class
from sklearn.model_selection import train_test_split#this is a module
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

#1:loading the data
try:
    data = pd.read_csv("labeled_transaction.csv")
except Exception as e:
    print(f"{e}")
finally:
    print(data)
#2: preparing data for testing
X = data["Details"]
y = data["Category"]
#3:text to numbers using bag.of.words vala logic
vectorizer = CountVectorizer()
x_vector=vectorizer.fit_transform(X)
#4: data ko testing and training me split krna
X_train,X_test,y_train,y_test = train_test_split(x_vector,y,test_size =0.1,random_state = 42 ) 
#5:model training
model = MultinomialNB(alpha=0.5)
model.fit(X_train,y_train)
#6:testing phase
scores=model.score(X_test,y_test)
print(f"Model accuracy: {scores*100}%")

