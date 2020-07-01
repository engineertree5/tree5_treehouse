# Strategy Learnings - EMA (Exponential Moving Average)
Let me start by saying I'm looking to get a full understanding (pros, cons, key points, formula, etc) of eeach strategy before I move on to the next strategy. If you read the title of this post you can see that I'll be discussing EMA's and what I learned. Through my learnings understood that EMA's `hold a greater weight to recent data`. Previously I was charting Simple moving averages which are not as quick to respond as EMA's. 

On to the most important piece of any analysis, the formula! To properly chart the passo do so you will actually need the SMA to pull the weighted/weighting multiplier. 

'''python

Multiplier: (2 / (Time periods + 1) ) 
EMA: {Close - EMA(previous day)} x multiplier + EMA(previous day). 
Here Time period is the number of days you want to look back.

'''
