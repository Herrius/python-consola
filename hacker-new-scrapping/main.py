from bs4 import BeautifulSoup
import requests

def main():
    response= requests.get('https://news.ycombinator.com/')
    yc_web_page=response.text
    soup=BeautifulSoup(yc_web_page,'html.parser')
    array_title=[]
    array_points=[]
    title=soup.find_all('a',class_='titlelink')
    points=soup.find_all('span',class_='score')
    for text in title:
        array_title.append(text.getText())
    for text in points:
        array_points.append(int(text.getText().split()[0]))
    max_value=max(array_points)
    pos_max_value=array_points.index(max_value)
    max_vote_news=array_title[pos_max_value]
    print(max_vote_news,max_value)
main()