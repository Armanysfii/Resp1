import pandas as pd

mySeries = pd.Series([1, 4, 6, 8],
                     index=['row1', 'row2', 'row3', 'row4'])
print(mySeries)

print(mySeries.values)
print(mySeries.index)

# index name must be same as the string that you defined
print(mySeries['row2'])
print(mySeries.row2)

print(mySeries[mySeries>5])

mySeries.index = ['first', 'second', 'third', 'fourth']
print(mySeries)
