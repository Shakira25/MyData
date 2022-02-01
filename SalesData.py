import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


sales = pd.read_csv('../sales.csv')


def print_total_sales_in_dec():
    total_sales = sales['Amount'].sum()
    print("{:,}".format(round(total_sales)))

def print_most_profitable_item():
    y = sales.groupby(['Trade Name'],as_index=True).sum()
    x = y.sort_values(['Profit'], ascending = False)
    w = x.iloc[0].to_frame()
    print(w)

def print_least_profitable_item():
    y = sales.groupby(['Trade Name'], as_index = True).sum()
    x = y.sort_values(['Profit'], ascending = True)
    w = x.iloc[0].to_frame()
    print(w)

def print_dispenser_that_sold_most():
    y = sales.groupby(['Dispenser'], as_index =True).sum()
    x = y.sort_values(['Amount'], ascending = False)
    w = x.iloc[0].to_frame()
    print(w)

def print_dispenser_that_sold_least():
    y = sales.groupby(['Dispenser'], as_index =True).sum()
    x = y.sort_values(['Amount'], ascending = True)
    w = x.iloc[0].to_frame()
    print(w)

def print_item_that_sold_most():
    y = sales.groupby(['Trade Name'], as_index =True).sum()
    x = y.sort_values(['Amount'], ascending = False)
    w = x.iloc[0].to_frame()
    print(w)
    
def print_item_that_sold_least():
    y = sales.groupby(['Trade Name'], as_index =True).sum()
    x = y.sort_values(['Amount'], ascending = True)
    w = x.iloc[0].to_frame()
    print(w)

