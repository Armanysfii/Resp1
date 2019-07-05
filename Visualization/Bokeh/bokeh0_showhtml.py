from bokeh.plotting import figure
from bokeh.io import show

x = [1, 3, 6, 2]
y = [4, 6, 1, 5]

# define layout scale
p = figure(plot_width=700, plot_height=400)
# pass the data to plot (line, scatter, bar, pie chart, ...)
p.line(x, y)
# show plot in browser
show(p)
