''' This is done by me'''
#klfdsfndslfndsklfsdfljdfljflksj
#lkfjkfjdslfnsdlfsdlfdslf
#vjdkcjdlkmdsksdlkdsflksdn
from flask import Flask, render_template
from wizcon.wizcon import Wizcon
from PIL import Image,ImageGrab
from googlesearch import search
from win10toast import ToastNotifier
from PyDictionary import PyDictionary
from playsound import playsound
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pyttsx3 
import datetime
import asyncio
import speech_recognition as sr
import wikipedia
import sports
import webbrowser
import speedtest as st
import sports
import os
import pyautogui
import time
import random
import requests
import pyowm
import pyperclip
import pyjokes
 
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  

@app.route('/jarvis/')
def jarvis_assistant():
    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate_of_words=engine.setProperty('rate',193)
  

    def network_availability():
        try:
            requests.get('https://www.google.com').status_code
            return True
        except Exception:
            return False    

    def speak(text):
        engine.say(text) 
        engine.runAndWait()

    def greeting():
        hours=datetime.datetime.now().hour
        if hours<12:
            speak('Good Morning! Sharad')
        elif hours>=12 and hours<=16:
            speak('Good AfterNoon! Sharad') 
        else:
            speak('Good Evening! Sharad')  
        speak(' I am awake how may i help you????')      

    def command():
        input_command=sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening...') 
            input_command.adjust_for_ambient_noise(source,duration=0.25)
            audio=input_command.listen(source)
        try:
            print("Processing...") 
            query=input_command.recognize_google(audio,language="en-in")
            print(f"User said:{query}\n")
        except Exception:
            print("Say that again please...") 
            return "String"
        return query     

    greeting()
    while True:
        if network_availability(): 
            smart_bulb=Wizcon('192.168.100.8')
            rate_of_words=engine.setProperty('rate',193)
            final_result=command().lower()     
            if 'go to sleep' in final_result:
                    speak('ok I am going to sleep you can wake me up later if you want to')
                    break
            elif 'meaning' in final_result:
                engine.setProperty('rate',150)
                ll=final_result.split(' ')
                word=ll[-1]
                ob=PyDictionary()
                try:
                    meaning=ob.meaning(word)['Noun']
                    speak(meaning)
                except Exception:
                    speak('say that again')

            elif 'speed' in final_result:
                try: 
                    speak('ok I am checking your internet speed this may take some time please hang on!!')
                    speed_test = st.Speedtest()
                    speed_test.get_best_server()
                #    ping = str(speed_test.results.ping)+'ms'
                    download = speed_test.download()
                    upload = speed_test.upload()
                    num_download=round(download / (10**6), 1)
                    num_upload=round(upload / (10**6), 1)
                    if num_download>25 or num_upload>25:
                        speak('your internet speed is fast')
                    else:
                        speak('your internet speed is poor')    
                    download_mbs = str(round(download / (10**6), 1))+'Mbp s'
                    upload_mbs = str(round(upload / (10**6), 1))+'Mbp s'
                #    print(ping)
                    speak(f'Your Downloading speed is {download_mbs}')
                    speak(f'Your Uploading speed is {upload_mbs}')
                except Exception:
                    speak('Something is wrong please try again later')

            elif 'turn on' in final_result:
                speak('turning on the bulb')
                asyncio.run(smart_bulb.turn_bulb_on_scene_id(13))  

            elif 'party' in final_result:
                speak('acivating party mode')
                asyncio.run(smart_bulb.turn_bulb_on_scene_id(4))

            elif 'turn off' in final_result:
                speak('turning off the bulb')
                asyncio.run(smart_bulb.turn_bulb_off())   

            elif 'change the colour' in final_result:
                speak('changing colour of the bulb')
                while True:
                    theme=random.randint(1,32)
                    asyncio.run(smart_bulb.turn_bulb_on_scene_id(theme))
                    time.sleep(2)
                    speak('do you like this colour?')
                    ans=command().lower()
                    if 'yes' in ans:
                        speak('ok great')
                        break
                    elif 'no change' in ans:
                        speak('ok I am changing the colour')

            elif 'score' in final_result:
                toaster=ToastNotifier()
                match_info=sports.get_sport('CRICKET')
                speak('ok i am showing you the match stats hopefully your favourite team is winning')
                toaster.show_toast('LIVE SCORE',str(match_info[0]),duration=10,icon_path='C:\\Users\\sharad\\Documents\\CODE\\PROJECTS\\JARVIS\\ipl.ico')

            elif 'music' in final_result:
                dir='A:\\Music\\'
                l=os.listdir(dir)
                random_number=random.randint(0,len(l))
                new_dir=dir+l[random_number]
                speak('Ok I am playing music you just sit back and enjoy!!')
                playsound(new_dir)

            elif 'who is' in final_result:
                try:
                    rate_of_words=engine.setProperty('rate',140)
                    results=wikipedia.summary(final_result,sentences=1)
                    speak(results)

                except Exception:
                    speak('I do not know who he is')
         
            elif 'screenshot' in final_result:
                speak('ok')
                image=ImageGrab.grab()     
                image.show()   

            elif 'open youtube' in final_result:
                speak('opening you tube...')
                chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                webbrowser.get(chrome_path).open("youtube.com")
                break

            elif 'play video on youtube' in final_result:  
                try:
                  import pywhatkit as kit    
                  speak('ok which video should i play')    
                  video_name=command().lower()
                  speak(f'ok playing {video_name}')
                  kit.playonyt(video_name)
                  break

                except Exception:
                    speak('something is wrong make sure you have the library')

            elif 'search' in final_result:
                speak('which query do you want me to search?')
                quer=command().lower()
                speak('ok i am searching you something hopefully this can help')
                chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                for i in search(quer,start=1,stop=1):
                    webbrowser.get(chrome_path).open(i)
                    
            elif 'joke' in final_result:
                joke=pyjokes.get_joke()
                rate_of_words=engine.setProperty('rate',145)
                speak(joke)        

            elif 'send whatsapp to' in final_result:
                l=final_result.split(' ')
                name=''
                for i in l:
                    if i=='send'or i=='whatsapp' or i=='to':
                        continue
                    name+=i+' '

                dic={}
                try:
                    with open('contacts.txt','r') as f:
                        li=f.read().split('\n')
                        for i in li:
                            sub_li=i.split(':')
                            dic[sub_li[0]]=sub_li[1]

                except Exception:
                    speak('make sure you have a file in which all your contacts in the same folder')            
                
                for key,value in dic.items():
                    try:
                      import pywhatkit as kit  
                      if key in name:
                        value="+"+value
                        speak(f'ok what message should i write to {name}')
                        message=command().lower()
                        current_hour=datetime.datetime.now().hour
                        current_minute=datetime.datetime.now().minute
                        current_second=datetime.datetime.now().second
                        updated_second=current_second+3
                        speak('ok sending')
                        kit.sendwhatmsg(value,message,current_hour,current_minute,updated_second)
                        speak('your message is sent')
                    
                    except Exception:
                        speak('something is wrong')

            elif 'open gartic' in final_result:
                speak('opening garic...')
                chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                webbrowser.get(chrome_path).open("gartic.io")
                break

            elif 'open telegram' in final_result:
                speak('opening telegram...')
                dir="C:\\Users\\sharad\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe" 
                os.startfile(dir)

            elif 'open google duo' in final_result:
                speak('opening google duo')
                chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                webbrowser.get(chrome_path).open('https://duo.google.com/?web&utm_source=marketing_page_button_top')

            elif 'spotify' in final_result and 'play' not in final_result and 'on' not in final_result and 'close' not in final_result:
                try:
                    speak("opening spotify Enjoy your music!!")
                    dir="C:\\Users\\sharad\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Spotify.lnk"
                    pyautogui.hotkey('win','m')
                    os.startfile(dir)
                    time.sleep(1)
                    pyautogui.hotkey('win','up')
                    time.sleep(1.5)
                    pyautogui.press(' ')
                    while True:
                        internal_command=command().lower()
                        if 'close' in internal_command:
                            speak('ok closing spotify')
                            pyautogui.hotkey('alt','f4')
                            break
                        elif 'pause' in internal_command:
                            pyautogui.press(' ')        
                        elif 'play' in internal_command:
                            pyautogui.press(' ')    
                        elif 'shuffle' in internal_command:
                            pyautogui.hotkey('ctrl','s')
                        elif 'next' in internal_command:
                            pyautogui.hotkey('ctrl','right')   
                          
                
                except Exception:
                    speak('sorry I cannot find spotify in your system')

            elif 'on spotify' in final_result and 'close' not in final_result:
                sl=final_result.split(' ')
                song_name=''
                for i in sl:
                    if i=='play' or i=='on' or i=='spotify' or i=='jarvis':
                        continue
                    else:
                        song_name+=i+' '   
                pyperclip.copy(song_name)                     
                speak(f'ok playing {song_name} on spotify')
                pyautogui.hotkey('win','m')
                dir="C:\\Users\\sharad\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Spotify.lnk"
                os.startfile(dir)
                time.sleep(4.75)
                pyautogui.moveTo(299,21)
                pyautogui.click()
                time.sleep(1.25)
                pyautogui.hotkey('ctrl','v')
                time.sleep(2)
                pyautogui.moveTo(300,193)
                pyautogui.click()             

            elif 'open netflix' in final_result:
                speak("Neflix and chill sharad")
                chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                webbrowser.get(chrome_path).open("https://www.netflix.com/browse/")

            elif 'netflix' in final_result:
                li=final_result.split(' ')
                desired_video_name=''
                for i in li:
                    if i=='play' or i=='on' or i=='netflix' or i=='jarvis':
                        continue
                    else:
                        desired_video_name+=i+' '  
                pyautogui.hotkey('win','m')             
                speak(f'ok')
                try:
                    driver = webdriver.Chrome(ChromeDriverManager().install())
                    pyautogui.hotkey('win','up')
                    driver.get("https://www.netflix.com/in/Login")
                    username=driver.find_element_by_xpath('//*[@id="id_userLoginId"]')
                    password=driver.find_element_by_xpath('//*[@id="id_password"]')
                    sign_in_button=driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button')
                    username.send_keys('roti_2345@hotmail.com')
                    password.send_keys('batmaN3#')
                    time.sleep(1)
                    sign_in_button.click()
                    time.sleep(2)
                    profile=driver.find_elements_by_class_name('profile-link')[1]
                    profile_link=profile.get_attribute('href')
                    driver.get(profile_link)
                    time.sleep(1)
                    driver.get(f'https://www.netflix.com/search?q={desired_video_name}')
                    try:
                        desired_video=driver.find_element_by_xpath('//*[@id="title-card-0-0"]/div[1]/a')
                        desired_video_link=desired_video.get_attribute('href')
                        chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                        speak(f'ok playing {desired_video_name} on netflix')
                        driver.close()
                        webbrowser.get(chrome_path).open(desired_video_link)
                        break
                        
                    except Exception:
                        speak('there is no such video on netflix')    

                except Exception:
                    speak('sorry but something occurred wrong')      

            elif 'open gmail' in final_result:
                speak('opening gmail...')
                chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                webbrowser.get(chrome_path).open("https://mail.google.com/mail/u/0/#inbox") 
                
            elif 'second account' in final_result:
                speak('opening your second account')
                chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                webbrowser.get(chrome_path).open("https://mail.google.com/mail/u/1/#inbox")
                
            elif 'maps' in final_result:
                speak("opening google map") 
                chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                webbrowser.get(chrome_path).open("maps.google.com") 

            elif 'close' in final_result:
                pyautogui.hotkey('alt','f4')    
                
            elif 'open settings' in final_result:
                pyautogui.hotkey('win','i')
                time.sleep(1)
                pyautogui.hotkey('win','up')
            
            elif 'open file explorer ' in final_result:
                pyautogui.hotkey('win','e')
                
            elif 'best show' in final_result:
                speak("obviously it's dark")

            elif 'watch today' in final_result:
                speak("here is my recommendation...")
                dir="A:\\"
                li=os.listdir(dir)
                entertainment_list=[]
                for i in li:
                    if i=='$RECYCLE.BIN' or i=='HARVARD' or i=='System Volume Information' or i=='MUSIC':
                        continue
                    entertainment_list.append(i)
                number=random.randint(0,len(entertainment_list))
                sub_dir=f"A:\\{entertainment_list[number]}"
                sub_li=os.listdir(sub_dir)
                series=random.randint(0,len(sub_li))
                speak(f"I think you should watch {sub_li[series]}")
                time.sleep(1)
                speak(f'do you want me to open {sub_li[series]}?')
                while True:
                    respond=command().lower()
                    if 'yes' in respond:
                        speak(f'ok enjoy {sub_li[series]}')
                        pyautogui.hotkey('win','m')
                        dir=f"A:\\{entertainment_list[number]}\\{sub_li[series]}"
                        os.startfile(dir)
                        pyautogui.hotkey('win','up')
                        break
                    else:
                        speak('ok no problem')
                        break
                break        
                    
            elif 'new file' in final_result:
                speak("what name should i give to your file?")
                filename=command().lower()
                filename=filename+".txt"
                with open(filename,'w') as f:
                    speak("what content should i add in this file")
                    content=command().lower()
                    f.write(content)
                speak("your file is ready you can search the file in the search bar") 
                pyautogui.hotkey('win','m')
                pyautogui.press('win')   
                break

            elif 'set alarm' in final_result:
                speak('at what time do you want me to set an alarm')  
                alarm_time=command().lower()
                if len(alarm_time)==9:
                    if 'a.m.' in alarm_time:  
                        alarm_hours=alarm_time[:1]
                        alarm_minutes=alarm_time[2:4]  
                        final_alarm_time=alarm_hours+alarm_minutes
                    elif 'p.m.' in alarm_time:
                        alarm_hours=int(alarm_time[:1])+12
                        alarm_minutes=alarm_time[2:4]
                        final_alarm_time=str(alarm_hours)+alarm_minutes
                elif len(alarm_time)==10:
                    if 'a.m.' in alarm_time:
                        alarm_hours=alarm_time[:2]
                        if alarm_hours=='12':
                            alarm_hours="00"
                        alarm_minutes=alarm_time[3:5]
                        final_alarm_time=alarm_hours+alarm_minutes
                    elif 'p.m.' in alarm_time:
                        alarm_hours=alarm_time[:2]
                        if alarm_hours=="12":
                            alarm_hours=12
                        else:
                            alarm_hours=int(alarm_time[:2])+12
                        alarm_minutes=alarm_time[3:5]
                        final_alarm_time=str(alarm_hours)+alarm_minutes    
            
                speak('your alarm is set')
                while True:       
                    try:
                        current_hours=str(datetime.datetime.now().hour)
                        current_minutes=str(datetime.datetime.now().minute)
                        current_time=current_hours+current_minutes
                        if current_time==final_alarm_time:
                            dir="A:\\MUSIC\\therock.mp3"
                            playsound(dir)
                            break  
                    except Exception:
                        speak("the time you told me is not correct. Please tell me the time again")
                        break   

            elif 'weather' in final_result:
                try:
                    rate_of_words=engine.setProperty('rate',128)
                    li=final_result.split(' ')
                    venue=str(li[-1])
                    observation=pyowm.OWM('8d205e0bd57ba7df07a3b93ad0b6c5cc')
                    weather_of_venue=observation.weather_at_place(venue)
                    weather_object=weather_of_venue.get_weather()
                    temperature=weather_object.get_temperature('celsius')
                    average_temperature=str(temperature['temp'])+'degree celsius'
                    wind_speed_in_km_format=weather_object.get_wind()['speed']*3.6
                    wind_speed_in_km_format=str(wind_speed_in_km_format)+'kilometre per hour'
                    humidity=str(weather_object.get_humidity())
                    humidity=str(humidity[:4])+'%'
                    weather_status=str(weather_object.get_detailed_status())
                    speak(f'temperature of {venue} is {average_temperature} status is {weather_status} humidity is {humidity} wind speed is {wind_speed_in_km_format}')
                
                except Exception:
                    speak(f'Sorry i did not understand what you were saying')  

            elif "open google" in final_result:
                speak('opening google...')
                chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                webbrowser.get(chrome_path).open("google.com")
                
            elif 'open facebook' in final_result:
                speak('opening facebook...')
                chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                webbrowser.get(chrome_path).open("facebook.com")
                
            elif 'open twitter' in final_result:
                speak('opening twitter...')
                chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                webbrowser.get(chrome_path).open("twitter.com")
                
            elif 'open instagram' in final_result:
                speak('opening instagram...')
                chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                webbrowser.get(chrome_path).open("instagram.com") 

            elif 'like' in final_result:
                lo=final_result.split(' ')
                user=lo[-1]
                default_amount=1
                num_dic={'Two':2,'three':3,'six':6}
                speak(f'ok great how many photos you want to like of {user}')
                amount=command().lower()
                for k,v in num_dic.items():
                    if amount==k:
                        amount=v
                if amount.isdigit()==False:
                    amount=default_amount        
                speak(f'ok I am going to like {amount} photos of {user}')        
                try:
                    driver = webdriver.Chrome(ChromeDriverManager().install())
                    pyautogui.hotkey('win','up')
                    driver.get("https://www.instagram.com/")
                    time.sleep(2)
                    log_in_facebook=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[5]/button/span[2]')
                    log_in_facebook.click()
                    username=driver.find_element_by_xpath('//*[@id="email"]')
                    username.send_keys('8171271221')
                    password=driver.find_element_by_xpath('//*[@id="pass"]')
                    password.send_keys('Peoplesschamp')
                    sign_in=driver.find_element_by_xpath('//*[@id="loginbutton"]')
                    sign_in.click()
                    time.sleep(25)
                    no_notification=driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
                    no_notification.click()
                    search_bar=driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div/div/span[2]')
                    insta_dictionary={}
                    with open('insta_usernames.txt','r') as f:
                        insta_li=f.read().split('\n')
                        for i in insta_li:
                            insta_sub_li=i.split(':')
                            insta_dictionary[insta_sub_li[0]]=insta_sub_li[1]
                    try:        
                        for key,value in insta_dictionary.items():
                            if key in user:
                                search_bar.click()
                                pyautogui.typewrite(value)
                                time.sleep(2)
                                first_search=driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]/div')
                                first_search.click()
                                time.sleep(10)
                    except Exception:
                        speak(f'there is no name called {user} in the file. Please try with valid names')
                                   
                    try:
                        first_image=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div/div[2]')
                    except Exception:
                        first_image=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a/div/div[2]')
                    first_image.click()
                    time.sleep(4)
                    i=0
                    flag=0
                    while i<=amount:
                        time.sleep(2)
                        image_status=driver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > div > span > svg')
                        like_status=image_status.get_attribute('aria-label')
                        if like_status=='Like':
                            image_status.click()
                            i+=1
                        if i==amount:
                            flag+=1
                            break    
                        next_image=driver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.EfHg9 > div > div > a._65Bje.coreSpriteRightPaginationArrow')
                        next_image.click()  
                except Exception:
                    speak('something is wrong please try again later!!')
                
                try:
                    if flag>0:
                        speak('Hey! Sharad I have liked the photos')
                        driver.close()   
                except Exception:
                    speak('Sorry! but loading speed is too slow please try again')

            elif 'story of' or 'profile of' in final_result:
                ll=final_result.split(' ')
                username=ll[-1]
                insta_dic={}
                with open('insta_usernames.txt','r') as f:
                    li=f.read().split('\n')
                    for i in li:
                        sub_li=i.split(':')
                        insta_dic[sub_li[0]]=sub_li[1]
                for key,value in insta_dic.items():
                    if 'story of' in final_result:
                      if key in username:
                        speak(f'ok opening the instagram story of {username} ')
                        chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                        webbrowser.get(chrome_path).open(f"instagram.com/stories/{value}/") 
                        time.sleep(3)
                        pyautogui.moveTo(x=751,y=312)
                        time.sleep(2)
                        pyautogui.click()

                    elif 'profile of ' in final_result:
                        if key in username:
                            speak(f'ok opening the profile of {username} ')
                            chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                            webbrowser.get(chrome_path).open(f"instagram.com/{value}/") 

        else:
            speak("your system is not connected to your network. Please connect it to the network and restart me again")  
            break

    return render_template('shutdown.html')     
                
if __name__ == '__main__':
   app.run(debug=True)    
    
                        
                



    
    
   


        
    
         


     

    
    



    
    
