from xml.parsers import expat

import pandas as pd


df = pd.read_csv("Titanic-Dataset.xls")


# Խնդիր 1.1: Գտիր, թե որ սյուներում կան բաց թողնված (NaN) արժեքներ և քանի հատ:
#
# Խնդիր 1.2: Age (Տարիք) սյան բաց թողնված արժեքները լրացրու տվյալ սեռի (Sex) և տոմսի դասի (Pclass) միջին տարիքով (կամ մեդիանով):
#
# Խնդիր 1.3: Embarked սյան բաց թողնված 2 արժեքները լրացրու ամենահաճախ հանդիպող (mode) նավահանգստով:
#
# Խնդիր 1.4: Cabin սյունը ունի չափազանց շատ բաց թողնված արժեքներ. հեռացրու այդ սյունը dataset-ից:


#1.1
# print(df.info())

#1.2
# age_median = df.groupby(['Sex','Pclass'])['Age'].transform('median')
# df['Age'] = df['Age'].fillna(age_median)
# # print(age_median)
#
# #1.3
# pop_embarked = df['Embarked'].mode()[0]
# df['Embarked'] = df['Embarked'].fillna(pop_embarked)
# # print(df.info())
# # print(pop_embarked)
# df = df.drop(columns='Cabin')
# print(df.shape)


# Խնդիր 2.1: Հաշվիր, թե ուղևորների քանի տոկոսն է ողջ մնացել (Survived == 1):
#
# Խնդիր 2.2: Գտիր ողջ մնալու տոկոսը՝ ըստ սեռի (Sex) և ըստ տոմսի դասի (Pclass):

#2.1
# df_surv = df[ df['Survived'] == 1 ]
# print(df_surv.shape[0]/891*100)

#2.2
# print( df.groupby(['Sex', 'Pclass'])['Survived'].mean()*100  )

# Խնդիր 2.3: Գտիր ամենաթանկ տոմսով ճանապարհորդած 5 ուղևորներին:
#
# Խնդիր 2.4: Քանի՞ հոգի են ճանապարհորդել մենակ (առանց ընտանիքի անդամների, այսինքն՝ SibSp == 0 և Parch == 0):


#2.3

# Fare_df = df.sort_values(
#     by= "Fare",
#     ascending=False
# ).head(9)
# print(Fare_df[['Name','Fare']])

#
# alone_people = df[ (df['SibSp'] == 0) & (df["Parch"] == 0) ]
# print(alone_people.shape[0])


# Խնդիր 3.1 (FamilySize): Ստեղծիր FamilySize սյունը, որը ցույց կտա ընտանիքի անդամների ընդհանուր քանակը (SibSp + Parch + 1):
#
# Խնդիր 3.2 (IsAlone): Ստեղծիր IsAlone սյունը (1՝ եթե մենակ է, 0՝ եթե ընտանիքով է):
#
# Խնդիր 3.3 (Title): Name սյունից առանձնացրու մարդկանց կոչումները (օրինակ՝ Mr, Mrs, Miss, Master, Dr) և ստեղծիր նոր Title սյուն:
#
# Խնդիր 3.4 (AgeGroup): Age սյունը բաժանիր տարիքային խմբերի (օրինակ՝ Child [0-12], Teenager [12-18], Adult [18-60], Senior [60+]):

#3.1

# df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
# print(df['FamilySize'])
#3.2
# df["IsAlone"] =  ((df['SibSp'] == 0)  & (df['Parch'] == 0)).astype(int)
# print(df['IsAlone'])

# #3.3
# df['Title'] = df['Name'].str.extract(r' ([A-Za-z]+)\.', expand = False)
# print(df['Title'])
# df['SurName'] = df['Name'].str.split(',').str[0]
# # print(df['SurName'])
# print(df['SurName'].value_counts().head(12))


# x = [0,12,18,60,100]
# y = ['Child','Teenager','Adult','Senior']
# df['AgeGroup'] = pd.cut(df['Age'], bins = x, labels = y)
# print(df['AgeGroup'].value_counts().head(5))


