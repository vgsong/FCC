import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


pd.set_option('display.max_rows', None)

df = pd.read_csv('medical_foo.csv')
df['overweight'] = df['weight']/((df['height']/100)**2)
df['overweight'] = np.where(df['overweight'] > 25,1,0)

# df['cholesterol'] = np.where(df['cholesterol'] > 1,0,1)
# df['gluc'] = np.where(df['gluc'] > 1,0,1)
#
# #
# # print(df['cholesterol'].value_counts())
# # print(df['gluc'].value_counts())
#
# result_df = df.astype('int32')
#
# print(result_df)


# Debug area -------


# # print(df['overweight'])
# listKC = df['overweight'].value_counts().keys()
# listCount = df['overweight'].value_counts()
# listVC = df['overweight'].value_counts()


#
# print(listCount)
# print(listKC)
#
# print(type(listVC))

print(df.columns)
# print(df['gender'].value_counts())

# print(df[['ap_lo','ap_hi']])
# print(df['ap_hi'].value_counts())
filter_df = df[df['ap_lo'] <= df['ap_hi']]
filter2_df = df[df['height'] >= df['height'].quantile(0.025)]
filter3_df = df[df['height'] > df['height'].quantile(0.975)]
filter4_df = df[df['height'] < df['height'].quantile(0.025)]
filter5_df = df[df['height'] > df['height'].quantile(0.975)]


print(df.shape)
print(filter_df.shape)
print(filter5_df.shape)

print(filter2_df.shape)
print(np.unique(df['gender']))


# END of Debug area -------