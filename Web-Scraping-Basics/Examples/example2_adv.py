import requests
from bs4 import BeautifulSoup
import multiprocessing 
import time

def backup(num,queue):
    while len(queue) != 0 :
        if num == 0: #If num of process is 0 start from the first item in queue
            link = queue.pop(0)
        else:
            link = queue.pop(len(queue) - 2*num) #If num is not 0 then remove a kinda random item
        page = requests.get(f'https://en.wikipedia.org/{link}')
        soup = BeautifulSoup(page.content,'html.parser')
        links = soup.find_all('a',{'href':True})
        for a in links:
            href = a['href']
            if '/wiki/' in href and ':' not in href and '?' not in href and '//' not in href:
                if href not in crawled and href not in queue and href != link:
                    queue.append(href)
        crawled.add(link)
        print(f'thread:{num}  link:{link}   queue:{len(queue)}   crawled:{len(crawled)}')

if __name__ == '__main__':
    process = list() #Init process list
    crawled = set() #Init crawled set

    manager = multiprocessing.Manager() #Init Manager -- Manager enables memory sharing between processing so they can manipulate the same queue
    queue = manager.list() #Init sharing list
    queue.append('/wiki/Mia_Khalifa') #Append first link

        t = multiprocessing.Process(target=backup,args=(i,queue)) #Init processes
    for i in range(8): #8 processes
        process.append(t)

    for num,t in enumerate(process):
        t.start() #Start processes
        if num == 0: #Let the other processes to wait in order to add some links to queue
            time.sleep(2)  

    for t in process: 
        t.join() #Wait untill every process is finished
            