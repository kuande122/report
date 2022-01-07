import streamlit as st
import pandas as pd               # 資料處理套件
import matplotlib.pyplot as plt   # 資料視覺化套件
import xlrd
import plotly.express as px
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
GuardiansBatting=pd.read_excel('GuardiansBatting.xlsx')
BrothersDefense=pd.read_excel('BrothersDefense.xlsx')
UnilionsDefense=pd.read_excel('UnilionsDefense.xlsx')
DragonsDefense=pd.read_excel('DragonsDefense.xlsx')
RakutenDefense=pd.read_excel('RakutenDefense.xlsx')
GuardiansDefense=pd.read_excel('GuardiansDefense.xlsx')
Brothers=pd.read_excel('Brothers.xlsx')
Unilions=pd.read_excel('Unilions.xlsx')
Dragons=pd.read_excel('Dragons.xlsx')
Rakuten=pd.read_excel('Rakuten.xlsx')
Guardians=pd.read_excel('Guardians.xlsx')

if option == '中信兄弟':
  image = Image.open('brothers.png')
  st.image(image)
    
  if option1=='球隊成績':
    st.header('球隊成績')
    st.write(Brothers) 
    st.header('2021全年度戰績')
    labels = 'Home Win', 'Away Win','Home Lose', 'Away Lose','Home Tie', 'Away Tie'
    sizes = [22, 34, 26, 23,2,3]
    explode = (0,0.2,0 ,0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
    shadow=True, startangle=90,textprops = {"fontsize" : 7})
    plt.legend(loc = "best")   
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)

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
    x=st.button('點取看更多分析')
    if x:
        df = pd.DataFrame(
        [["2021", 839, 317], ["2020", 1035, 366],["2019",797,376],["2018",820,394],["2017",841,424],["2016",867,398],
        ["2015",710,345],["2014",674,320]],
        columns=["Year", "StrikeOut", "BB"],
        )

        fig = px.bar(df, x="Year", y=["StrikeOut","BB"], barmode='group', height=400)
        
        st.plotly_chart(fig)
    
      
    
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
    x=st.button('點取看更多分析')
    if x:
        plt.subplot(2, 1 ,1)
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
        plt.subplot(2, 1 ,2)
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
        plt.subplots_adjust(left=0.125,
                    bottom=3.0, 
                    right=0.9, 
                    top=5.0, 
                    wspace=0.2, 
                    hspace=0.3)
        st.pyplot(plt)
        df = pd.DataFrame(
        [["2021", 1080, 77], ["2020", 1319, 143],["2019",1168,148],["2018",1152,91],["2017",1214,145],["2016",1460,169],
        ["2015",1308,90],["2014",1083,52]],
         columns=["Year", "Hit", "Homerun"],
        )

        fig = px.bar(df, x="Year", y=["Hit", "Homerun"], barmode='group', height=400)
        
        st.plotly_chart(fig)
    
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
    x=st.button('點取看更多分析')
    if x:
        df = pd.DataFrame(
        [["2021", 4591, 73], ["2020", 4522, 96],["2019",4497,89],["2018",4477,132],["2017",4662,118],["2016",4633,134],
        ["2015",4605,129],["2014",4535,97]],
        columns=["Year", "Baseball Defense Opportunity", "E"],
        )

        fig = px.bar(df, x="Year", y=["Baseball Defense Opportunity","E"], barmode='group', height=400)
        
        st.plotly_chart(fig)
    
    
elif option == '統一7-Eleven獅':
  image = Image.open('unilion.png')
  st.image(image)
  if option1=='球隊成績':
    st.header('球隊成績')
    st.write(Unilions) 
    st.header('2021全年度戰績')
    labels = 'Home Win', 'Away Win','Home Lose', 'Away Lose','Home Tie', 'Away Tie'
    sizes = [36, 28, 21, 30,3,2]
    explode = (0.2,0,0 ,0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
    shadow=True, startangle=90,textprops = {"fontsize" : 7})

    plt.legend(loc = "best")   
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)
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
    x=st.button('點取看更多分析')
    if x:
        df = pd.DataFrame(
        [["2021", 846, 343], ["2020", 793, 395],["2019",775,368],["2018",858,369],["2017",867,431],["2016",831,439],
        ["2015",699,480],["2014",622,330]],
         columns=["Year", "StrikeOut", "BB"],
        )

        fig = px.bar(df, x="Year", y=["StrikeOut","BB"], barmode='group', height=400)
        
        st.plotly_chart(fig)
        
        
        
        
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
     x=st.button('點取看更多分析')
     if x:
        plt.subplot(2, 1 ,1)
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
       
        plt.subplot(2, 1 ,2)
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
        plt.subplots_adjust(left=0.125,
                    bottom=3.0, 
                    right=0.9, 
                    top=5.0, 
                    wspace=0.2, 
                    hspace=0.3)
        st.pyplot(plt)
        df = pd.DataFrame(
        [["2021", 1041, 57], ["2020", 1261, 143],["2019",1070,99],["2018",1221,114],["2017",1154,103],["2016",1282,145],
        ["2015",1196,98],["2014",1079,55]],
        columns=["Year", "Hit", "Homerun"]
        )
        fig = px.bar(df, x="Year", y=["Hit", "Homerun"], barmode='group', height=400)
        
        st.plotly_chart(fig)
 
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
    x=st.button('點取看更多分析')
    if x:
        df = pd.DataFrame(
        [["2021", 4454, 104], ["2020", 4523, 101],["2019",4544,134],["2018",4533,131],["2017",4525,121],["2016",4518,140],
        ["2015",4552,123],["2014",4705,111]],
        columns=["Year", "Baseball Defense Opportunity", "E"],
        )

        fig = px.bar(df, x="Year", y=["Baseball Defense Opportunity","E"], barmode='group', height=400)
        
        st.plotly_chart(fig)
elif option == '味全龍':
  image = Image.open('Dragons.png')
  st.image(image)
  if option1=='球隊成績':
    st.header('球隊成績')
    st.write(Dragons) 
    st.header('2021全年度戰績')
    labels = 'Home Win', 'Away Win','Home Lose', 'Away Lose','Home Tie', 'Away Tie'
    sizes = [29, 22, 29, 38,2,1]
    explode = (0,0,0 ,0.2, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
    shadow=True, startangle=90,textprops = {"fontsize" : 7})

    plt.legend(loc = "best")   
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)
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
    x=st.button('點取看更多分析')
    if x:
        df = pd.DataFrame(
        [["2021", 734, 378]],
         columns=["Year", "StrikeOut", "BB"],
        )

        fig = px.bar(df, x="Year", y=["StrikeOut","BB"], barmode='group', height=400)
        
        st.plotly_chart(fig)
    
  elif option1=='打擊成績':
    st.header('打擊成績')
    st.write(DragonsBatting)
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
    plt.title('Dragons Batting Avg VS Other Teams ') # 設定圖表標題
    plt.legend(labels=["BrothersBatting", "UnilionsBatting","DragonsBatting","GuardiansBatting","RakutenBatting"], loc = 'best')
    st.pyplot(plt)
    x=st.button('點取看更多分析')
    if x:
        plt.subplot(2, 1 ,1)
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
        plt.subplot(2, 1 ,2)
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
        plt.subplots_adjust(left=0.125,
                    bottom=3.0, 
                    right=0.9, 
                    top=5.0, 
                    wspace=0.2, 
                    hspace=0.3)
        st.pyplot(plt)
        df = pd.DataFrame([["2021", 977, 52]],columns=["Year", "Hit", "Homerun"]
        )   
        
        fig = px.bar(df, x="Year", y=["Hit", "Homerun"], barmode='group', height=400)
        
        st.plotly_chart(fig)
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
    x=st.button('點取看更多分析')
    if x:
        df = pd.DataFrame(
        [["2021", 4597, 117]],
        columns=["Year", "Baseball Defense Opportunity", "E"],
        )

        fig = px.bar(df, x="Year", y=["Baseball Defense Opportunity","E"], barmode='group', height=400)
        
        st.plotly_chart(fig)
  
elif option == '樂天桃猿':
  image = Image.open('Rakuten.png')
  st.image(image)
  if option1=='球隊成績':
    st.header('球隊成績')
    st.write(Rakuten) 
    st.header('2021全年度戰績')
    labels = 'Home Win', 'Away Win','Home Lose', 'Away Lose','Home Tie', 'Away Tie'
    sizes = [27, 29, 31, 30,2,1]
    explode = (0,0,0.2 ,0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
    shadow=True, startangle=90,textprops = {"fontsize" : 7})
    
    plt.legend(loc = "best")   
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)
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
    x=st.button('點取看更多分析')
    if x:
        df = pd.DataFrame(
        [["2021", 798, 399], ["2020", 893, 378]],
         columns=["Year", "StrikeOut", "BB"],
        )

        fig = px.bar(df, x="Year", y=["StrikeOut","BB"], barmode='group', height=400)
        
        st.plotly_chart(fig)
    
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
    x=st.button('點取看更多分析')
    if x:
        plt.subplot(2, 1 ,1)
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
        plt.subplot(2, 1 ,2)
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
        plt.subplots_adjust(left=0.125,
                    bottom=3.0, 
                    right=0.9, 
                    top=5.0, 
                    wspace=0.2, 
                    hspace=0.3)
        st.pyplot(plt)
        df = pd.DataFrame(
        [["2021", 1170, 78], ["2020", 1361, 137]],
        columns=["Year", "Hit", "Homerun"]
        )
        fig = px.bar(df, x="Year", y=["Hit", "Homerun"], barmode='group', height=400)
        
        st.plotly_chart(fig)
   
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
    x=st.button('點取看更多分析')
    if x:
        df = pd.DataFrame(
        [["2021", 4583, 109], ["2020", 4563, 130]],
        columns=["Year", "Baseball Defense Opportunity", "E"],
        )

        fig = px.bar(df, x="Year", y=["Baseball Defense Opportunity","E"], barmode='group', height=400)
        
        st.plotly_chart(fig)
  
elif option == '富邦悍將':
  image = Image.open('guardians.png')
  st.image(image)
  if option1=='球隊成績':
    st.header('球隊成績')
    st.write(Guardians) 
    st.header('2021全年度戰績')
    labels = 'Home Win', 'Away Win','Home Lose', 'Away Lose','Home Tie', 'Away Tie'
    sizes = [27, 27, 32, 30,1,3]
    explode = (0,0,0.2 ,0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
    shadow=True, startangle=90,textprops = {"fontsize" : 7})

    plt.legend(loc = "best")   
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)
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
    x=st.button('點取看更多分析')
    if x:
        df = pd.DataFrame(
        [["2021", 851, 363], ["2020", 867, 344],["2019",920,326],["2018",837,341],["2017",839,440]],
         columns=["Year", "StrikeOut", "BB"],
        )

        fig = px.bar(df, x="Year", y=["StrikeOut","BB"], barmode='group', height=400)
        
        st.plotly_chart(fig)
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
    x=st.button('點取看更多分析')
    if x:
        plt.subplot(2, 1 ,1)
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
        plt.subplot(2, 1 ,2)
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
        plt.subplots_adjust(left=0.125,
                    bottom=3.0, 
                    right=0.9, 
                    top=5.0, 
                    wspace=0.2, 
                    hspace=0.3)
        st.pyplot(plt)
        df = pd.DataFrame(
        [["2021", 1044, 67], ["2020", 1227, 138],["2019",1218,102],["2018",1217,86],["2017",1180,95]],
        columns=["Year", "Hit", "Homerun"]
        )
        fig = px.bar(df, x="Year", y=["Hit", "Homerun"], barmode='group', height=400)
        
        st.plotly_chart(fig)
    
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
    x=st.button('點取看更多分析')
    if x:
        df = pd.DataFrame(
        [["2021", 4522, 100], ["2020", 4518, 119],["2019",4411,93],["2018",4497,121],["2017",4381,114]],
        columns=["Year", "Baseball Defense Opportunity", "E"],
        )

        fig = px.bar(df, x="Year", y=["Baseball Defense Opportunity","E"], barmode='group', height=400)
        
        st.plotly_chart(fig)
