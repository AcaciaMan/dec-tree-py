#class to implement regression using decision tree

from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
from m_settings.m_settings import M_SettingsSingleton
from time_decomp.decomposition import DecompositionSingleton

class M_Regressor:
    def __init__(self):
        self.iset = M_SettingsSingleton()
        self.df = pd.read_pickle(self.iset.m_set['rootFolder'] + '/shop_data.pkl')
        self.item_name = 'Cheap drill'
        self.features = ['impressions', 'demand', 'stock', 'sell']
        self.target = 'demand_next_sum'

    def train_regressor(self):
        """
        Train a regressor using the shop data for item 'Cheap drill' sell prediction
        """
        self.df = pd.read_pickle(self.iset.m_set['rootFolder'] + '/shop_data.pkl')
        # Filter the dataframe for the item name
        self.df = self.df[self.df['name'] == self.item_name].copy()

        # calculate the sell for the next 2 months
        self.df['sell_next'] = self.df['sell'].shift(-1)
        self.df['sell_next2'] = self.df['sell'].shift(-2)
        self.df['sell_next_sum'] = self.df['sell_next'] + self.df['sell_next2']
        self.df['sell_next_actual'] = self.df['sell_next_sum'].shift(2)
        self.df['demand_next'] = self.df['demand'].shift(-1)
        self.df['demand_next2'] = self.df['demand'].shift(-2)
        self.df['demand_next_sum'] = self.df['demand_next'] + self.df['demand_next2']
        self.df.dropna(inplace=True)




        # Set the features and target

        X = self.df[self.features]
        y = self.df[self.target]

        # Train the regressor
        self.iset.regressor.fit(X, y)

    def plot_feature_importance(self):
        """
        Plot the feature importance
        """
        # Get the feature importance
        feature_importance = self.iset.regressor.feature_importances_

        # Create a dataframe with the feature importance
        df_feature_importance = pd.DataFrame({'feature': self.features, 'importance': feature_importance})

        # Sort the dataframe by importance
        df_feature_importance = df_feature_importance.sort_values(by='importance', ascending=False)

        # Plot the feature importance
        plt.figure(figsize=(10, 6))
        sns.barplot(x='importance', y='feature', data=df_feature_importance)
        plt.title('Feature Importance')
        plt.savefig(self.iset.getTryFolder() + '/feature_importance.png')

    def plot_sell_prediction(self):
        """
        Plot the sell prediction
        """
        # Predict the sell
        self.df['sell_pred'] = self.iset.regressor.predict(self.df[self.features])

        # Plot the sell and sell prediction
        plt.figure(figsize=(10, 6))
        sns.lineplot(x='month', y='sell_next_actual', data=self.df, label='Actual sell')
        sns.lineplot(x='month', y='sell_pred', data=self.df, label='Predicted sell')
        plt.title('Sell Prediction')
        plt.savefig(self.iset.getTryFolder() + '/sell_prediction.png')

    def plot_seasonality(self):
        """
        Plot the seasonality
        """
        # Get the seasonality
        decomp = DecompositionSingleton()
        decomp.df = self.df
        decomp.features = ['sell']
        decomp.decompose_params = {'model': 'additive', 'period':12, 'extrapolate_trend':'freq'}
        decomp.m_decompose()
        decomp.plot_decomposition('sell', 'year', range(2021,2025), 'month', 'Sells trend')

        plt.savefig(self.iset.getTryFolder() + '/selltrend.png')