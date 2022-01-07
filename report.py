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
  st.header('中信兄弟')
  st.write('兄弟象(1990-2013) – 中信兄弟(2014 - 至今)')
  image = Image.open('brothers.png')
  st.image(image)
  st.write('季冠軍17次，年度冠軍8次')
  st.write('中信兄弟隊前身兄弟象隊為中職四支創始球隊之一，1992年至1994年曾創下空前的連續三年奪下總冠軍之傲人成績，1992年球季更創下了例行賽45場中37場封王最快速封王的紀錄。之後兄弟象隊於2001年至2003年達成第二次三連霸紀錄，成為中職至今唯一兩度締造三連霸紀錄的球隊。2010年兄弟象隊達成了隊史千勝紀錄，為中職至今唯二達成的球隊，同年下半季取得隊史第11座季冠軍，在當年總冠軍賽以四連勝橫掃興農牛隊，奪下隊史第七座總冠軍，之後10年間，中信兄弟多次闖進總冠軍賽卻始終鎩羽而歸，終於在2021年奪下了隊史第八座總冠軍，奪冠次數僅次於統一7-ELEVEn獅隊，為中華職棒史上奪得總冠軍次數第二多的球隊。')
  st.write("嗆司曲 兄弟精神")
  audio_file = open("兄弟精神.mp3", "rb")
  st.audio(audio_file.read())  
    
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
  st.header('統一7-Eleven獅')
  st.write('統一獅(1990-2007) – 統一7-ELEVEn獅(2008 - 至今 )')

  image = Image.open('unilion.png')
  st.image(image)
  st.write('季冠軍15次，年度冠軍10次')
  st.write('統一7-ELEVEn獅隊為台灣在1989年成立中華職棒聯盟時的四支創始球隊之一，也是唯一從職棒元年存續至今的球隊，最初僅命名為統一獅隊；是聯盟第一支有二軍的球隊，同時也是目前中華職棒聯盟贏得總冠軍次數最多的球隊，母企業為統一企業。由於中職初創時統一獅隊成軍較晚，人手不足，經驗也有限，因此於職棒元年開打後，即創下八連敗的紀錄，並在上半球季敬陪末座。但秉著「誠實苦幹」的企業精神，統一球團積極整軍經武，使獅子軍下半球季戰績得以回升，全年度排名第三，免於墊底。隔年更在投打戰力補強有成的情況下，於總冠軍賽擊敗味全龍隊，笑擁隊史首座總冠軍獎盃')
  st.write("嗆司曲 誰與爭鋒")
  audio_file = open("誰與爭鋒.mp3", "rb")
  st.audio(audio_file.read())  
    
    
    
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
  st.header('味全龍')
  st.write('味全龍(1990-1999, 2019 - 至今)')
  image = Image.open('Dragons.png')
  st.image(image)
  st.write('季冠軍17次，年度冠軍8次')
  st.write('味全龍隊是中華職棒所屬的球隊，歷史可追溯至1980年代的業餘成棒。其首次進軍中職時，是由味全企業出資成立「純青職棒事業股份有限公司」經營；但1999年季後因經營虧損，以及併購母企業的頂新集團無意繼續經營，最終決定解散球隊。但相隔20年後的2019年，頂新集團出乎意料宣佈重組球隊，並通過聯盟審核，以聯盟第五隊的身份重返中華職棒。')
  st.write("嗆司曲 龍霸一方")
  audio_file = open("龍霸一方.mp3", "rb")
  st.audio(audio_file.read())  
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
  st.header('樂天桃猿')
  st.write('第一金剛(2003) – La new熊(2004-2010) – Lamigo 桃猿(2011-2019) – 樂天桃猿(2020 - 至今)')
  image = Image.open('Rakuten.png')
  st.image(image)
  st.write('季冠軍13次，年度冠軍7次')
  st.write('2019年07月03日，甫達成季冠軍五連霸的Lamigo桃猿隊於選秀會結束後，突如其來宣佈因不堪連年經營虧損，決定轉賣球隊，也震撼了原先尚在歡慶味全龍隊重返職棒的中華職棒。09月19日，桃猿隊正式宣佈將經營權完全轉售予已在日本職棒擁有東北樂天金鷲隊的日商樂天集團，結束16年職棒經營事業，樂天也向桃猿保證，接手後大高熊育樂股份有限公司（經營桃猿隊）、大桃猿育樂股份有限公司（經營桃園國際棒球場）的球隊相關工作人員都會予以留用。')
  st.write("應援曲 勇敢樂天")
  audio_file = open("勇敢樂天.mp3", "rb")
  st.audio(audio_file.read())  
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
  st.header('富邦悍將')
  st.write('俊國熊(1993-1995) – 興農熊(1996上半季) – 興農牛(1996下半季 – 2012) – 義大犀牛(2013-2016) – 富邦悍將(2017 - 至今)')
  image = Image.open('guardians.png')
  st.image(image)
  st.write('季冠軍8次，年度冠軍3次')
  st.write('富邦悍將隊（Fubon Guardians）的前身可追溯至成立於1989年的社會甲組球隊俊國建設棒球隊。俊國棒球隊進軍職棒後更名為俊國熊隊，其後歷經三次轉賣，隊名也陸續更改為興農熊隊、興農牛隊、義大犀牛隊，並曾獲得三次總冠軍。2016年季中，當時擁有義大犀牛隊的義联集團宣佈出售球隊，最後由長期贊助業餘棒運的富邦金控以新台幣3億元買下。該年季後，義大隊奪得隊史首座也是最後一座的總冠軍後，隨即自同年11月01日起改由富邦金控接手經營，並在11月15日正式公佈新隊名為富邦悍將隊。')
  st.write("嗆司曲 超強一擊")
  audio_file = open("超強一擊.mp3", "rb")
  st.audio(audio_file.read())  
 
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
