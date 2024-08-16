from typing import Any
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from child_channel import ChildChannel

class M_Classifier(object):
  def __call__(self, *args: Any, **kwds: Any) -> Any:
    clf = DecisionTreeClassifier()
    iris = load_iris()

    print('Data loaded')

    iris_df = pd.DataFrame(iris.data, columns = iris.feature_names)
    iris_df['species'] = iris.target
    #iris_df

    #set width to 1000 to avoid truncation
    pd.set_option('display.width', 1000)
    pd.set_option('display.max_columns', None)

    #mark start of stdout message
    print(ChildChannel.STDOUT_START)
    iris_df.info()
    #send dataframe to the stdout

    #dataframe describe to print all the columns
  
    print(iris_df.describe(include='all'))
    #mark end of stdout message
    print(ChildChannel.STDOUT_END, flush=True)

    X = iris_df.drop(['species'], axis = 1)
    y = iris_df['species']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

    clf.fit(X_train,y_train)

    predicted = clf.predict(X_test)

    accuracy = accuracy_score(predicted, y_test)
    print(f'Accuracy: {accuracy}')
    return accuracy