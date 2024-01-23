#####  To find the overall average of a hotel rating by adding all the rating, food_rating and service rating #####

# for data manupulation
import pandas as pd 

path1 = 'E:/BA PROJECTS/Customer_feedback_analysis_jan_2024/archive/chefmozaccepts.csv'
df1=pd.read_csv(path1)

# creating dataframe from csv file
df2=pd.read_csv(r'E:\BA PROJECTS\Customer_feedback_analysis_jan_2024\archive\rating_final.csv')

'''print(df1.head(2))
print(df2.head(2))

print(len(df1))
print(len(df2))'''

''''# to get the column headings
print(df1.columns)
print(df2.columns)'''

df3=pd.merge(df1,df2,on='placeID')

# to find the total row wise

print(df3)
df3['total'] = df3[['rating','food_rating','service_rating']].sum(axis=1)
#print(df3.head(10))

# covert the total into df and then grp by using rpayment then use mean 
res=df3.groupby('Rpayment')['total'].mean()
print('The average rating:', res) 

#print(df3.columns)
#print(df3.describe())
