from typing import Any
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from child_channel import ChildChannel
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import tree

from m_settings.m_settings import M_SettingsSingleton

class M_Classifier(object):
  def __init__(self) -> None:
    self.iset = M_SettingsSingleton()
    self.iris = load_iris()

    print('Data loaded')

    self.iset.df = pd.DataFrame(self.iris.data, columns = self.iris.feature_names)
    self.iset.df['species'] = self.iris.target

  def __call__(self, *args: Any, **kwds: Any) -> Any:

    #iris_df

    #set width to 1000 to avoid truncation
    pd.set_option('display.width', 1000)
    pd.set_option('display.max_columns', None)

    #mark start of stdout message
    print(ChildChannel.STDOUT_START)
    self.iset.df.info()
    #send dataframe to the stdout

    #dataframe describe to print all the columns
  
    print(self.iset.df.describe(include='all'))
    #mark end of stdout message
    print(ChildChannel.STDOUT_END, flush=True)

    X = self.iset.df.drop(['species'], axis = 1)
    y = self.iset.df['species']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

    self.iset.clf.fit(X_train,y_train)

    predicted = self.iset.clf.predict(X_test)

    accuracy = accuracy_score(predicted, y_test)
    print(f'Accuracy: {accuracy}')
    return accuracy
  
  def plot_tree(self):
    """
    docstring
    """
    plt.figure()
    tree.plot_tree(self.iset.clf, feature_names = self.iris.feature_names, class_names = self.iris.target_names, filled = True)
    #send the plot to the stdout
    plt.savefig(self.iset.m_set['rootFolder']+'/decision_tree.png')

  def plot_importance(self):
    """
    docstring
    """
    num_features = len(self.iris.feature_names)
    width = num_features * 1.5  # Adjust the multiplier as needed
    height = 10  # Fixed height or adjust as needed

    # Make new figure with dynamic figsize
    plt.figure(figsize=(width, height))

    sns.barplot(x = self.iris.feature_names, y=self.iset.clf.feature_importances_ )
    plt.xticks(rotation = 50)
    plt.savefig(self.iset.m_set['rootFolder']+'/feature_importance.png')
    