import time
from gtts import gTTS
from pygame import mixer
import tempfile
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}
url='https://tw.appledaily.com/realtime/recommend/'
tar=requests.get(url,headers=headers)


soup=BeautifulSoup(tar.text,'lxml')
one=soup.find('div',id="section-body")
two = one.find_all('div',class_='storycard-headline text_greyish-brown-two')
for i in two:
   print(i.select_one("span").getText())


count=0  
with open("news.txt","w",encoding='utf-8') as fp:
    for i in two:
        count+=1
        fp.write(str(count)+'.'+str(i.select_one("span").getText())+'\n')
    fp.close


def talk(sentence,lang):
    with tempfile.NamedTemporaryFile(delete=True) as f:
        tts=gTTS(text=sentence,lang=lang)
        tts.save('{}.mp3'.format(f.name))
        mixer.init()
        mixer.music.load('{}.mp3'.format(f.name))
        mixer.music.play(loops=0)




news=[]
with open('news.txt','r',encoding='utf-8') as f:
    for line in f:
        news.append(line)


talk(str(news),'zh-tw')
time.sleep(300)









#沒MIC
'''
r=sr.Recognizer()
r.energy_threshold=4000
while True:
    try:
        with sr.Microphone() as soure:
            print("請開始說話:")
            audio=r.listen(soure)
            listen_text=r.recognize_google(audio,language='zh-TW')
            print(listen_text+'\n')
            if listen_text=="結束":
                break
    except sr.UnknownValueError:
        print('無法辨識\n')
    except sr.RequestError:
        print('錯誤\n')
'''

