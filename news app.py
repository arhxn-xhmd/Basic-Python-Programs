import requests
import json
print('\t  𝗧𝗛𝗘 𝗗𝗔𝗜𝗟𝗬 𝗖𝗛𝗥𝗢𝗡𝗜𝗖𝗟𝗘')
categories = ['business','entertainment','general','health','science','technology','sports','politics','climate change']
url = "https://newsapi.org/v2/top-headlines"
api_key = 'e9aa0ff7de3a416c96ed89132c2683e0'
print('\nYou want to see business news, entertainment news, general news, health news, science news, technology news, sports news or political news?')
print('\n0 for Business news\n1 for Entertainment news\n2 for general news\n3 for health news\n4 for science\n5 for technology news\n6 for sports news\n7 for political news\n10 for others')
user_choice = int(input('\nEnter your choice here : '))
if (user_choice != 10) :
    params1 = {
        'apiKey' : api_key, 
        'category' : categories [user_choice]
    }
    response = requests.get(url, params=params1)
    data = response.json()
    if data['articles'] :
        for article in data['articles'] :
            print('\n' + article['title'])
            print (article['description'] + '\n')
            print('------------------------------------------')
        
    else :
        print('No new articles found')
elif (user_choice == 10) :
    query = input('\nEnter the topic on which you want to see  news : ')
    params2 = {
        "apiKey": api_key,
        "q": query}
    response = requests.get(url, params=params2)
    data = response.json()
    if data['articles'] :
        for article in data['articles'] :
            print('\n' + article['title'])
            print (article['description'] + '\n')
            print('------------------------------------------')
    else :
        print('No new articles found')