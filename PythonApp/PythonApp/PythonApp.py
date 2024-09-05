import yfinance as yf
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid')
ticker_list = ['PTT.BK','PTTEP.BK','PTTGC.BK','TOP.BK']

data_df = pd.DataFrame()
for i in range(0,len(ticker_list)):
    ticker = ticker_list[i]
    df_yahoo = yf.download(ticker,  start='2000-01-01',  end='2023-12-31', progress=True) #download the data
    data_df = pd.concat([data_df, df_yahoo['Adj Close']],axis=1) #store data in one dataframe      

data_df.columns = ticker_list #change columns to ticker name
data_df.index = pd.to_datetime(data_df.index, format='%y%m%d') #set index as datetime
data_df['2015':].plot(figsize=(12,6))
plt.legend(loc='upper left') 
(data_df['2015':].pct_change()+1).cumprod().plot(figsize=(12,6))
plt.ylabel('Growth of hypothetical 1 Bt.')
plt.savefig('CumRet_since2015.png') 

plt.show()