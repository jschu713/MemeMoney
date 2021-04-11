# MemeMoney
This is a project created for the Spring 2021 BeaverHacks hackathon. 
The theme of the hackathon was FinTech and the scope was broad. 

Not just for sharing moments with friends, family, and internet strangers, 
social media sites have begun to even influence financial markets. 
Meme stocks--stocks that have increased in value not due to performance, 
but social media hype--heavily favor early adopters who enter and exit 
at the right time. 

MemeMoney allows you to follow the hype around a stock.* It tracks the
number of mentions of stock ticker symbol on  two popular social media sites--
Reddit and Twitter for the past three days from
the current date, excluding weekends. It then creates a table displaying:

* the previous day's close price
* the number of mentions on Reddit
* the number of mentions on Twitter in English, excluding retweets
* the price differential from the previous day, and
* the mention differential from the previous day

Simply enter a stock ticker symbol (letters only) and MemeMoney will display
the results. 

![Alt Text](https://i.imgur.com/22DqaDf.jpg)


*Due to free API limitations, MemeMoney is unable to track realtime stock data
and social media mentions.
