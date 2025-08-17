# import pandas as pan
# import regex

# df=pan.read_csv("dataset.csv")



# # document=df['content_column'] .astype(str).tolist()


# #print(df['Gender'])

# #read row

# #print(df.iloc[2])


# #Read row data as whole

# # for index,row in df.iterrows():
# #     print(index,row['Gender'])

# # df.loc[df['Gender']=='Male']

# # print(df.describe())

# # cols=list(df.columns.values)

# # print(cols[0:13]) # print 12 columns after converting them to list


# # df=df[cols[0:13]]
# # print(df)

# #Filtering the data
# # filtered_df = df.loc[(df['Workout_Frequency (days/week)'] == 4.0) & (df['Height (m)' ]>= 1.70)]
# # print(filtered_df)

# # #saving the data in new csv file
# # filtered_df.to_csv('filtered data.csv')

# #now using string methods to store and filter data
# #
# # str_filtered_data=df.loc[df['Gender'].str.contains('Fe',na=False)]

# # print(str_filtered_data)

# #regex filtering

# # regex_filtering=df.loc[df['Gender'].str.contains('Fe|fem',regex=True,na=False)]

# # print(regex_filtering)
# # regex_filtering=df.loc[df['Gender'].str.contains('Fe[a-z]*',regex=True,na=False)]

# # print(regex_filtering)


# moddf=pan.read_csv("filtered data.csv")

# modf=moddf.loc[moddf['Gender']=='Female','Gender']='Workers'

# print(moddf)


# aggreg=moddf.groupby(['Gender']).mean(numeric_only=True).sort_values('Workout_Frequency (days/week)',ascending=False)

# print(aggreg)


# #chunking

# for data in pan.read_csv('filtered data.csv',chunksize=10):
#     print("Chunk")
#     print(data)



