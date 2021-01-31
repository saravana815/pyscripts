import pandas as pd
import numpy as np
import jinja2

# Sample DataFrame
# df = pd.DataFrame(np.random.randn(5, 4), columns=['one', 'two', 'three', 'four'],
#                   index=['a', 'b', 'c', 'd', 'e'])

data = [['Geeks', 10], ['for', 15], ['geeks', 20]]
df = pd.DataFrame(data, columns = ['Name', 'Age'])

# See: https://pandas.pydata.org/pandas-docs/stable/user_guide/style.html#Building-styles
def color_negative_red(val):
    # color = 'red' if val < 0 else 'black'
    color = 'red'
    return f'color: {color}'

styler = df.style.applymap(color_negative_red)

# Template handling
env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath=''))
template = env.get_template('template.html')
html = template.render(my_table=styler.render())
# html = template.render()

# Plot
ax = df.plot.bar()
fig = ax.get_figure()
fig.savefig('plot.svg')

# Write the HTML file
with open('report.html', 'w') as f:
    f.write(html)
