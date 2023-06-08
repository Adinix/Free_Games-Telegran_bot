import requests
from bs4 import BeautifulSoup as BS


#! main-block
def free_games():

    #* Values
    dict_free_games = dict()
    dict_image_games = dict()
    list_name_games = list()
    headers= {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    }

    req = requests.get("https://freesteam.ru/category/steam/", headers=headers)

    soup = BS(req.text, 'lxml')

    box_free = soup.find_all('div', class_='col-lg-4 col-md-4 three-columns post-box')

    list_box_free_game = list()
    for i in box_free:
        s = i.find('a', href="https://freesteam.ru/category/active/")
        if s:
            list_box_free_game.append(i)

    #* sites main block
    list_img_games = list()
    list_free_game_examination = list()
    for i in list_box_free_game:

        #* get_link_sites_free_game
        s = i.find('a', class_="thumb-link")

        req_game = requests.get(s['href'], headers=headers)
        soup = BS(req_game.text, 'lxml')

        link_game = soup.find('div', 'entry-content')
        link_game = link_game.find('a')

        list_free_game_examination.append(link_game['href'])

        #* get_game_name
        name_game = i.find('h2', class_='entry-title').find('a')

        name_game = str(name_game.text).replace('Раздача ', '').replace(' для Steam', '').replace(' + DLC', '')

        list_name_games.append(name_game)

        #* get_game_img
        img_game = i.find('img')
        list_img_games.append(img_game['data-src'])


    #* get link steam game
    k = 0
    for i in list_free_game_examination:
        req = requests.get(i, headers=headers)
        soup = BS(req.text, 'lxml')

        free_game = soup.find('a', class_='btn_green_steamui btn_medium')
        if free_game != None:
            free_game = free_game.find('span')

            if free_game.text.strip() == 'Add to Account':
                dict_free_games[list_name_games[k]] = i
                dict_image_games[list_name_games[k]] = list_img_games[k]
                k += 1


    return [dict_free_games, dict_image_games]


if __name__ == '__main__':
    free_games()