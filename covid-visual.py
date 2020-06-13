import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#read confirmed
corona_dataset_csv = pd.read_csv("Dataset/cofirmed_dataset.csv")

#remove unnecessary coulumn
corona_dataset_csv.drop("Lat","Long",axis =1 , inplace= True)

#group by
corna_dataset_aggregate = corona_dataset_csv.groupby(Country/Region).sum()

#sample plot
#corona_dataset_aggregate.loc["China"].plot()  #[:3]
#plt.legend()

#sample country max infect 
#corona_dataset_aggregate.loc["China"].diff().max()

#find least position of country in memory
county = list(corona_dataset_aggregate.index)
max_infection_rate = []

#finding max infection rate for all countries
for i in county:
	max_infection_rate.append(corona_dataset_aggregated.loc[i].diff().max()
corona_dataset_aggregated["max_infect_rate"] = max_infection_rate

#keeping only max infect rate, removing else
corona_data = pd.DataFrame(corona_dataset_aggregated["max_infect_rate"])

#reading second
happiness_report_csv = pd.read("Datasets/worlds_report.csv")

#un-necessary coulumns
useless_coulumn = ["Overall rank", "Score", "Generosity", "Perception of corruption"]

#removing them
happiness_report_csv.drop(useless_coulumn,axis =1. inplace = True)

#changing index to same as the above dataset
happiness_report_csv.set_index("Country or region", inplace = True)

#verify shape similarity
#corona_data.shape

#inner join for ease
data = corona_data.join(happiness_report_csv, how = "inner")

#correlation of it
data.corr()

#coordinate from the joined dataset
x = data["GDP per capita"]
y = data["max_infect_rate"]

#simple scatterplot
sns.scatterplot(x, np.log(y))

#Final regression plot
sns.regplot(x, np.log(y))
