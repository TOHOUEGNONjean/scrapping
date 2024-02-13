import requests
from bs4 import BeautifulSoup

urls ='https://beninwebtv.com/pays/afrique/afrique-de-louest/benin/?tdb-loop-page='

def scrap_page(urls):
    for i in range(1, 10):
        url = urls+str(i)
        lien = requests.get(url)
        soup = BeautifulSoup(lien.content,"html.parser")
        titre = soup.find('title').text
        sous_titre = soup.find_all('div', class_ = 'tdc-row')
        with open("rendu.txt", "a") as f:
            f.write(str(i) +' '+titre+'\n\n')

        for val in sous_titre:
            h = val.find("h3", class_ = "td_block_wrap")
            if h:
                #resultat.append(h.text.strip())
                with open("rendu.txt", "a") as f:
                    f.write(h.text.strip() +'\n')

scrap_page(urls)
