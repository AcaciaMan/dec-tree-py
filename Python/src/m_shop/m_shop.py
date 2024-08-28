
import pandas as pd
import numpy as np
#class to manage the shop data
class M_Shop:
    def __init__(self):
        self.shop = []
        self.shop.append({"item":"Drill", "name":"Expensive"})
        self.shop.append({"item":"Drill", "name":"Mid-priced"})
        self.shop.append({"item":"Drill", "name":"Cheap"})
        self.shop.append({"item":"Hammer", "name":"Expensive"})
        self.shop.append({"item":"Hammer", "name":"Mid-priced"})
        self.shop.append({"item":"Hammer", "name":"Cheap"})

        self.ledger = []
        self.ledger.append({"item":"Drill", "name":"Expensive","year":2020,"month":1,"sell":0,"buy":0,"impressions":0,"demand":0, "stock":0})

        self.df = pd.DataFrame()


    def generate_ledger_df(self):
        """
        Generate a dataframe for shop items ledger from January 2019 to current month
        """
        # Create a list of months
        months = []
        for year in range(2019, 2025):
            for month in range(1, 13):
                months.append((year, month))

        # Create a list of items
        items = []
        for item in self.shop:
            items.append((item['item'], item['name']))

        # Create a list of ledger entries
        ledger_entries = []
        for item in items:
            for month in months:
                ledger_entries.append({
                    'item': item[0],
                    'name': item[1],
                    'year': month[0],
                    'month': month[1],
                    'sell': 0,
                    'buy': 0,
                    'impressions': 0,
                    'demand': 0,
                    'stock': 0

                })

        # Create a dataframe from the list of ledger entries
        self.df = pd.DataFrame(ledger_entries)

    def assign_impressions(self):
        """
        Assign impressions to the ledger randomly each month between 0 and 100
        """
        self.df['impressions'] = np.random.randint(0, 100, size=len(self.df))

    def assign_first_month_buy(self):
        """
        Assign a random number of buys to the first month for each item
        """
        for item in self.shop:
            self.df.loc[(self.df['item'] == item['item']) & (self.df['name'] == item['name']) & (self.df['year'] == 2019) & (self.df['month'] == 1), 'buy'] = np.random.randint(10, 30)

    def assign_demand(self):
        """
        Assign a random number of demands to each month for each item
        """
        for item in self.shop:
            for year in range(2019, 2025):
                for month in range(1, 13):
                    self.df.loc[(self.df['item'] == item['item']) & (self.df['name'] == item['name']) & (self.df['year'] == year) & (self.df['month'] == month), 'demand'] = np.random.randint(0, 20)    

    def assign_first_month_sell(self):
        """
        Sell what is in demand in the first month
        Do not sell more than the number of buys in the first month
        """
        for item in self.shop:
            self.df.loc[(self.df['item'] == item['item']) & (self.df['name'] == item['name']) & (self.df['year'] == 2019) & (self.df['month'] == 1), 'sell'] = min(self.df.loc[(self.df['item'] == item['item']) & (self.df['name'] == item['name']) & (self.df['year'] == 2019) & (self.df['month'] == 1), 'demand'].iloc[0], self.df.loc[(self.df['item'] == item['item']) & (self.df['name'] == item['name']) & (self.df['year'] == 2019) & (self.df['month'] == 1), 'buy'].iloc[0])

    def update_stock(self, year, month):
        """
        Update the stock
        """
        for item in self.shop:
            if month == 1 and year == 2019:
                self.df.loc[(self.df['item'] == item['item']) & (self.df['name'] == item['name']) & (self.df['year'] == year) & (self.df['month'] == month), 'stock'] = int(
                    self.df.loc[(self.df['item'] == item['item']) & (self.df['name'] == item['name']) & (self.df['year'] == year) & (self.df['month'] == month), 'buy'].iloc[0] - 
                    self.df.loc[(self.df['item'] == item['item']) & (self.df['name'] == item['name']) & (self.df['year'] == year) & (self.df['month'] == month), 'sell'].iloc[0]
                    )
            elif month == 1 and year != 2019:
                self.df.loc[(self.df['item'] == item['item']) & (self.df['name'] == item['name']) & (self.df['year'] == year) & (self.df['month'] == month), 'stock'] = int(self.df.loc[(self.df['item'] == item['item']) & (self.df['name'] == item['name']) & (self.df['year'] == year-1) & (self.df['month'] == 12), 'stock'].iloc[0] + self.df.loc[(self.df['item'] == item['item']) & (self.df['name'] == item['name']) & (self.df['year'] == year) & (self.df['month'] == month), 'buy'].iloc[0] - self.df.loc[(self.df['item'] == item['item']) & (self.df['name'] == item['name']) & (self.df['year'] == year) & (self.df['month'] == month), 'sell'].iloc[0])
            else:
                self.df.loc[(self.df['item'] == item['item']) & (self.df['name'] == item['name']) & (self.df['year'] == year) & (self.df['month'] == month), 'stock'] = int(self.df.loc[(self.df['item'] == item['item']) & (self.df['name'] == item['name']) & (self.df['year'] == year) & (self.df['month'] == month-1), 'stock'].iloc[0] + self.df.loc[(self.df['item'] == item['item']) & (self.df['name'] == item['name']) & (self.df['year'] == year) & (self.df['month'] == month), 'buy'].iloc[0] - self.df.loc[(self.df['item'] == item['item']) & (self.df['name'] == item['name']) & (self.df['year'] == year) & (self.df['month'] == month), 'sell'].iloc[0])

    def buy_and_sell(self):
        """
        Buy and sell items
        """
        self.generate_ledger_df()
        self.assign_impressions()
        self.assign_first_month_buy()
        self.assign_demand()
        self.assign_first_month_sell()
        self.update_stock( 2019, 1)
        #each month buy item randomly between 10 and 30 if previous month stock is less than 5
        #each month sell items in demand whenever there are items in stock
        #update stock for each month
        for item in self.shop:
            for year in range(2019, 2025):
                for month in range(1, 13):
                    if month == 1 and year == 2019:
                        continue
                    elif month == 1 and year != 2019:
                        if (self.df.loc[(self.df['item'] == item['item']) & (self.df['name'] == item['name']) & (self.df['year'] == year-1) & (self.df['month'] == 12), 'stock'] < 5).all():
                            self.df.loc[(self.df['item'] == item['item']) & (self.df['name'] == item['name']) & (self.df['year'] == year) & (self.df['month'] == month), 'buy'] = np.random.randint(10, 30)
                        #sell items in demand whenever there are items in stock
                        # Do not sell more than the number of items in stock
                        # Do not sell more than the demand
                        self.df.loc[(self.df['item'] == item['item']) & (self.df['name'] == item['name']) & (self.df['year'] == year) & (self.df['month'] == month), 'sell'] = min(self.df.loc[(self.df['item'] == item['item']) & (self.df['name'] == item['name']) & (self.df['year'] == year-1) & (self.df['month'] == 12), 'stock'].iloc[0], self.df.loc[(self.df['item'] == item['item']) & (self.df['name'] == item['name']) & (self.df['year'] == year) & (self.df['month'] == month), 'demand'].iloc[0])     
                        self.update_stock( year, month)
                    else:
                        if (self.df.loc[(self.df['item'] == item['item']) & (self.df['name'] == item['name']) & (self.df['year'] == year) & (self.df['month'] == month-1), 'stock'] < 5).all():
                            self.df.loc[(self.df['item'] == item['item']) & (self.df['name'] == item['name']) & (self.df['year'] == year) & (self.df['month'] == month), 'buy'] = np.random.randint(10, 30)
                        #sell items in demand whenever there are items in stock
                        # Do not sell more than the number of items in stock
                        # Do not sell more than the demand
                        self.df.loc[(self.df['item'] == item['item']) & (self.df['name'] == item['name']) & (self.df['year'] == year) & (self.df['month'] == month), 'sell'] = min(self.df.loc[(self.df['item'] == item['item']) & (self.df['name'] == item['name']) & (self.df['year'] == year) & (self.df['month'] == month-1), 'stock'].iloc[0], self.df.loc[(self.df['item'] == item['item']) & (self.df['name'] == item['name']) & (self.df['year'] == year) & (self.df['month'] == month), 'demand'].iloc[0])    
                        self.update_stock( year, month)

        

        return self.df




            


