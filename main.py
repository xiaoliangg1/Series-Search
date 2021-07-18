"""A function that search user inputted show and storage the five especial they
select into a .cvs file."""


import ast
import urllib.request
import os.path


def open_url(url):
    """A function turn the b string which return from a url into usable data
    type."""
    response = urllib.request.urlopen(url)
    inf = response.read()
    response.close()
    inf = inf.decode('utf-8')
    inf = ast.literal_eval(inf)
    return inf


def user_search():
    """A function that get user input and print out all episodes in the show"""
    search = input('Enter the title of series:\n')
    search = str(search.replace(' ', '+'))
    # Check if the input is a show which storage in the url, else tell the user
    # input again.
    try:
        url = 'http://www.omdbapi.com/?t=' + search
        url += '&episodes&apikey=8ae9454b'
        data = open_url(url)
        # A loop that go thought all the seasons in the show.
        for i in range(1, int(data['totalSeasons']) + 1):
            # Skip season that is not storage in the data base.
            try:
                url = 'http://www.omdbapi.com/?t=' + search
                url += '&type=series&season=' + str(i) + '&apikey=8ae9454b'
                epi = open_url(url)
                # Check if the episodes excess.
                if epi['Response'] == 'True':
                    # Turn the information in the data base to readable format.
                    for j in epi['Episodes']:
                        print('Season:', i, 'Episodes:',
                              j['Episode'], 'Title:', j['Title'])
            except:
                pass
        return search
    except:
        print('The series does not exist. Please be more specific.')
        user_search()


def storage(search):
    """A function that take user inputted episode and storage into a list."""
    l = []
    u = 0
    h = 0
    # Check the user input is valid
    while u != 1:
        # Run the loop 5 times
        while h != 5:
            try:
                season = int(input('Input the season number:\n'))
                episode = int(input('Input the episode number:\n'))
                l.append(season * 100 + episode)
                u = 1
                h += 1
            except:
                print('The value is not an integer.')
                u = 0
    l.sort()
    # Get all the plot information for each episode.
    for i in range(len(l)):
        url1 = 'http://www.omdbapi.com/?t=' + search + '&type=series&season='
        url1 += str(l[i]//100) + '&episode=' + str(l[i] % 100)
        url1 += '&plot=short&apikey=8ae9454b'
        epi = open_url(url1)
        # turn each element
        if epi['Response'] == 'True':
            statement = 'Title: ' + epi['Title'] + ', Season: ' + epi['Season']
            statement += ', Episode: ' + epi['Episode'] + ', Plot: '
            statement += epi['Plot'] + '\n'
            l[i] = statement
        # Print out a error message when one of the episode is not in data
        # base.
        else:
            print('One or more season and episode number don\'t match.')
            print('Please try entering again.')
            global series_search
            return 1
    return l


def save_file(lst):
    """A function to turn the episode list into a .csv file"""
    nameFile = input('Please name the file: ')
    pathInput = input('Please input path of the directory you want to'
                      ' save the file in:\n')
    # Print out a error message when the part is not valid.
    try:
        compname = os.path.join(pathInput, nameFile+'.csv')
        f = open(compname, 'w')
        for i in lst:
            f.write(i)
        f.close()
        print('The data has been stored in the desired file.')
    except:
        print('Either the file name or the path is invalid.')
        print('Please choose another file name or path.')
        return 1


def menu():
    """Main function to call the whole program."""
    series_search = user_search()
    namelst = storage(series_search)
    while namelst == 1:
        namelst = storage(series_search)
    file = save_file(namelst)
    while file == 1:
        file = save_file(namelst)


if __name__ == '__main__':
    menu()
