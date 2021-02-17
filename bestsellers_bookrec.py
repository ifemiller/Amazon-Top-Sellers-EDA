import pandas as pd
import time
#Load in data
topsellers_datta = pd.read_csv('https://github.com/ifemiller/Amazon-Top-Sellers-EDA/blob/main/bestsellers%20with%20categories.csv')

#Create a copy
Recommenddf = topsellers_data.copy()

#Make a ratings list
Ratings= []
for rating in testdf['User Rating']:
    if rating >3 and rating <=3.5:
        Ratings.append('Okay')
    elif rating > 3.6 and rating <=4:
        Ratings.append('Good')
    elif rating > 4.1 and rating <=4.5:
        Ratings.append('Great')
    else:
        Ratings.append('Excellent')
#Convert the ratings to a series
Ratings = pd.Series(Ratings)

#Concatenate the dataframe
Recommenddf = pd.concat([Recommenddf, Ratings], axis = 1)
#Renaming a column
Recommenddf = Recommenddf.rename(columns = {0: 'Ratings'})

#Creating dfs for each rating
Okaybooks = Recommenddf[Recommenddf['Ratings']== 'Okay'][['Name','Author']]
Goodbooks = Recommenddf[Recommenddf['Ratings']== 'Good'][['Name','Author']]
Greatbooks = Recommenddf[Recommenddf['Ratings']== 'Great'][['Name','Author']]
Excellentbooks = Recommenddf[Recommenddf['Ratings']== 'Excellent'][['Name','Author']]

#Recommender Function. Basically asks user for inputs and then recommends a book from that specific rating group
def getbookreq():
    bookreq = input("Would you like an 'Okay', 'Good', 'Great' or 'Excellent' \nbook rec?\n")

    if bookreq == 'Okay':
        thebook = pd.DataFrame(Okaybooks.sample())
        print("There's only 1!")
        time.sleep(3)
        print('Try: {} by {}'.format(thebook['Name'].iloc[0],thebook['Author'].iloc[0]))

    elif bookreq == 'Good':

        thebook = pd.DataFrame(Goodbooks.sample())
        print('Picking from {} Good books!'.format(len(Goodbooks)))
        time.sleep(3)
        print('Try: {} by {}'.format(thebook['Name'].iloc[0],thebook['Author'].iloc[0]))

    elif bookreq == 'Great':

        thebook = pd.DataFrame(Greatbooks.sample())
        print('Picking from {} Great books!'.format(len(Greatbooks)))
        time.sleep(3)
        print('Try: {} by {}'.format(thebook['Name'].iloc[0],thebook['Author'].iloc[0]))

    elif bookreq == 'Excellent':

        thebook = pd.DataFrame(Excellentbooks.sample())
        print('Picking from {} Excellent books!'. format(len(Excellentbooks)))
        time.sleep(3)
        print('Try: {} by {}'.format(thebook['Name'].iloc[0],thebook['Author'].iloc[0]))

    else:
        print("Please enter 'Okay', 'Good', 'Great' or 'Excellent'")

    goodchoice = input('Have you read this book already? [y/n] \n')
    if goodchoice == 'y':
        print("Oh no! Pick another then!")
        time.sleep(2)
        getbookreq()

    else:
        print('Great! Happy Reading!')

getbookreq()
