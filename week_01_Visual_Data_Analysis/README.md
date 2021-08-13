## Income and Life Expectancy of the Nations of the World - Correlation or Causation?
### 200 Countries over the last 220 years and a prognosis 20 years into the future 



![animated_scatteplot](animated_scatterplot.gif)




The idea was inspried by [Hans Rosling's presentation in 2010 on BBC Four](https://www.youtube.com/watch?v=jbkSRLYSojo "go to presentation"). The chart was generated with free data from World Bank via [GAPMINDER.ORG](https://www.gapminder.org/data/ "go to page"), CC-BY LICENSE.

Thanks to the simplicity and interactivity of plotly express the plot could be generated with only two lines of code:

`fig = px.scatter(df_all, x="income", y="life_expectancy", animation_frame="year", animation_group="country", size="population", color="continent",hover_name="country", log_x = True, size_max=50, range_x=[100,100000], range_y=[25,90])`

`fig.show()`

The only requirement was to organize the data in the right shape by utilizing different data wrangling techniques which can be observed in the [jupyter notebook](200_Countries_240_Years.ipynb "go to notebook").




