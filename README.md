# Web Scraping
Le script suivant est un exemple de web scraping réalisé en Python, utilisant les bibliothèques requests, BeautifulSoup, et re pour extraire des données d'un site web spécifique. Dans cet exemple, nous illustrons comment extraire les titres et les sous-titres d'articles d'un site d'actualités, en l'occurrence **"beninwebtv.com"** .

Voici une explication ligne par ligne :

## Importation des modules nécessaires :

**requests** : Module pour envoyer des requêtes HTTP.
**BeautifulSoup** : Une bibliothèque pour extraire des données à partir de fichiers HTML et XML.
* Définition de l'URL de base :
La variable urls contient l'URL de base du site à partir duquel les données seront extraites. L'URL inclut une variable de pagination **?tdb-loop-page=**.
Définition de la fonction **scrap_page(urls)** :
Cette fonction prend l'URL de base en argument.
* Elle parcourt les pages numérotées de 1 à 9 (définies dans la boucle for i in range(1, 10)) en concaténant le numéro de page à l'URL de base.
Pour chaque page, elle envoie une requête HTTP à l'URL correspondante.
* Elle utilise BeautifulSoup pour analyser le contenu HTML de la page.
* Elle extrait le titre de la page à l'aide de **soup.find('title').text** et les sous-titres à l'aide de soup.find_all('div', class_ = 'tdc-row').
* Les titres de page et les sous-titres sont écrits dans un fichier texte nommé  **"rendu.txt"** .
Appel de la fonction scrap_page(urls) avec l'URL de base en argument


# TOHOUEGNON Jean-Baptiste
