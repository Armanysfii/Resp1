import pandas as pd
import numpy as np

arr = np.array([[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]])
df_withArray = pd.DataFrame(arr, index=['row1', 'row2', 'row3', 'row4']
                            , columns=['col1', 'col2', 'col3', 'col4'])
print(df_withArray)

dict = {'col1': [1, 2, 3, 4],
        'col2': [5, 6, 7, 8],
        'col3': [1, 2, 3, 4],
        'col4': [1, 2, 3, 4]}
df_withDict = pd.DataFrame(dict, index=['row1', 'row2', 'row3', 'row4']
                           , columns=['col1', 'col2', 'col3', 'col4'])
print(df_withArray)

# df_withArray.index
# df_withArray.columns
# df_withArray.values


# selecting
df_withArray.loc['row1'][:]  # all
df_withArray.loc['row1']['col2']

df_withArray.iloc[0][:]  # all
df_withArray.iloc[0][2]  # row1 col2

# editing
df_withDict.loc[['row1', 'row2'], 'col1'] = 0

# reset index
df_withDict.reset_index(drop=True)

# delete
df_withDict.drop('col2', axis=1)  # ruye sutun ha donbale col5 begard

# renaming
df_withDict.rename(columns={'col4': 'columns4'})

# replacing
df_withDict.replace({0: 1})

# apply function on index
df_withDict.col2 = ['{:.2f}'.format(x) for x in df_withDict.iloc[:, 0]]
# or
df_withDict['col2'] = df_withDict['col2'].apply(lambda x: '{:.2f}'.format(x))

# SORTING

df_withDict.sort_index(axis=1, ascending=False)  # axis sutun haro nozuli ya su'udi miare
df_withDict.sort_values(by='col2', ascending=True)

# Most useful methods
df_withArray.head(2)  # 5 is default value for big dataFrames
df_withArray.tail(2)

