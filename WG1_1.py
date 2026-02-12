#%%hoi
import pandas
data = pandas.read_csv("datasets.csv")
print(data.shape)
dataset_names = data["dataset"].unique() #dataset is je eerste kolom in je csv file, dus je haalt alle unieke waarden uit die kolom
print(dataset_names) #print alle unieke dataset namen

#%%
mean = data.groupby("dataset").mean() #groep de data op dataset naam en bereken het gemiddelde van de  kolom voor elke groep
std = data.groupby("dataset").std()  #groep de data op dataset naam en bereken de standaarddeviatie van de  kolom voor elke groep
var = data.groupby("dataset").var()  #groep de data op dataset naam en bereken de variantie van de  kolom voor elke groep
count = data.groupby("dataset").count() #groep de data op dataset naam en tel het aantal rijen voor elke groep
print(mean) #print het gemiddelde van de  kolom voor elke dataset
print(std) #print de standaarddeviatie van de  kolom voor elke dataset
print(var) #print de variantie van de  kolom voor elke dataset
print(count) #print het aantal rijen voor elke dataset

#%%
import matplotlib.pyplot as plt
import seaborn as sns   

sns.violinplot(x="dataset", y="x", data=data) #maak een violin plot van de kolom x voor elke dataset
plt.show() #toon de plot

sns.violinplot(x="dataset", y="y", data=data) #maak een violin plot van de kolom x voor elke dataset
plt.show() #toon de plot

#%%
grouped = data.groupby("dataset") #groep de data op dataset naam
correlation = grouped.apply(lambda g: g["x"].corr(g["y"]))

print(correlation) #print de correlatie tussen de kolommen x en y voor elke dataset


# %%
grouped = data.groupby("dataset") #groep de data op dataset naam
covariance = grouped.apply(lambda g: g["x"].cov(g["y"]))

print(covariance) #print de covariantie tussen de kolommen x en y voor elke dataset


# %%
from scipy.stats import linregress
from scipy import stats

grouped = data.groupby("dataset") #groep de data op dataset naam
regression_results = grouped.apply(lambda g: stats.linregress(g["x"], g["y"]))    
print(regression_results) #print de resultaten van de lineaire regressie tussen de kolommen x en y voor elke dataset
linreg_df = grouped.apply(lambda g: pandas.Series(stats.linregress(g["x"], g["y"]), index=["slope", "intercept", "r_value", "p_value", "std_err"])) #maak een dataframe van de resultaten van de lineaire regressie tussen de kolommen x en y voor elke dataset
print(linreg_df) #print de dataframe van de resultaten van de lineaire regressie tussen de kolommen x en y voor elke dataset

# %%
g = sns.FacetGrid(data, col="dataset", col_wrap=2, height=3, sharex=False, sharey=False)
g.map_dataframe(sns.scatterplot, x="x", y="y")
g.set_titles("Dataset: {col_name}")
g.fig.suptitle("Scatterplots per dataset", y=1.03)
plt.show()

# %%
sns.lmplot(data=data, x="x", y="y",col="dataset",col_wrap=2, height=3, ci=None, sharex=False, sharey=False)
plt.suptitle("Scatterplots met regressielijn per dataset", y=1.02)
plt.show()

# %%
#heeeee dit is aangepast!!!

a = 15
a = 3 
a = 139

#aangepast in 2e branche
a = 80
a = 15
a = 3
a = 139


