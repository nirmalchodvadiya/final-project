import pandas as pdLib1
data = pdLib1.read_csv("TV_Shows.csv")

df = pdLib1.DataFrame(data)
print(df)

import sqlite3
connection = sqlite3.connect("ottData.db")
myCursor = connection.cursor()
query = "create table ottData (title word, year word, age word, imdb double, rotten_tomatoes word, netflix word, hulu word, prime_video word, disney_plus word)"
myCursor.execute(query)

for index, row in df.iterrows():
    insertQuery = "insert into ottData values (?,?,?,?,?,?,?,?,?)"
    myCursor.execute(insertQuery,(row['Title'],row['Year'],row['Age'],row['IMDb'],row['Rotten Tomatoes'],row['Netflix'],row['Hulu'],row['Prime Video'],row['Disney+']))   

query = "select * from ottData"
myCursor.execute(query)
myCursor.fetchall()

import matplotlib.pyplot as plt

yearData = df[(df.Year >= 2000) & (df.Year <= 2020)]
# print(yearData)

netflixShows = df[(df['Netflix'] == 1)]
print(len(netflixShows.index))

primevideoShows = df[(df['Prime Video'] == 1)]
print(len(primevideoShows.index))

huluShows = df[(df['Hulu'] == 1)]
print(len(huluShows.index))

disneyplusShows = df[(df['Disney+'] == 1)]
print(len(disneyplusShows.index))

plt.plot(df.Year,df.Title)
plt.xlabel("Years")
plt.ylabel("Title")
plt.title("Numbers of TV Shows Titles")
plt.savefig("bestPlatform.png")
plt.show()

plt.bar(df.Age,df['Age'].count())
plt.xlabel("Age Groups")
plt.ylabel("Count of Ages")
plt.title("Different Age Groups")
plt.savefig("ageGroup.png")
plt.show()

plt.barh(df.Title,df['Netflix'])
plt.xlabel("TV Shows")
plt.ylabel("TV Shows on Prime Video")
plt.title("Number of TV Shows available on Prime Video")
plt.savefig("primeVideoShows.png")
plt.show()