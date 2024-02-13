import requests
import pandas as pd

class DataRepositories:

    def __init__(self, owner):
        self.owner = owner
        self.api_base_url = 'https://api.github.com'
        self.access_token='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'
        self.headers = {'Authorization': 'Bearer ' + self.access_token,
            'X-GitHub-Api-Version' : '2022-11-28'}
        
    def repositories_list(self):
        repos_list = []

        for page_num in range(1, 20):
            try:
                url = f'{self.api_base_url}/users/{self.owner}/repos?page={page_num}'
                response = requests.get(url, headers=self.headers)
                #print(response.text)
                repos_list.append(response.json())
            except:
                repos_list.append(None)

        return repos_list

    def repositories_names (self, repos_list): 
        repo_names=[] 
        for page in repos_list:
            for repo in page:
                try:
                    repo_names.append(repo['name'])
                except: 
                    pass

        return repo_names

    def repositories_languages (self, repos_list):
        repo_languages=[]
        for page in repos_list:
            for repo in page:
                try:
                    repo_languages.append(repo['language'])
                except:
                    pass

        return repo_languages

    def create_df_languages(self):

        repositories = self.repositories_list()
        names = self.repositories_names (repositories)
        languages = self.repositories_languages(repositories)

        dataFrame = pd.DataFrame()
        dataFrame['repository_name'] = names
        dataFrame['language'] = languages

        return dataFrame
    

amazon_rep = DataRepositories('amzn')
languages_amzn = amazon_rep.create_df_languages()


netflix_rep = DataRepositories('netflix')
languages_netflix = netflix_rep.create_df_languages()

spotify_rep = DataRepositories('spotify')
languages_spotify = spotify_rep.create_df_languages()

#Saving data

languages_amzn.to_csv('data/amzn_languages.csv')
languages_netflix.to_csv('data/netflix_languages.csv')
languages_spotify.to_csv('data/spotify_languages.csv')


