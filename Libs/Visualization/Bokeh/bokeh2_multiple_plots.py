from bokeh.plotting import figure
from bokeh.io import show

p = figure(plot_width=700,
           plot_height=400,
           title='Markers')

p.asterisk([1, 2, 3, 4, 5],
           [6, 7, 3, 4, 5],
           size=15,
           color='green')

p.diamond([1, 2, 3, 4, 5],
          [6, 7, 3, 4, 5],
          size=24,
          color='#EE02EE',
          angle=0.9)

p.square([1, 2, 3, 4, 5],
         [6, 7, 3, 4, 5],
         size=20,
         line_color='rgb(214, 0, 214)',
         fill_color='rgb(214, 214, 0)',
         line_width=2)

p.line([1, 2, 3, 4, 5],
       [6, 7, 3, 4, 5],
       line_width=4,
       alpha=0.6,
       color='red',
       line_dash='dashed')

p.step([1, 2, 3, 4, 5],
       [6, 7, 3, 4, 5],
       line_width=3,
       color='gold',
       mode='before')

p.multi_line([[1, 2, 3], [4, 5, 6, 7, 8]],
       [[3, 1, 4], [4, 7, 8, 10, 12]],
       line_width=[4, 2],
       alpha=[0.6, 2],
       color=['yellow', 'orange'],
       line_dash='dashed')

show(p)
