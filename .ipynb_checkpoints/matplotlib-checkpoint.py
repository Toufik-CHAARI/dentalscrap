from pytrends.request import TrendReq
import matplotlib.pyplot as plt 

pytrends = TrendReq(hl='en-US')
keywords = ['Kavo', 'NSK','Sirona', 'Adec']
pytrends.build_payload(keywords, timeframe='today 5-y')
data = pytrends.interest_over_time()

#plt.plot(data)
#plt.show()
