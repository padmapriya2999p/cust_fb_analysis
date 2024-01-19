#####  To find the overall average of a hotel rating by adding all the rating, food_rating and service rating #####

# for data manupulation
import pandas as pd 

#path1 = 'E:/BA PROJECTS/Customer_feedback_analysis_jan_2024/archive/chefmozaccepts.csv'
#df1=pd.read_csv(path1)

# creating dataframe from csv file
df2=pd.read_csv(r'E:\BA PROJECTS\Customer_feedback_analysis_jan_2024\archive\rating_final.csv')

'''print(df1.head(2))
print(df2.head(2))

print(len(df1))
print(len(df2))'''

# to get the column headings
#print(df1.columns)
print(df2.columns)

# to find the total row wise
total = df2[['rating','food_rating','service_rating']].sum(axis=1)
#print(total)

# to add all the rating from user
overall_total=0
for i in total:
    overall_total+=i
print('The over all total of rating:', overall_total)

# getting the overall rating avg 
avg = overall_total/len(df2)
print('The average rating:', avg)

print(" draft me my ... will do the rest tmrw")

#print(df2.describe())
