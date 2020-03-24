import requests
from bs4 import BeautifulSoup

def backup():
    while len(queue) != 0 : #While links in queue repeat
        link = queue[0] #Get first link
        page = requests.get(f'https://en.wikipedia.org/{link}') #Send a request to site
        soup = BeautifulSoup(page.content,'html.parser') 
        links = soup.find_all('a',{'href':True}) #Find all <a> tags with href
        for a in links: #Loop links
            href = a['href'] #Get href 
            if '/wiki/' in href and ':' not in href and '?' not in href and '//' not in href: #Check if its a valid link
                if href not in crawled and href not in queue: #Check if there is already in queue or crawled
                    queue.append(href) #Append to queue
        crawled.add(queue.pop(0)) #Remove link from queue and add it to crawl
        print(f'link:{link}   queue:{len(queue)}   crawled:{len(crawled)}') #Print progress to user

if __name__ == "__main__":
    queue = list() #Init queue
    crawled = set() #Init crawled
    queue.append('/wiki/Mia_Khalifa') #Starting link
    try:
        backup() #Start looping
    except KeyboardInterrupt: #When you press Ctrl+C write everything to file
        with open('./links.txt','a') as file: #Open file
            for link in queue: #Loop through queue
                try:
                    file.write(link + '\n' + crawled.pop() + '\n') #Write queue link and crawled link
                except:
                    file.write(link + '\n') #If there is no links in crawled there is an exception and write only queue link
