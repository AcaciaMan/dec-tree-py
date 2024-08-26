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
            self.m_conf = {}
            self.m_try = {}
            self.initialized = True

    def addSettings(self, settings):
        """go through the settings dictionary and add them to the settings dictionary"""
        for key in settings:
            self.m_set[key] = settings[key]
            if key == 'shop-config':
                self.addConf(settings[key])

    def addConf(self, conf):
        """go through the configuration dictionary and add them to the configuration dictionary"""
        for key in conf:
            self.m_conf[key] = conf[key]

        self.addTry(self.m_conf[self.getCurrentTry()])

    def addTry(self, try_dict):
        """go through the try dictionary and add them to the try dictionary"""
        for key in try_dict:
            self.m_try[key] = try_dict[key]

    def getCurrentTry(self):
        """return the current try"""
        return self.m_conf['current_try']
    
    def getTryFolder(self):
        """return the current try folder"""
        return self.m_set['rootFolder']+self.m_try['name']
    
