from typing import Any
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from child_channel import ChildChannel
#import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import tree
import io

class M_Classifier(object):
  def __init__(self) -> None:
    self.clf = DecisionTreeClassifier()
    self.iris = load_iris()

    print('Data loaded')

    self.iris_df = pd.DataFrame(self.iris.data, columns = self.iris.feature_names)
    self.iris_df['species'] = self.iris.target

  def __call__(self, *args: Any, **kwds: Any) -> Any:

    #iris_df

    #set width to 1000 to avoid truncation
    pd.set_option('display.width', 1000)
    pd.set_option('display.max_columns', None)

    #mark start of stdout message
    print(ChildChannel.STDOUT_START)
    self.iris_df.info()
    #send dataframe to the stdout

    #dataframe describe to print all the columns
  
    print(self.iris_df.describe(include='all'))
    #mark end of stdout message
    print(ChildChannel.STDOUT_END, flush=True)

    X = self.iris_df.drop(['species'], axis = 1)
    y = self.iris_df['species']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

    self.clf.fit(X_train,y_train)

    predicted = self.clf.predict(X_test)

    accuracy = accuracy_score(predicted, y_test)
    print(f'Accuracy: {accuracy}')
    return accuracy
  
  def plot_tree(self):
    """
    docstring
    """
    plt.figure(figsize = (10, 7))
    tree.plot_tree(self.clf, feature_names = self.iris.feature_names, class_names = self.iris.target_names, filled = True)
    #send the plot to the stdout
    print(ChildChannel.STDOUT_START)

    # Save the plot to a buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    
    # Print the buffer's contents
    print(buf.read())
    
    #mark end of stdout message
    print(ChildChannel.STDOUT_END, flush=True)