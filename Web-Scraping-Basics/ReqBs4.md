# Simple tutorial on requests and BeautifulSoup

## Requests
Requests is a python library used for sending HTTP requests 

You can install the library by typing to the terminal:

```python
pip install requests
```
To use the library just import it 
```python
import requests
```

For this tutorial you will just need the HTTP GET method
```python
response = requests.get('https://www.iee.ihu.gr')
```
You can get the HTML by typing:
```python
response.content
```

If the HTML from the request is not the same with the site, try adding a User Agent. Pick a common user agent.This is just an example
```python
header = {
'User-agent':'Mozilla/5.0'
}
response = requests.get('https://www.iee.ihu.gr', headers=header)
```


## BeautifulSoup
BeautifulSoup is a library used for parsing html. Think of it as a simple way to search through HTML.

Installing BeautifulSoup
```python
pip install BeautifulSoup4
```

Importing BeautifulSoup
```python
from bs4 import BeautifulSoup
```

Functions
```python
find_all()
find()
```

### Using BeautifulSoup and Requests
```python
page = requests.get('https://www.iee.ihu.gr')
soup = BeautifulSoup(page.content,'html.parser')
body = soup.find('body')
print(body)
#Result: <body> ... </body>
```
You can make the result more readable by doing:
```python
print(body.prettify())
```

Examples:

```python
page = requests.get('http://www.iee.ihu.gr')
soup = BeautifulSoup(page.content,'html.parser')
tables = soup.find_all('table', {'class':'className'})
```

You can get the specific attribute data from a tag by doing:
```python
div = soup.find('div',{'class':'className'})
style = div['style']
id = div['id']
```
