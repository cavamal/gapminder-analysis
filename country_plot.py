import pandas as pd
import matplotlib.pyplot as plt

def country_plot(country):

	df_life = pd.read_csv('data/life_norm.csv')
	df_tax = pd.read_csv('data/tax_norm.csv')
	df_gdp = pd.read_csv('data/gdp_norm.csv')
	df_pov = pd.read_csv('data/poverty_norm.csv')
	df_su = pd.read_csv('data/suicide_norm.csv')

	fig = plt.figure(figsize=(10,5))
	ax1 = fig.add_subplot(111)

	#some countries are not represented and need to not graph if they don't exist
	if country in df_life.index:
	    ax1.scatter(df_life.columns.tolist(),df_life.loc[country],s=10, c='k', marker="<", label = 'Life Exepctancy')
	    
	if country in df_tax.index:
	    ax1.scatter(df_tax.columns.tolist(),df_tax.loc[country],s=10, c='b',marker ="x", label = '% Tax Revenue GDP per Capita')
	    
	if country in df_gdp.index:
	    ax1.scatter(df_gdp.columns.tolist(), df_gdp.loc[country],s=10, c='g', marker="o", label = 'GDP/Capita')
	    
	if country in df_pov.index:
	    ax1.scatter(df_pov.columns.tolist(), df_pov.loc[country],s=10, c='r', marker=",", label = '% of People Living Under National Poverty Markers')

	if country in df_su.index:
	    ax1.scatter(df_su.columns.tolist(), df_su.loc[country],s=10, c='m', marker=">", label = 'Suicide Rates per 100,000 People')

	plt.ylim(0,1)
	plt.xticks(rotation=70)
	plt.xlabel('Year and Mean')
	plt.ylabel('Relative Proportion Compared\n to Maximum and Minimum Values')

	plt.legend(loc='center left', bbox_to_anchor = (1,0.5));
	plt.show()