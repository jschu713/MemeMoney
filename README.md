# MemeMoney

### <ins>Goal</ins>
This is a project created for the Spring 2021 BeaverHacks hackathon. 
The theme of the hackathon was FinTech and the scope was broad. This project
was created as a group consisting of [@jschu713](http://www.github.com/jsch713),
[@jennyxchang](http://www.github.com/jennyxchang), and 
[@vborder](http://www.github.com/vborder).

### <ins>Purpose</ins>
Not just for sharing moments with friends, family, and internet strangers, 
social media sites have begun to even influence financial markets. 
Meme stocks--stocks that have increased in value not due to performance, 
but social media hype--heavily favor early adopters who enter and exit 
at the right time. 

### <ins>How it works:</ins>

MemeMoney allows you to follow the hype around a stock.* It tracks the
number of mentions of stock ticker symbol on  two popular social media sites--
Reddit and Twitter for the past three days from
the current date, excluding weekends. It then creates a table displaying:

* the previous day's close price
* the number of mentions on Reddit
* the number of mentions on Twitter in English, excluding retweets
* the price differential from the previous day, and
* the mention differential from the previous day

### <ins>How to use it:</ins>

#### Opening
Run the GUI.py file.

#### Using
Then simply enter a stock ticker symbol (letters only) and 
the application will display the results.

An example execution:

![Alt Text](https://i.imgur.com/22DqaDf.jpg)


*Due to free API limitations, MemeMoney will
have a long runtime for more popular stocks due to API request timeouts.
Due to the same limitations, MemeMoney is also unable to track real time 
stock data and social media mentions.

