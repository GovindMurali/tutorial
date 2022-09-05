16
import lxml as lxml
from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
import lxml
#scrape shots #16441
base_url = 'https://understat.com/match/'
match = str(input("Please enter the match id"))
url = base_url + match
print(url)
res = requests.get(url)
soup = BeautifulSoup(res.content, 'lxml')
#to scrape shotData
scripts = soup.find_all('script')
strings = scripts[1].string
print(strings)
#strip unnecessary symbols
ind_start = strings.index("('")+2
ind_end = strings.index("')")
json_data = strings[ind_start:ind_end]
print(json_data)
json_data = json_data.encode('utf8').decode('unicode_escape')
data = json.loads(json_data)
print(data)
x = []
y = []
xg = []
team = []
minute = []
result = []
player = []
data_away = data['a']
data_home = data['h']
for i in range(len(data_home)):
    for j in data_home[i]:
        if j == "X":
            x.append(data_home[i][j])
        if j == "Y":
            y.append(data_home[i][j])
        if j == "xG":
            xg.append(data_home[i][j])
        if j == 'h_team':
            team.append(data_home[i][j])
        if j == 'minute':
            minute.append(data_home[i][j])
        if j == 'result':
            result.append(data_home[i][j])
        if j == 'player':
            player.append(data_home[i][j])
for i in range(len(data_away)):
    for j in data_away[i]:
        if j == "X":
            x.append(data_away[i][j])
        if j == "Y":
            y.append(data_away[i][j])
        if j == "xG":
            xg.append(data_away[i][j])
        if j == 'a_team':
            team.append(data_away[i][j])
        if j == 'minute':
            minute.append(data_away[i][j])
        if j == 'result':
            result.append(data_away[i][j])
        if j == 'player':
            player.append(data_away[i][j])
col_names =['x','y','xg','team','minute','result','player']
df = pd.DataFrame([x,y,xg,team,minute,result,player], index=col_names)
df = df.T
df.to_csv('file8.csv')
print(df)
#xg_h = 0.00
#for i in range(len(data_home)):
 #     xg_h = xg_h + float((xg[i]))
#print("Home team xG is", xg_h)
#xg_a = 0.000
#for i in range(0, len(data_away)):
 #    xg_a = xg_a + float((xg[i]))
#print("Away team xG is", xg_a)




