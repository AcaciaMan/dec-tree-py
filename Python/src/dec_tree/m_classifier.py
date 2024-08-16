from typing import Any
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class M_Classifier(object):
  def __call__(self, *args: Any, **kwds: Any) -> Any:
    clf = DecisionTreeClassifier()
    iris = load_iris()

    print('Data loaded')

    iris_df = pd.DataFrame(iris.data, columns = iris.feature_names)
    iris_df['species'] = iris.target
    #iris_df

    X = iris_df.drop(['species'], axis = 1)
    y = iris_df['species']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

    clf.fit(X_train,y_train)

    predicted = clf.predict(X_test)

    accuracy = accuracy_score(predicted, y_test)
    print(f'Accuracy: {accuracy}')
    return accuracy