class Movie:
    def __init__(self, title, release_year, story_year):
        self.__title = title
        self.__release_year = release_year
        self.__story_year = story_year

    def get_title(self):
        return self.__title

    def get_release_year(self):
        return self.__release_year

    def get_story_year(self):
        return self.__story_year

    def set_title(self, title):
        self.__title = title

    def set_release_year(self, release_year):
        self.__release_year = release_year

    def set_story_year(self, story_year):
        self.__story_year = story_year


movies = []


try:
    with open('MarvelMovies.csv', 'r') as file:
        for line in file:
            values = line.strip().split(',')

            movie = Movie(values[0], values[1], values[2])
            movies.append(movie)

except FileNotFoundError:
    print('Error: File not found')
except:
    print('Error: An unknown error occurred')


movies.sort(key=lambda x: x.get_title())

print('{:<30} {:<10} {}'.format('Title', 'Release', 'Storyline'))
for movie in movies:
    print('{:<30} {:<10} {}'.format(movie.get_title(), movie.get_release_year(), movie.get_story_year()))