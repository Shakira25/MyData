import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


import requests
import io
url = "https://raw.githubusercontent.com/Shakira25/MyData/main/insurance.csv"
download = requests.get(url).content
df = pd.read_csv(io.StringIO(download.decode('utf-8')))

df = pd.read_csv('insurance.csv')

def print_the_first_five_rows():
    df.head()

def print_number_of_rows_and_columns():
    df.shape

def print_the_size_of_our_data():
    df.size

def print_the_different_data_types():
    df.dtypes

def print_the_statistical_summaries():
    df.describe()

def draw_pie_chart_showing_the_size_of_each_region():
    plt.figure(figsize=(15,10))
    df['region'].value_counts().plot(kind='pie',autopct='%.2f%%')
    plt.show()
    plt.savefig('state.png')

def plot_a_box_plot_showing_distribution_of_charges_among_smokers():
    sns.catplot(x="smoker", y="charges", kind="box", data=df)
    plt.title('Distribution of charges among smokers')

def plot_a_bar_plot_showing_charges_per_region():
    plt.figure(figsize=(15,10))
    df["region"].value_counts().plot.bar(title="Bar Graph Showing charges Per region")
    plt.ylabel('charges')
    plt.xlabel('region')

def plot_a_box_plot_showing_distribution_of_charges_among_smokers_of_different_sexes():
    sns.catplot(x="sex", y="charges", hue="smoker", kind="box", data=df)
    plt.title('Distribution of charges among smokers and non smokers of different sexes')

def plot_a_bar_plot_showing_smoking_status_and_number_of_charges_per_region():
    sns.barplot(data=df, x= 'charges', y='smoker', hue='region')
    plt.title('A bar plot showing smoking status and number of charges per region')
#According to the graph below, the more someone smokes the higher the charges. Southwest had the highest number of smokers and Northwest had the least number of smokers.

def plot_bar_gragh_showing_smoking_status_and_number_of_charges():
    sns.barplot(data=df, x= 'charges', y='smoker', hue='sex')
    plt.title('A bar plot showing smoking status and number of charges per sex')

def plot_scatter_plot_showing_relationship_between_age_and_charges():
    sns.lmplot(x='age', y='charges', data=df)
    plt.title('Relationship between age and charges')
