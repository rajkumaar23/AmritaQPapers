import prettytable
import webbrowser
import requests
import itertools
import threading
import time
import sys
import datetime
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from time import sleep
from sys import exit
from os import system, name

stack_url=[]
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def year(url):
    clear()
    year_url=url
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content,'html.parser')
        div=soup.findAll('div', xmlns="http://di.tamu.edu/DRI/1.0/")
        ul=div[0].findAll('ul')
        li=ul[0].findAll('li')
        hyper=li[0].a['href']
        url='http://dspace.amritanet.edu:8080/'
        url+=hyper
        page = requests.get(url)
        soup = BeautifulSoup(page.content,'html.parser')
        t=PrettyTable(['No','Subjects']) 
        div=soup.findAll('div', class_="file-list")
        subdiv=div[0].findAll('div',class_="file-wrapper clearfix")
        for i in range(len(subdiv)):
            title=subdiv[i].findAll('div')
            span=title[1].div.findAll('span')
            t.add_row([i+1,span[1]['title']])
        t.add_row([len(subdiv)+1,"Back"])
        t.align='l'
        print(t)
        while(True):
            ch=int(input("Enter your choice: "))
            if(ch>0 and ch<=len(subdiv)):
                title=subdiv[ch-1].findAll('div')
                link=title[0].a['href']
                url='http://dspace.amritanet.edu:8080/'
                url+=link
                break
            elif(ch == len(subdiv)+1):
                semchoose(stack_url.pop())

            else:
                print("Please enter a valid input!")
    except:
        print("UNEXPECTED ERROR! :(")
        exit()
    print("Please wait till the browser opens ! ")
    webbrowser.open(url, new=0, autoraise=True)
    ch=int(input('Do you want to continue ? \nPress 1 for Yes and 0 for No : '))
    if(ch==0):
        exit()
    else:
        year(year_url)

def semchoose(url):
    clear()
    try:
        params_url =url
        page = requests.get(url)
        soup = BeautifulSoup(page.content,'html.parser')

        t=PrettyTable(['No','Available Assessments'])  
        div=soup.findAll('div', id="aspect_artifactbrowser_CommunityViewer_div_community-view")
        ul=div[0].findAll('ul')
        if(len(ul)>1):
            li=ul[1].findAll('li')
        else:
            li=ul[0].findAll('li')

        for i in range(len(li)):
            t.add_row([i+1,li[i].a.text.strip()])

        t.add_row([len(li)+1, "Back"])
        t.align = "l"

        print(t)  
        while(True):
            ch=int(input("Enter your choice: "))
            if(ch>0 and ch<=len(li)):
                url='http://dspace.amritanet.edu:8080/'
                url+=li[ch-1].a['href']
                break
            elif(ch == len(li)+1):
                sem_table(stack_url.pop())
            else:
                print("Please enter a valid input !")
    except:
        print("\nUNEXPECTED ERROR ! :( ")
        sleep(3)
        exit()
    stack_url.append(params_url)
    year(url)


def sem_table(url):
    clear()
    try:
        stack_url.append(url)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        t = PrettyTable(['No', 'Semesters'])
        div = soup.findAll('div', id="aspect_artifactbrowser_CommunityViewer_div_community-view")
        li = div[0].ul.findAll('li')

        for i in range(len(li)):
            t.add_row([i + 1, li[i].a.text.strip()])
        t.add_row([(len(li) + 1), "Back"])
        t.align = "l"
        print(t)
        while (True):
            ch = int(input("Enter your semester : "))

            if (ch > 0 and ch <= len(li)):
                url = 'http://dspace.amritanet.edu:8080/'
                url += li[ch - 1].a['href']
                break
            elif (ch == len(li) + 1):
                start()
            else:
                print("Please enter a valid input !")
    except Exception as e:
        print("\nUNEXPECTED ERROR ! :( ")
        sleep(3)
        exit()
    semchoose(url)


def start():
    clear()
    url="http://dspace.amritanet.edu:8080/xmlui/handle/123456789/"
    try:    
        page = requests.get(url)
        print("\n")
        t=PrettyTable(['No','Courses'])
        t.add_row(["1","B.Tech"])
        t.add_row(["2","BA Communication"])
        t.add_row(["3","MA Communication"])
        t.add_row(["4","Integrated MSc & MA"])
        t.add_row(["5","MCA"])
        t.add_row(["6","MSW"])
        t.add_row(["7","M.Tech"])
        t.add_row(["8","Exit"])
        t.align="l"
        print(t)
        while(True):
            print("\n")
            ch=int(input("Enter your choice : "))
            if(ch<9 and ch>0):
                if(ch==1) : 
                    url+="150"
                elif(ch==2) : 
                    url+="893"
                elif(ch==3) : 
                    url+="894"
                elif(ch==4) : 
                    url+="903"
                elif(ch==5) : 
                    url+="331"
                elif(ch==6) : 
                    url+="393"
                elif(ch==7) : 
                    url+="279"
                elif (ch==8):
                    exit()
                break
            else:
                print("Please enter a valid input ! ")
    except Exception as e:
        print("\nOOPS! There was an unexpected error.\nExiting in few seconds... ")
        sleep(4)
        exit()
    sem_table(url)




url="http://dspace.amritanet.edu:8080"
print("\nHELLO! Ever wanted to use Amrita Repository on PC ? \nWell, here's my Python Script that does the same job as the app. \nHave a look at your question papers without wasting time !! \n")
print("Please ensure you're connected to Amrita Wi-Fi for a smooth experience :)\n")
print("Report bugs to : rajkumaar2304@gmail.com")
now = datetime.datetime.now()
print("(c) "+str(now.year)+" Rajkumar\n")
done=10
for c in itertools.cycle(['|', '/', '-', '\\']):
    if not(done):
        break
    sys.stdout.write('\rPlease wait..' + c)
    sys.stdout.flush()
    done=done-1
    time.sleep(0.1)
sys.stdout.flush()
start()
