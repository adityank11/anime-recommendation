# from mal import AnimeSearch

# search = AnimeSearch("cowboy bebop")
# print(search.results[0].title)

# from mal import Anime
# anime = Anime(mal_id=5)   # Cowboy Bebop
# print(anime.image_url)




# def fetch_poster(anime_id):
#     headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
#     webpage=requests.get(f'https://myanimelist.net/anime/{anime_id}',headers=headers).text
#     soup = BeautifulSoup(webpage,'lxml')
#     anime_url = soup.find_all('meta',property="og:image")
#     poster_link = anime_url[0]['content']
#     return poster_link
