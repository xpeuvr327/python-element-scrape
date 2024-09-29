import requests
import bs4
import lxml

element = input('What element would you want to know the name of? ')
url = f'https://www.rsc.org/periodic-table/element/{element}/'
res = requests.get(url)
soup = bs4.BeautifulSoup(res.text, 'lxml')
div = soup.find('span', {"class": "element_header"})
if div:
    text = div.text.strip()
    text = ' '.join(text.split())
    print(f"The name of the element with atomic number {element} is {text}.")
else:
    print("Element not found on the page.")import requests
import bs4
import lxml

element = input('What element would you want to know the name of? ')
url = f'https://www.rsc.org/periodic-table/element/{element}/'
res = requests.get(url)
soup = bs4.BeautifulSoup(res.text, 'lxml')
div = soup.find('span', {"class": "element_header"})
if div:
    text = div.text.strip()
    text = ' '.join(text.split())
    print(f"The name of the element with atomic number {element} is {text}.")
else:
    print("Element not found on the page.")
