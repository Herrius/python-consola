from bs4 import BeautifulSoup
import requests


def main():
    URL='https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

    response= requests.get(URL)
    empire_website=response.text
    soup=BeautifulSoup(empire_website,'html.parser')
    movies=soup.find_all('h3',class_='title')
    movies_list=[movie.getText() for movie in movies]
    movies_list=movies_list[::-1]
    with open('list.txt','w', encoding='utf-8') as list:
        for movie in movies_list:
            list.write(f"{movie} \n")
main()