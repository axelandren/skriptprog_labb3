import requests, json


class ManageFiles:
    def __init__(self):
        self.my_url = 'http://www.omdbapi.com/?apikey=5f248365&'

    def search(self, search):
        link = self.my_url + 's=' + search
        response = requests.get(link)
        data = response.json()
        if data['Response'] == 'True':
            results = data['Search']
            if int(data['totalResults']) > 1:
                for t in range(len(results)):
                    print(f"{t+1}: {results[t]['Title']}")
                self.show_movie_info(results)
            elif int(data['totalResults']) == 1:
                for r in data['Search']:
                    print(r)
        else:
            print('No results found')

        input('\nPress Enter to continue\n')

    def prev_results(self, previous):
        print()
        for c in range(len(previous)):
            print(f'{c+1}: {previous[c]}')
        while True:
            answer = input('\nDo you want to search for one of these again? yes/no: ')
            if answer.lower() == 'yes' or answer.lower() == 'y':
                while True:
                    index = input('\nSelect search by index number: ')
                    try:
                        new_search = previous[int(index) - 1]
                        self.search(new_search)
                        break
                    except ValueError as ve:
                        print(ve)
                    except IndexError as ie:
                        print(ie)
            elif answer.lower() == 'no' or answer.lower() == 'n':
                break
            else:
                input('Wrong input, press Enter to try again')

    def show_movie_info(self, results):
        while True:
            index = input('\nSelect movie by index number: ')
            try:
                movie_url = results[int(index) - 1]['imdbID']
                response = requests.get(self.my_url + 'i=' + movie_url)
                data = response.json()
                print(json.dumps(data, indent=4))
                break
            except ValueError as ve:
                print(ve)
            except IndexError as ie:
                print(ie)
