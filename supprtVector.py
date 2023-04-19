from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import train_test_split

# Load the iris dataset
iris = datasets.load_iris()
X = iris["data"]
y = iris["target"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0)

# Train a SVM classifier on the training data
clf = svm.SVC(kernel='linear', C=1, random_state=0)
clf.fit(X_train, y_train)

# Evaluate the classifier on the testing data
accuracy = clf.score(X_test, y_test)
print("Accuracy: ", accuracy)