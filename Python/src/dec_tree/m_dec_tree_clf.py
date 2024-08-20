from matplotlib import pyplot as plt
from sklearn import tree
from sklearn.base import accuracy_score
from sklearn.model_selection import train_test_split
from m_settings.m_settings import M_SettingsSingleton
import seaborn as sns


class M_DecTreeClfSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(M_DecTreeClfSingleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        """
        docstring
        """
        if not hasattr(self, 'initialized'):  # Ensure __init__ is called only once
            self.iset = M_SettingsSingleton()
            self.initialized = True

    def generate_df(self):
        """
        Generate a dataframe 
        """
        #make method abstract
        pass

    def train_clf(self):
        """
        docstring
        """
        X = self.iset.df[self.iset.m_set['features_names']]
        y = self.iset.df[self.iset.m_set['target_name']]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

        self.iset.clf.fit(X_train, y_train)

        predicted = self.iset.clf.predict(X_test)

        accuracy = accuracy_score(predicted, y_test)
        print(f'Accuracy: {accuracy}')
        return accuracy
    
    def plot_tree(self):
        """
        Plot the decision tree with dynamic figsize
        """
        # Determine the depth of the tree
        tree_depth = self.iset.clf.get_depth()
        num_leaves = self.iset.clf.get_n_leaves()

        # Set the width and height proportional to the depth and number of leaves
        width = tree_depth * 2
        height = num_leaves * 0.5

        # Make new figure with dynamic figsize
        plt.figure(figsize=(width, height))
        tree.plot_tree(self.iset.clf, feature_names=self.iset.m_set['features_names'], class_names=self.iset.m_set['class_name'], filled=True)
        #send the plot to the stdout
        plt.savefig(self.iset.m_set['rootFolder']+'/decision_tree.png')

    def plot_feature_importance(self):
        """
        docstring
        """
        num_features = len(self.iset.m_set['features_names'])
        width = num_features * 1.5  # Adjust the multiplier as needed
        height = 10  # Fixed height or adjust as needed

        # Make new figure with dynamic figsize
        plt.figure(figsize=(width, height))

        sns.barplot(x = self.iset.m_set['features_names'], y=self.iset.clf.feature_importances_ )
        plt.xticks(rotation = 50)
        plt.savefig(self.iset.m_set['rootFolder']+'/feature_importance.png')
    