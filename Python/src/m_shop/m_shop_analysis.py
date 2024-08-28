#class to analyze the data from the m_shop table
from matplotlib import pyplot as plt
from m_settings.m_settings import M_SettingsSingleton
import pandas as pd
import seaborn as sns

class M_ShopAnalysis:

    def __init__(self):
        self.iset = M_SettingsSingleton()
        #load the dataframe from pickle
        self.df = pd.DataFrame().from_pickle(self.iset.m_set['rootFolder'] +'/shop_data.pkl')

    #method to plot yearly sell per item name
    def plot_yearly_sell(self):
        """
        Plot the yearly sell per item name
        """
        #group by item name and year and sum the sell
        df_yearly_sell = self.df.groupby(['name', 'year'])['sell'].sum().reset_index()
        #plot the data
        plt.figure(figsize=(10, 6))
        sns.lineplot(x='year', y='sell', hue='name', data=df_yearly_sell)
        plt.title('Yearly sell per item name')
        plt.savefig(self.iset.getTryFolder() + '/yearly_sell.png')

    #method to plot yearly stock per item name
    def plot_yearly_stock(self):
        """
        Plot the yearly stock per item name
        """
        #group by item name and year and sum the stock
        df_yearly_stock = self.df.groupby(['name', 'year'])['stock'].sum().reset_index()
        #plot the data
        plt.figure(figsize=(10, 6))
        sns.lineplot(x='year', y='stock', hue='name', data=df_yearly_stock)
        plt.title('Yearly stock per item name')
        plt.savefig(self.iset.getTryFolder() + '/yearly_stock.png')




    