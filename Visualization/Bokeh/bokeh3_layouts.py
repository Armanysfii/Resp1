from bokeh.plotting import figure
from bokeh.io import show
from bokeh.layouts import gridplot
from bokeh.layouts import layout

# first line plot
p1 = figure(plot_width=300,
            plot_height=150,
            title='first')

p1.line([1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        color='blue')

# second line plot
p2 = figure(plot_width=300,
            plot_height=150,
            title='second')

p2.line([6, 7, 8, 9, 10],
        [1, 2, 3, 4, 5],
        color='green')

# third line plot
p3 = figure(plot_width=300,
            plot_height=150,
            title='second')

p3.line([6, 7, 3, 11, 10],
        [1, 2, 3, 2, 5],
        color='red')

# pass 3 objects of plots to a grid layout
grid = gridplot([[p1, p2], [p3]])

# # [0,0]: !null     [0,1]: !null       *[1,0]: null*       [1,1]:!null
# grid = gridplot([[p1, p2], [None, p3]])

# # span fits for a single column plot row
# doc = layout([[p1, p2], [p3]], sizing_mode='scale_width')

# pass the layout to show method instead plots
show(grid)
