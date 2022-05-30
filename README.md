# How does Super Bowl affect TV viewership and musician rating?

Whether or not you like football, the Super Bowl is a spectacle. There's drama in the form of blowouts, comebacks, and controversy in the games themselves. There are the ridiculously expensive ads, some hilarious, others gut-wrenching, thought-provoking, and weird. The half-time shows with the biggest musicians in the world, sometimes riding giant mechanical tigers or leaping from the roof of the stadium.



![image](https://user-images.githubusercontent.com/93321953/170988537-ff6fc914-4c8b-40a3-8125-0cfaccba5ab2.png)








In this project, we will find out how some of the elements of this show interact with each other. We will answer questions like:

• What are the most extreme game outcomes?

• How does the game affect television viewership?

• How have viewership, TV ratings, and ad cost evolved over time?

• Who are the most prolific musicians in terms of halftime show performances?



## The Data
The dataset we'll use was scraped and polished from Wikipedia. It is made up of three CSV files, one with game data, one with TV data, and one with halftime musician data for all 52 Super Bowls through 2018.
Using linear regression to predict who will win the game?

## Imports
• numpy, pandas, os, LabelEncoder, OneHotEncoder, statsmodels.ap, matplotlib.pyplot



## Preprocessing the Data
For the Super Bowl game data, we can see the dataset appears whole except for missing values in the backup quarterback columns, which make sense given most starting QBs in the Super Bowl play the entire game. The Super Bowl goes all the way back to 1967, and the more granular columns (e.g. the number of songs for halftime musicians) probably weren't tracked reliably over time. Wikipedia is great but not perfect.

For the TV data, the following columns have missing values and a lot of them:

• **total_us_viewers** (amount of U.S. viewers who watched at least some part of the broadcast)

•  **rating_18_49**  (average % of U.S. adults 18-49 who live in a household with a TV that were watching for the entire broadcast)

• **share_18_49** (average % of U.S. adults 18-49 who live in a household with a TV in use that were watching for the entire broadcast)

For the halftime musician data, there are missing numbers of songs performed (num_songs) for about a third of the performances.
Though it would be nice to have this data, the effort to fetch this data and incorporate into the dataset is too much and the insights obtained do not seen worth it, since most of the missing data is historical data of the 90s.

## The costly halftime shows. Are they worth it?
Plotitng a time-graph, we see that the viewers increased before ad costs did. Maybe the networks weren't very data savvy and were slow to react?

It turns out Michael Jackson's Super Bowl XXVII performance, one of the most watched events in American TV history, was when the NFL realized the value of Super Bowl airtime and decided they needed to sign big name acts from then on out. The halftime shows before MJ indeed weren't that impressive, which we can see by filtering our halftime_musician data.

## Who performed the most songs in a halftime show?
The world famous Grambling State University Tiger Marching Band takes the crown with six appearances. Beyoncé, Justin Timberlake, Nelly, and Bruno Mars are the only post-Y2K musicians with multiple appearances (two each).







### Conclusion

So most non-band musicians do 1-3 songs per halftime show. It's important to note that the duration of the halftime show is fixed (roughly 12 minutes) so songs per performance is more a measure of how many hit songs you have. JT went off in 2018, wow. 11 songs! Diana Ross comes in second with 10 in her medley in 1996.

In this project, we loaded, cleaned, then explored Super Bowl game, television, and halftime show data. We visualized the distributions of combined points, point differences, and halftime show performances using histograms. We used line plots to see how ad cost increases lagged behind viewership increases. And we discovered that blowouts do appear to lead to a drop in viewers!
