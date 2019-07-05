from bokeh.plotting import figure
from bokeh.io import show
from bokeh.io import output_file

x = [1, 3, 6, 2]
y = [4, 6, 1, 5]

# define layout scale
p = figure(plot_width=700, plot_height=400)
# pass the data to plot (line, scatter, bar, pie chart, ...)
p.line(x, y)

# # show plot in browser
# show(p)

# instead of those two lines, use output_file
output_file("bokeh1_outputhtml.html")
