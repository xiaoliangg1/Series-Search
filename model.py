import ast
import urllib.request



all_epi = []
user_epi = []


class NotFoundError(Exception):
    """Raise when series not found or unspecific enough."""
    pass


class Model:

    def __init__(self):
        self.List_of_epi = []
        self.select_epi = []

    def open_url(self, url):
        """A function turn the b string which return from a url into usable data
        type."""
        response = urllib.request.urlopen(url)
        inf = response.read()
        response.close()
        inf = inf.decode('utf-8')
        inf = ast.literal_eval(inf)
        return inf

    def user_search(self, search):
        """A function that get user input and print out all episodes in the
        show"""
        self.search = str(search.replace(' ', '+'))
        # Check if the input is a show which storage in the url, else tell
        # the user input again.
        try:
            url = 'http://www.omdbapi.com/?t=' + self.search
            url += '&episodes&apikey=8ae9454b'
            data = self.open_url(url)
            # A loop that go thought all the seasons in the show.
            for i in range(1, int(data['totalSeasons']) + 1):
                # Skip season that is not storage in the data base.
                try:
                    url = 'http://www.omdbapi.com/?t=' + self.search
                    url += '&type=series&season=' + str(i) + '&apikey=8ae9454b'
                    epi = self.open_url(url)
                    # Check if the episodes excess.
                    if epi['Response'] == 'True':
                        # Turn the information in the data base to readable
                        # format.
                        for j in epi['Episodes']:
                            k = {'Season': i, 'Episodes': j['Episode'],
                                 'Title': j['Title']}
                            all_epi.append(k)
                            self.List_of_epi.append(k)
                except:
                    pass
            return search
        except:
            raise NotFoundError()
            # give error when it is not found in data base or title is
            # too board

    def storage(self):
        for i in range(len(self.select_epi)):
            season = self.select_epi[i][8:10]
            rseason = ''
            for j in season:
                if j.isdigit():
                    rseason += j
            episode = self.select_epi[i][20:23]
            repisode = ''
            for j in episode:
                if j.isdigit():
                    repisode += j
            url1 = 'http://www.omdbapi.com/?t=' + self.search
            url1 += '&type=series&season='
            url1 += rseason + '&episode=' + repisode
            url1 += '&plot=short&apikey=8ae9454b'
            print(url1)
            epi = self.open_url(url1)
            
            if epi['Response'] == 'True':
                statement = 'Title: ' + epi['Title'] + ', Season: '
                statement += epi['Season']
                statement += ', Episode: ' + epi['Episode'] + ', Plot: '
                statement += epi['Plot'] + '\n'
                self.select_epi[i] = statement
        return self.select_epi
            
            

    def save_file(self, path1):
        f = open(path1, 'w')
        for i in self.select_epi:
            f.write(i)
        f.close()
