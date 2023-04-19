import pandas as pd
from sklearn.naive_bayes import BernoulliNB # Import BernoulliNB Naive Bayes Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
url = 'https://raw.githubusercontent.com/ashokgit/DataSets/main/heart.csv';
# load dataset
pima = pd.read_csv(url)
# pima.tail()

# feature_cols = ['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal']
X = pima[feature_cols] # Features
y = pima.target # Target variable
# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # 70% training and 30% test
# Create Naive Bayes classifer object
clf = BernoulliNB()
# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)
#Predict the response for test dataset
y_pred = clf.predict(X_test)
# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))