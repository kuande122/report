import streamlit as st
import pandas as pd               # 資料處理套件
import matplotlib.pyplot as plt   # 資料視覺化套件
import xlrd
from PIL import Image
st.set_page_config(
    page_title="猛祺的期末報告",
    page_icon='phil.ico'
    )
st.title('中華職棒數據查詢系統')
st.sidebar.header('選擇球隊及數據')
option = st.sidebar.selectbox( '選擇球隊？', ['中信兄弟', '統一7-Eleven獅', '味全龍', '樂天桃猿','富邦悍將'])
option1 = st.sidebar.selectbox( '選擇所想查看的數據？', ['球隊成績', '投手成績', '打擊成績', '守備成績'])

#讀取數據庫
BrothersPitching=pd.read_excel('BrothersPitching.xlsx')
UnilionsPitching=pd.read_excel('UnilionsPitching.xlsx')
DragonsPitching=pd.read_excel('DragonsPitching.xlsx')
RakutenPitching=pd.read_excel('RakutenPitching.xlsx')
GuardiansPitching=pd.read_excel('GuardiansPitching.xlsx')
BrothersBatting=pd.read_excel('BrothersBatting.xlsx')
UnilionsBatting=pd.read_excel('UnilionsBatting.xlsx')
DragonsBatting=pd.read_excel('DragonsBatting.xlsx')
RakutenBatting=pd.read_excel('RakutenBatting.xlsx')
GardiansBatting=pd.read_excel('GuardiansBatting.xlsx')
BrothersDefense=pd.read_excel('BrothersDefense.xlsx')
UnilionsDefense=pd.read_excel('UnilionsDefense.xlsx')
DragonsDefense=pd.read_excel('DragonsDefense.xlsx')
RakutenDefense=pd.read_excel('RakutenDefense.xlsx')
GuardiansDefense=pd.read_excel('GuardiansDefense.xlsx')
Brothers=pd.read_excel('Brothers.xlsx')
Unilions=pd.read_excel('Unilions.xlsx')


if option == '中信兄弟':
  image = Image.open('brothers.png')
  st.image(image)
    
  if option1=='球隊成績':
    st.header('球隊成績')
    st.write(Brothers) 

  elif option1=='投手成績':
    st.header('投手成績')
    st.write(BrothersPitching)
    st.header('數據分析')
    plt.style.use("ggplot")
    plt.plot(BrothersPitching.年度, BrothersPitching.防禦率,'.-' ,color='yellow')
    plt.plot(UnilionsPitching.年度, UnilionsPitching.防禦率,'.-' ,color='darkorange')
    plt.plot(DragonsPitching.年度, DragonsPitching.防禦率, '.-',color='red')
    plt.plot(GuardiansPitching.年度, GuardiansPitching.防禦率,'.-', color='darkblue')
    plt.plot(RakutenPitching.年度, RakutenPitching.防禦率,'.-', color='maroon')
    plt.xlabel('Season') # 設定x軸標題
    plt.xticks([2021,2020,2019,2018,2017,2016,2015,2014])
    plt.xticks(BrothersPitching.年度) # 設定x軸
    plt.xticks(UnilionsPitching.年度) 
    plt.xticks(RakutenPitching.年度) 
    plt.xticks(GuardiansPitching.年度)
    plt.xticks(DragonsPitching.年度) 
    plt.title('CTBC Brothers Pitching ERA VS Other Teams ') # 設定圖表標題
    plt.legend(labels=["BrothersPitching", "UnilionsPitching","DragonsPitching","GuardiansPitching","RakutenPitching"], loc = 'best')
    st.pyplot(plt) 
    
      
    
  elif option1=='打擊成績':
    st.header('打擊成績')
    st.write(BrothersBatting)
    st.header('數據分析')
    plt.style.use("ggplot") 
    plt.plot(BrothersBatting.年度, BrothersBatting.打擊率,'.-', color='yellow')
    plt.plot(UnilionsBatting.年度, UnilionsBatting.打擊率,'.-', color='darkorange')
    plt.plot(DragonsBatting.年度, DragonsBatting.打擊率, '.-',color='red')
    plt.plot(GuardiansBatting.年度, GuardiansBatting.打擊率,'.-', color='darkblue')
    plt.plot(RakutenBatting.年度, RakutenBatting.打擊率, '.-',color='maroon')
    plt.xlabel('Season') # 設定x軸標題
    plt.xticks([2021,2020,2019,2018,2017,2016,2015,2014])
    plt.xticks(BrothersBatting.年度) # 設定x軸label以及垂直顯示
    plt.xticks(UnilionsBatting.年度) 
    plt.xticks(RakutenBatting.年度) 
    plt.xticks(GuardiansBatting.年度) 
    plt.xticks(DragonsBatting.年度) 
    plt.title('CTBC Brothers Batting Avg VS Other Teams ') # 設定圖表標題
    plt.legend(labels=["BrothersBatting", "UnilionsBatting","DragonsBatting","GuardiansBatting","RakutenBatting"], loc = 'best')
    st.pyplot(plt)
    
    plt.style.use("ggplot")
    plt.plot(BrothersBatting.年度, BrothersBatting.上壘率,'.-', color='yellow')
    plt.plot(UnilionsBatting.年度, UnilionsBatting.上壘率,'.-', color='darkorange')
    plt.plot(DragonsBatting.年度, DragonsBatting.上壘率, '.-',color='red')
    plt.plot(GuardiansBatting.年度, GuardiansBatting.上壘率,'.-', color='darkblue')
    plt.plot(RakutenBatting.年度, RakutenBatting.上壘率, '.-',color='maroon')
    plt.xlabel('Season') # 設定x軸標題
    plt.xticks([2021,2020,2019,2018,2017,2016,2015,2014])
    plt.xticks(BrothersBatting.年度) # 設定x軸label以及垂直顯示
    plt.xticks(UnilionsBatting.年度) 
    plt.xticks(RakutenBatting.年度) 
    plt.xticks(GuardiansBatting.年度) 
    plt.xticks(DragonsBatting.年度) 
    plt.title('CTBC Brothers Batting OBP VS Other Teams ') # 設定圖表標題
    plt.legend(labels=["BrothersBatting", "UnilionsBatting","DragonsBatting","GuardiansBatting","RakutenBatting"], loc = 'best')
    st.pyplot(plt)
    
    plt.style.use("ggplot")
    plt.plot(BrothersBatting.年度, BrothersBatting.長打率,'.-', color='yellow')
    plt.plot(UnilionsBatting.年度, UnilionsBatting.長打率,'.-', color='darkorange')
    plt.plot(DragonsBatting.年度, DragonsBatting.長打率, '.-',color='red')
    plt.plot(GuardiansBatting.年度, GuardiansBatting.長打率,'.-', color='darkblue')
    plt.plot(RakutenBatting.年度, RakutenBatting.長打率, '.-',color='maroon')
    plt.xlabel('Season') # 設定x軸標題
    plt.xticks([2021,2020,2019,2018,2017,2016,2015,2014])
    plt.xticks(BrothersBatting.年度) # 設定x軸label以及垂直顯示
    plt.xticks(UnilionsBatting.年度) 
    plt.xticks(RakutenBatting.年度) 
    plt.xticks(GuardiansBatting.年度) 
    plt.xticks(DragonsBatting.年度) 
    plt.title('CTBC Brothers Batting SLG VS Other Teams ') # 設定圖表標題
    plt.legend(labels=["BrothersBatting", "UnilionsBatting","DragonsBatting","GuardiansBatting","RakutenBatting"], loc = 'best')
    st.pyplot(plt)
    
    
  else:
    st.header('守備成績')
    st.write(BrothersDefense)
    st.header('數據分析')
    plt.style.use("ggplot")
    plt.plot(BrothersDefense.年度, BrothersDefense.守備率,'.-' ,color='yellow')
    plt.plot(UnilionsDefense.年度, UnilionsDefense.守備率,'.-' ,color='darkorange')
    plt.plot(DragonsDefense.年度, DragonsDefense.守備率, '.-',color='red')
    plt.plot(GuardiansDefense.年度, GuardiansDefense.守備率,'.-', color='darkblue')
    plt.plot(RakutenDefense.年度, RakutenDefense.守備率,'.-', color='maroon')
    plt.xlabel('Season') # 設定x軸標題
    plt.xticks([2021,2020,2019,2018,2017,2016,2015,2014])
    plt.xticks(BrothersDefense.年度) # 設定x軸
    plt.xticks(UnilionsDefense.年度) 
    plt.xticks(RakutenDefense.年度) 
    plt.xticks(GuardiansDefense.年度)
    plt.xticks(DragonsDefense.年度) 
    plt.title('CTBC Brothers Defense FPCT  VS Other Teams ') # 設定圖表標題
    plt.legend(labels=["BrothersDefense", "UnilionsDefense","DragonsDefense","GuardiansDefense","RakutenDefense"], loc = 'best')
    st.pyplot(plt) 
    
    
elif option == '統一7-Eleven獅':
  image = Image.open('unilion.png')
  st.image(image)
  if option1=='球隊成績':
    st.header('球隊成績')
    st.write(Unilions)    
  elif option1=='投手成績':
    st.header('投手成績')
    st.write(UnilionsPitching)
    st.header('數據分析')
    plt.style.use("ggplot")
    plt.plot(BrothersPitching.年度, BrothersPitching.防禦率,'.-', color='yellow')
    plt.plot(UnilionsPitching.年度, UnilionsPitching.防禦率,'.-', color='darkorange')
    plt.plot(DragonsPitching.年度, DragonsPitching.防禦率,'.-', color='red')
    plt.plot(GuardiansPitching.年度, GuardiansPitching.防禦率,'.-', color='darkblue')
    plt.plot(RakutenPitching.年度, RakutenPitching.防禦率,'.-', color='maroon')
    plt.xlabel('Season') # 設定x軸標題
    plt.xticks([2021,2020,2019,2018,2017,2016,2015,2014])
    plt.xticks(BrothersPitching.年度) 
    plt.xticks(UnilionsPitching.年度) 
    plt.xticks(RakutenPitching.年度) 
    plt.xticks(GuardiansPitching.年度) 
    plt.xticks(DragonsPitching.年度) 
    plt.title('Unilions Pitching ERA VS Other Teams ') # 設定圖表標題
    plt.legend(labels=["BrothersPitching", "UnilionsPitching","DragonsPitching","GuardiansPitching","RakutenPitching"], loc = 'best')
    st.pyplot(plt)                
  elif option1=='打擊成績':
    st.header('打擊成績')
    st.write(UnilionsBatting) 
    st.header('數據分析')
    plt.style.use("ggplot")
    plt.plot(BrothersBatting.年度, BrothersBatting.打擊率,'.-', color='yellow')
    plt.plot(UnilionsBatting.年度, UnilionsBatting.打擊率,'.-', color='darkorange')
    plt.plot(DragonsBatting.年度, DragonsBatting.打擊率, '.-',color='red')
    plt.plot(GuardiansBatting.年度, GuardiansBatting.打擊率, '.-',color='darkblue')
    plt.plot(RakutenBatting.年度, RakutenBatting.打擊率, '.-',color='maroon')
    plt.xlabel('Season') # 設定x軸標題
    plt.xticks([2021,2020,2019,2018,2017,2016,2015,2014])
    plt.xticks(BrothersBatting.年度) # 設定x軸label以及垂直顯示
    plt.xticks(UnilionsBatting.年度) 
    plt.xticks(RakutenBatting.年度) 
    plt.xticks(GuardiansBatting.年度) 
    plt.xticks(DragonsBatting.年度) 
    plt.title('Unilions Batting Avg VS Other Teams ') # 設定圖表標題
    plt.legend(labels=["BrothersBatting", "UnilionsBatting","DragonsBatting","GuardiansBatting","RakutenBatting"], loc = 'best')
    st.pyplot(plt)
    
    plt.style.use("ggplot")
    plt.plot(BrothersBatting.年度, BrothersBatting.上壘率,'.-', color='yellow')
    plt.plot(UnilionsBatting.年度, UnilionsBatting.上壘率,'.-', color='darkorange')
    plt.plot(DragonsBatting.年度, DragonsBatting.上壘率, '.-',color='red')
    plt.plot(GuardiansBatting.年度, GuardiansBatting.上壘率,'.-', color='darkblue')
    plt.plot(RakutenBatting.年度, RakutenBatting.上壘率, '.-',color='maroon')
    plt.xlabel('Season') # 設定x軸標題
    plt.xticks([2021,2020,2019,2018,2017,2016,2015,2014])
    plt.xticks(BrothersBatting.年度) # 設定x軸label以及垂直顯示
    plt.xticks(UnilionsBatting.年度) 
    plt.xticks(RakutenBatting.年度) 
    plt.xticks(GuardiansBatting.年度) 
    plt.xticks(DragonsBatting.年度) 
    plt.title('Unilions Batting OBP VS Other Teams ') # 設定圖表標題
    plt.legend(labels=["BrothersBatting", "UnilionsBatting","DragonsBatting","GuardiansBatting","RakutenBatting"], loc = 'best')
    st.pyplot(plt)

    plt.style.use("ggplot")
    plt.plot(BrothersBatting.年度, BrothersBatting.長打率,'.-', color='yellow')
    plt.plot(UnilionsBatting.年度, UnilionsBatting.長打率,'.-', color='darkorange')
    plt.plot(DragonsBatting.年度, DragonsBatting.長打率, '.-',color='red')
    plt.plot(GuardiansBatting.年度, GuardiansBatting.長打率,'.-', color='darkblue')
    plt.plot(RakutenBatting.年度, RakutenBatting.長打率, '.-',color='maroon')
    plt.xlabel('Season') # 設定x軸標題
    plt.xticks([2021,2020,2019,2018,2017,2016,2015,2014])
    plt.xticks(BrothersBatting.年度) # 設定x軸label以及垂直顯示
    plt.xticks(UnilionsBatting.年度) 
    plt.xticks(RakutenBatting.年度) 
    plt.xticks(GuardiansBatting.年度) 
    plt.xticks(DragonsBatting.年度) 
    plt.title('Unilions Batting SLG VS Other Teams ') # 設定圖表標題
    plt.legend(labels=["BrothersBatting", "UnilionsBatting","DragonsBatting","GuardiansBatting","RakutenBatting"], loc = 'best')
    st.pyplot(plt)
 
  else:
    st.header('守備成績')
    st.write(UnilionsDefense) 
    st.header('數據分析')
    plt.style.use("ggplot")
    plt.plot(BrothersDefense.年度, BrothersDefense.守備率,'.-' ,color='yellow')
    plt.plot(UnilionsDefense.年度, UnilionsDefense.守備率,'.-' ,color='darkorange')
    plt.plot(DragonsDefense.年度, DragonsDefense.守備率, '.-',color='red')
    plt.plot(GuardiansDefense.年度, GuardiansDefense.守備率,'.-', color='darkblue')
    plt.plot(RakutenDefense.年度, RakutenDefense.守備率,'.-', color='maroon')
    plt.xlabel('Season') # 設定x軸標題
    plt.xticks([2021,2020,2019,2018,2017,2016,2015,2014])
    plt.xticks(BrothersDefense.年度) # 設定x軸
    plt.xticks(UnilionsDefense.年度) 
    plt.xticks(RakutenDefense.年度) 
    plt.xticks(GuardiansDefense.年度)
    plt.xticks(DragonsDefense.年度) 
    plt.title('Unilions Defense FPCT  VS Other Teams ') # 設定圖表標題
    plt.legend(labels=["BrothersDefense", "UnilionsDefense","DragonsDefense","GuardiansDefense","RakutenDefense"], loc = 'best')
    st.pyplot(plt) 
    
elif option == '味全龍':
  image = Image.open('Dragons.png')
  st.image(image)
  if option1=='球隊成績':
    st.header('球隊成績')
    st.write(Dragons) 
  elif option1=='投手成績':
    st.header('投手成績')  
    st.write(DragonsPitching)
    st.header('數據分析')
    plt.style.use("ggplot")
    plt.plot(BrothersPitching.年度, BrothersPitching.防禦率,'.-', color='yellow')
    plt.plot(UnilionsPitching.年度, UnilionsPitching.防禦率,'.-', color='darkorange')
    plt.plot(DragonsPitching.年度, DragonsPitching.防禦率,'.-', color='red')
    plt.plot(GuardiansPitching.年度, GuardiansPitching.防禦率,'.-', color='darkblue')
    plt.plot(RakutenPitching.年度, RakutenPitching.防禦率,'.-', color='maroon')
    plt.xlabel('Season') # 設定x軸標題
    plt.xticks([2021,2020,2019,2018,2017,2016,2015,2014])
    plt.xticks(BrothersPitching.年度) 
    plt.xticks(UnilionsPitching.年度) 
    plt.xticks(RakutenPitching.年度)
    plt.xticks(GuardiansPitching.年度) 
    #plt.xticks(DragonsPitching.年度) 
    plt.title('Dragons Pitching ERA VS Other Teams ') # 設定圖表標題
    plt.legend(labels=["BrothersPitching", "UnilionsPitching","DragonsPitching","GuardiansPitching","RakutenPitching"], loc = 'best')
    st.pyplot(plt)   
  elif option1=='打擊成績':
    st.header('打擊成績')
    st.write(DragonsBatting) 
    st.header('數據分析')
    plt.style.use("ggplot")
    plt.plot(BrothersBatting.年度, BrothersBatting.打擊率,'.-', color='yellow')
    plt.plot(UnilionsBatting.年度, UnilionsBatting.打擊率, '.-',color='darkorange')
    plt.plot(DragonsBatting.年度, DragonsBatting.打擊率, '.-',color='red')
    plt.plot(GuardiansBatting.年度, GuardiansBatting.打擊率,'.-', color='darkblue')
    plt.plot(RakutenBatting.年度, RakutenBatting.打擊率, '.-',color='maroon')
    plt.xlabel('Season') # 設定x軸標題
    plt.xticks([2021,2020,2019,2018,2017,2016,2015,2014])
    plt.xticks(BrothersBatting.年度) # 設定x軸label以及垂直顯示
    plt.xticks(UnilionsBatting.年度) 
    plt.xticks(RakutenBatting.年度) 
    plt.xticks(GuardiansBatting.年度) 
    plt.xticks(DragonsBatting.年度) 
    plt.title('Dragons Batting Avg VS Other Teams ') # 設定圖表標題
    plt.legend(labels=["BrothersBatting", "UnilionsBatting","DragonsBatting","GuardiansBatting","RakutenBatting"], loc = 'best')
    st.pyplot(plt)
    
    plt.style.use("ggplot")
    plt.plot(BrothersBatting.年度, BrothersBatting.上壘率,'.-', color='yellow')
    plt.plot(UnilionsBatting.年度, UnilionsBatting.上壘率,'.-', color='darkorange')
    plt.plot(DragonsBatting.年度, DragonsBatting.上壘率, '.-',color='red')
    plt.plot(GuardiansBatting.年度, GuardiansBatting.上壘率,'.-', color='darkblue')
    plt.plot(RakutenBatting.年度, RakutenBatting.上壘率, '.-',color='maroon')
    plt.xlabel('Season') # 設定x軸標題
    plt.xticks([2021,2020,2019,2018,2017,2016,2015,2014])
    plt.xticks(BrothersBatting.年度) # 設定x軸label以及垂直顯示
    plt.xticks(UnilionsBatting.年度) 
    plt.xticks(RakutenBatting.年度) 
    plt.xticks(GuardiansBatting.年度) 
    plt.xticks(DragonsBatting.年度) 
    plt.title('Dragons Batting OBP VS Other Teams ') # 設定圖表標題
    plt.legend(labels=["BrothersBatting", "UnilionsBatting","DragonsBatting","GuardiansBatting","RakutenBatting"], loc = 'best')
    st.pyplot(plt)
    
    plt.style.use("ggplot")
    plt.plot(BrothersBatting.年度, BrothersBatting.長打率,'.-', color='yellow')
    plt.plot(UnilionsBatting.年度, UnilionsBatting.長打率,'.-', color='darkorange')
    plt.plot(DragonsBatting.年度, DragonsBatting.長打率, '.-',color='red')
    plt.plot(GuardiansBatting.年度, GuardiansBatting.長打率,'.-', color='darkblue')
    plt.plot(RakutenBatting.年度, RakutenBatting.長打率, '.-',color='maroon')
    plt.xlabel('Season') # 設定x軸標題
    plt.xticks([2021,2020,2019,2018,2017,2016,2015,2014])
    plt.xticks(BrothersBatting.年度) # 設定x軸label以及垂直顯示
    plt.xticks(UnilionsBatting.年度) 
    plt.xticks(RakutenBatting.年度) 
    plt.xticks(GuardiansBatting.年度) 
    plt.xticks(DragonsBatting.年度) 
    plt.title('Dragons Batting SLG VS Other Teams ') # 設定圖表標題
    plt.legend(labels=["BrothersBatting", "UnilionsBatting","DragonsBatting","GuardiansBatting","RakutenBatting"], loc = 'best')
    st.pyplot(plt)
  else:
    st.header('守備成績')
    st.write(DragonsDefense) 
    st.header('數據分析')
    plt.style.use("ggplot")
    plt.plot(BrothersDefense.年度, BrothersDefense.守備率,'.-' ,color='yellow')
    plt.plot(UnilionsDefense.年度, UnilionsDefense.守備率,'.-' ,color='darkorange')
    plt.plot(DragonsDefense.年度, DragonsDefense.守備率, '.-',color='red')
    plt.plot(GuardiansDefense.年度, GuardiansDefense.守備率,'.-', color='darkblue')
    plt.plot(RakutenDefense.年度, RakutenDefense.守備率,'.-', color='maroon')
    plt.xlabel('Season') # 設定x軸標題
    plt.xticks([2021,2020,2019,2018,2017,2016,2015,2014])
    plt.xticks(BrothersDefense.年度) # 設定x軸
    plt.xticks(UnilionsDefense.年度) 
    plt.xticks(RakutenDefense.年度) 
    plt.xticks(GuardiansDefense.年度)
    plt.xticks(DragonsDefense.年度) 
    plt.title('Dragons Defense FPCT VS Other Teams ') # 設定圖表標題
    plt.legend(labels=["BrothersDefense", "UnilionsDefense","DragonsDefense","GuardiansDefense","RakutenDefense"], loc = 'best')
    st.pyplot(plt) 
  
elif option == '樂天桃猿':
  image = Image.open('Rakuten.png')
  st.image(image)
  if option1=='球隊成績':
    st.header('球隊成績')
    st.write(Rakuten) 
  elif option1=='投手成績':
    st.header('投手成績')
    st.write(RakutenPitching)
    st.header('數據分析')
    plt.style.use("ggplot")
    plt.plot(BrothersPitching.年度, BrothersPitching.防禦率,'.-', color='yellow')
    plt.plot(UnilionsPitching.年度, UnilionsPitching.防禦率,'.-', color='darkorange')
    plt.plot(DragonsPitching.年度, DragonsPitching.防禦率, '.-',color='red')
    plt.plot(GuardiansPitching.年度, GuardiansPitching.防禦率,'.-', color='darkblue')
    plt.plot(RakutenPitching.年度, RakutenPitching.防禦率, '.-',color='maroon')
    plt.xlabel('Season') # 設定x軸標題
    plt.xticks([2021,2020,2019,2018,2017,2016,2015,2014])
    plt.xticks(BrothersPitching.年度) # 設定x軸label以及垂直顯示
    plt.xticks(UnilionsPitching.年度) 
    plt.xticks(RakutenPitching.年度)
    plt.xticks(GuardiansPitching.年度) 
    plt.xticks(DragonsPitching.年度) 
    plt.title('Rakuten Pitching ERA VS Other Teams ') # 設定圖表標題
    plt.legend(labels=["BrothersPitching", "UnilionsPitching","DragonsPitching","GuardiansPitching","RakutenPitching"], loc = 'best')
    st.pyplot(plt)   
  elif option1=='打擊成績':
    st.header('打擊成績')
    st.write(RakutenBatting) 
    st.header('數據分析')
    plt.style.use("ggplot")
    plt.plot(BrothersBatting.年度, BrothersBatting.打擊率, '.-', color='yellow')
    plt.plot(UnilionsBatting.年度, UnilionsBatting.打擊率, '.-', color='darkorange')
    plt.plot(DragonsBatting.年度, DragonsBatting.打擊率, '.-', color='red')
    plt.plot(GuardiansBatting.年度, GuardiansBatting.打擊率, '.-', color='darkblue')
    plt.plot(RakutenBatting.年度, RakutenBatting.打擊率,  '.-',color='maroon')
    plt.xlabel('Season') # 設定x軸標題
    plt.xticks([2021,2020,2019,2018,2017,2016,2015,2014])
    plt.xticks(BrothersBatting.年度) # 設定x軸label以及垂直顯示
    plt.xticks(UnilionsBatting.年度) 
    plt.xticks(RakutenBatting.年度) 
    plt.xticks(GuardiansBatting.年度) 
    plt.xticks(DragonsBatting.年度) 
    plt.title('Rakuten Batting Avg VS Other Teams ') # 設定圖表標題
    plt.legend(labels=["BrothersBatting", "UnilionsBatting","DragonsBatting","GuardiansBatting","RakutenBatting"], loc = 'best')
    st.pyplot(plt)
    
    plt.style.use("ggplot")
    plt.plot(BrothersBatting.年度, BrothersBatting.上壘率,'.-', color='yellow')
    plt.plot(UnilionsBatting.年度, UnilionsBatting.上壘率,'.-', color='darkorange')
    plt.plot(DragonsBatting.年度, DragonsBatting.上壘率, '.-',color='red')
    plt.plot(GuardiansBatting.年度, GuardiansBatting.上壘率,'.-', color='darkblue')
    plt.plot(RakutenBatting.年度, RakutenBatting.上壘率, '.-',color='maroon')
    plt.xlabel('Season') # 設定x軸標題
    plt.xticks([2021,2020,2019,2018,2017,2016,2015,2014])
    plt.xticks(BrothersBatting.年度) # 設定x軸label以及垂直顯示
    plt.xticks(UnilionsBatting.年度) 
    plt.xticks(RakutenBatting.年度) 
    plt.xticks(GuardiansBatting.年度) 
    plt.xticks(DragonsBatting.年度) 
    plt.title('Rakuten Batting OBP VS Other Teams ') # 設定圖表標題
    plt.legend(labels=["BrothersBatting", "UnilionsBatting","DragonsBatting","GuardiansBatting","RakutenBatting"], loc = 'best')
    st.pyplot(plt)
   
    plt.style.use("ggplot")
    plt.plot(BrothersBatting.年度, BrothersBatting.長打率,'.-', color='yellow')
    plt.plot(UnilionsBatting.年度, UnilionsBatting.長打率,'.-', color='darkorange')
    plt.plot(DragonsBatting.年度, DragonsBatting.長打率, '.-',color='red')
    plt.plot(GuardiansBatting.年度, GuardiansBatting.長打率,'.-', color='darkblue')
    plt.plot(RakutenBatting.年度, RakutenBatting.長打率, '.-',color='maroon')
    plt.xlabel('Season') # 設定x軸標題
    plt.xticks([2021,2020,2019,2018,2017,2016,2015,2014])
    plt.xticks(BrothersBatting.年度) # 設定x軸label以及垂直顯示
    plt.xticks(UnilionsBatting.年度) 
    plt.xticks(RakutenBatting.年度) 
    plt.xticks(GuardiansBatting.年度) 
    plt.xticks(DragonsBatting.年度) 
    plt.title('Rakuten Batting SLG VS Other Teams ') # 設定圖表標題
    plt.legend(labels=["BrothersBatting", "UnilionsBatting","DragonsBatting","GuardiansBatting","RakutenBatting"], loc = 'best')
    st.pyplot(plt)
   
  else:
    st.header('守備成績')
    st.write(RakutenDefense)
    st.header('數據分析')
    plt.style.use("ggplot")
    plt.plot(BrothersDefense.年度, BrothersDefense.守備率,'.-' ,color='yellow')
    plt.plot(UnilionsDefense.年度, UnilionsDefense.守備率,'.-' ,color='darkorange')
    plt.plot(DragonsDefense.年度, DragonsDefense.守備率, '.-',color='red')
    plt.plot(GuardiansDefense.年度, GuardiansDefense.守備率,'.-', color='darkblue')
    plt.plot(RakutenDefense.年度, RakutenDefense.守備率,'.-', color='maroon')
    plt.xlabel('Season') # 設定x軸標題
    plt.xticks([2021,2020,2019,2018,2017,2016,2015,2014])
    plt.xticks(BrothersDefense.年度) # 設定x軸
    plt.xticks(UnilionsDefense.年度) 
    plt.xticks(RakutenDefense.年度) 
    plt.xticks(GuardiansDefense.年度)
    plt.xticks(DragonsDefense.年度) 
    plt.title('Rakuten Defense FPCT  VS Other Teams ') # 設定圖表標題
    plt.legend(labels=["BrothersDefense", "UnilionsDefense","DragonsDefense","GuardiansDefense","RakutenDefense"], loc = 'best')
    st.pyplot(plt) 
  
elif option == '富邦悍將':
  image = Image.open('guardians.png')
  st.image(image)
  if option1=='球隊成績':
    st.header('球隊成績')
    st.write(Guardians) 
  elif option1=='投手成績':
    st.header('投手成績')
    st.write(GuardiansPitching)
    st.header('數據分析')
    plt.style.use("ggplot")
    plt.plot(BrothersPitching.年度, BrothersPitching.防禦率,'.-', color='yellow')
    plt.plot(UnilionsPitching.年度, UnilionsPitching.防禦率,'.-', color='darkorange')
    plt.plot(DragonsPitching.年度, DragonsPitching.防禦率, '.-',color='red')
    plt.plot(GuardiansPitching.年度, GuardiansPitching.防禦率, '.-',color='darkblue')
    plt.plot(RakutenPitching.年度, RakutenPitching.防禦率,'.-', color='maroon')
    plt.xlabel('Season') # 設定x軸標題
    plt.xticks([2021,2020,2019,2018,2017,2016,2015,2014])
    plt.xticks(BrothersPitching.年度 )
    plt.xticks(UnilionsPitching.年度) 
    plt.xticks(RakutenPitching.年度) 
    plt.xticks(GuardiansPitching.年度) 
    plt.xticks(DragonsPitching.年度) 
    plt.title('Guardians Pitching ERA VS Other Teams ') # 設定圖表標題
    plt.legend(labels=["BrothersPitching", "UnilionsPitching","DragonsPitching","GuardiansPitching","RakutenPitching"], loc = 'best')
    st.pyplot(plt)       
  elif option1=='打擊成績':
    st.header('打擊成績')
    st.write(GuardiansBatting) 
    st.header('數據分析')
    plt.style.use("ggplot")
    plt.plot(BrothersBatting.年度, BrothersBatting.打擊率, '.-', color='yellow')
    plt.plot(UnilionsBatting.年度, UnilionsBatting.打擊率, '.-', color='darkorange')
    plt.plot(DragonsBatting.年度, DragonsBatting.打擊率,  '.-',color='red')
    plt.plot(GuardiansBatting.年度, GuardiansBatting.打擊率,  '.-',color='darkblue')
    plt.plot(RakutenBatting.年度, RakutenBatting.打擊率,  '.-',color='maroon')
    plt.xlabel('Season') # 設定x軸標題
    plt.xticks([2021,2020,2019,2018,2017,2016,2015,2014])
    plt.xticks(BrothersBatting.年度) # 設定x軸label以及垂直顯示
    plt.xticks(UnilionsBatting.年度) 
    plt.xticks(RakutenBatting.年度) 
    plt.xticks(GuardiansBatting.年度) 
    plt.xticks(DragonsBatting.年度) 
    plt.title('Guardians Batting Avg VS Other Teams ') # 設定圖表標題
    plt.legend(labels=["BrothersBatting", "UnilionsBatting","DragonsBatting","GuardiansBatting","RakutenBatting"], loc = 'best')
    st.pyplot(plt)
    
    plt.style.use("ggplot")
    plt.plot(BrothersBatting.年度, BrothersBatting.上壘率,'.-', color='yellow')
    plt.plot(UnilionsBatting.年度, UnilionsBatting.上壘率,'.-', color='darkorange')
    plt.plot(DragonsBatting.年度, DragonsBatting.上壘率, '.-',color='red')
    plt.plot(GuardiansBatting.年度, GuardiansBatting.上壘率,'.-', color='darkblue')
    plt.plot(RakutenBatting.年度, RakutenBatting.上壘率, '.-',color='maroon')
    plt.xlabel('Season') # 設定x軸標題
    plt.xticks([2021,2020,2019,2018,2017,2016,2015,2014])
    plt.xticks(BrothersBatting.年度) # 設定x軸label以及垂直顯示
    plt.xticks(UnilionsBatting.年度) 
    plt.xticks(RakutenBatting.年度) 
    plt.xticks(GuardiansBatting.年度) 
    plt.xticks(DragonsBatting.年度) 
    plt.title('Guardians Batting OBP VS Other Teams ') # 設定圖表標題
    plt.legend(labels=["BrothersBatting", "UnilionsBatting","DragonsBatting","GuardiansBatting","RakutenBatting"], loc = 'best')
    st.pyplot(plt)
    
    plt.style.use("ggplot")
    plt.plot(BrothersBatting.年度, BrothersBatting.長打率,'.-', color='yellow')
    plt.plot(UnilionsBatting.年度, UnilionsBatting.長打率,'.-', color='darkorange')
    plt.plot(DragonsBatting.年度, DragonsBatting.長打率, '.-',color='red')
    plt.plot(GuardiansBatting.年度, GuardiansBatting.長打率,'.-', color='darkblue')
    plt.plot(RakutenBatting.年度, RakutenBatting.長打率, '.-',color='maroon')
    plt.xlabel('Season') # 設定x軸標題
    plt.xticks([2021,2020,2019,2018,2017,2016,2015,2014])
    plt.xticks(BrothersBatting.年度) # 設定x軸label以及垂直顯示
    plt.xticks(UnilionsBatting.年度) 
    plt.xticks(RakutenBatting.年度) 
    plt.xticks(GuardiansBatting.年度) 
    plt.xticks(DragonsBatting.年度) 
    plt.title('Guardians Batting SLG VS Other Teams ') # 設定圖表標題
    plt.legend(labels=["BrothersBatting", "UnilionsBatting","DragonsBatting","GuardiansBatting","RakutenBatting"], loc = 'best')
    st.pyplot(plt)
  else:
    st.header('守備成績') 
    st.write(GuardiansDefense)  
    st.header('數據分析')
    plt.style.use("ggplot")
    plt.plot(BrothersDefense.年度, BrothersDefense.守備率,'.-' ,color='yellow')
    plt.plot(UnilionsDefense.年度, UnilionsDefense.守備率,'.-' ,color='darkorange')
    plt.plot(DragonsDefense.年度, DragonsDefense.守備率, '.-',color='red')
    plt.plot(GuardiansDefense.年度, GuardiansDefense.守備率,'.-', color='darkblue')
    plt.plot(RakutenDefense.年度, RakutenDefense.守備率,'.-', color='maroon')
    plt.xlabel('Season') # 設定x軸標題
    plt.xticks([2021,2020,2019,2018,2017,2016,2015,2014])
    plt.xticks(BrothersDefense.年度) # 設定x軸
    plt.xticks(UnilionsDefense.年度) 
    plt.xticks(RakutenDefense.年度) 
    plt.xticks(GuardiansDefense.年度)
    plt.xticks(DragonsDefense.年度) 
    plt.title('Guardians Defense FPCT  VS Other Teams ') # 設定圖表標題
    plt.legend(labels=["BrothersDefense", "UnilionsDefense","DragonsDefense","GuardiansDefense","RakutenDefense"], loc = 'best')
    st.pyplot(plt) 
