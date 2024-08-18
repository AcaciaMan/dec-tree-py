import pandas as pd
from sklearn.tree import DecisionTreeClassifier

class M_SettingsSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(M_SettingsSingleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        """
        docstring
        """
        if not hasattr(self, 'initialized'):  # Ensure __init__ is called only once
            self.df = pd.DataFrame()
            self.clf = DecisionTreeClassifier()
            self.m_set = {}
            self.initialized = True

    def addSettings(self, settings):
        """go through the settings dictionary and add them to the settings dictionary"""
        for key in settings:
            self.m_set[key] = settings[key]