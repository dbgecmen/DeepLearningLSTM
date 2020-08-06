from apscheduler.schedulers.blocking import BlockingScheduler
from pytrends.request import TrendReq


def GetTrends():
	pytrend = TrendReq()
	kw_list = ['bitcoin']

	pytrend.build_payload(kw_list, timeframe='now 1-H')
	interest_over_time_df =  pytrend.interest_over_time()
	print(interest_over_time_df.head())
	with open('googletrends.csv', 'a') as f:
		interest_over_time_df.to_csv(f,mode='a', header=False)


GetTrends()
scheduler = BlockingScheduler()
scheduler.add_job(GetTrends, 'interval', hours=1)
scheduler.start()


