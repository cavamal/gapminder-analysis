import pandas as pd
import matplotlib.pyplot as plt

def country_plot(country):

	fig = plt.figure(figsize=(10,10))
	ax1 = fig.add_subplot(111)


	ax1.scatter(df_life.columns.tolist(),df_life.loc[country],s=10, c='k', marker="<", label = 'Life Exepctancy')
	ax1.scatter(df_tax.columns.tolist(),df_tax.loc[country],s=10, c='b',marker ="x", label = '% Revenue GDP')
	ax1.scatter(df_gdp.columns.tolist(), df_gdp.loc[country],s=10, c='g', marker="o", label = 'GDP/Capita')
	ax1.scatter(df_pov.columns.tolist(), df_pov.loc[country],s=10, c='r', marker=",", label = '% of People Living Under National Poverty Markers')

	plt.xticks(rotation=70)
	plt.xlabel('Year')
	plt.ylabel('Percentage Relative to Max and Mins ')

	plt.legend(loc='best');
	plt.show()