import requests
from bs4 import BeautifulSoup

# formulating url for rotten tomatoes page
actor = input("Enter the number of the actor: ")
quer = "".join(i+"_" for i in actor.split(' '))[:-1]
content = requests.get("https://www.rottentomatoes.com/celebrity/"+quer).text

# getting all the data from website
soup = BeautifulSoup(content, 'html.parser')

try:
    # extracting the data we need from the soup
    films = soup.find("table", {"data-qa":"celebrity-filmography-movies"}).find_all("td", {"class":"celebrity-filmography__title"})
    years = soup.find("table", {"data-qa":"celebrity-filmography-movies"}).find_all("td", {"class":"celebrity-filmography__year"})

    # compiling the data together
    filmography = []
    for film, year in zip(films,years):
        filmography.append([film.get_text().strip('\n'),year.get_text().strip('\n')])

    # sorting the movies in descending order
    for i in range(0, len(filmography)):
        for j in range(0, len(filmography)-i-1):
            if (filmography[j][1] < filmography[j + 1][1]):
                    temp = filmography[j]
                    filmography[j] = filmography[j + 1]
                    filmography[j + 1] = temp

    # printing the movies
    print(f"\nThe filmography of {actor}:\n")
    for film in filmography:
        print(f"{film[0]} ({film[1]})\n")

except AttributeError:
     # In case the URL is wrong, the actor's name isn't correctly input by the user
     print("\nEnsure you've typed the name of the actor correctly!\n")