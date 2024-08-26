from dec_tree.m_dec_tree_clf import M_DecTreeClfSingleton
from sklearn.datasets import load_iris
import pandas as pd

class M_DecTreeIris(M_DecTreeClfSingleton):
    def __init__(self):
        """
        docstring
        """
        if not hasattr(self, 'initialized'):  # Ensure __init__ is called only once
            super().__init__()
            self.iris = load_iris()
            self.initialized = True

    def load_df(self):
        """
        Load a dataframe 
        """


        print('Data loaded')

        self.iset.df = pd.DataFrame(self.iris.data, columns = self.iris.feature_names)
        self.iset.df['species'] = self.iris.target
        return True


