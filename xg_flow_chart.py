#import packages
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
df = pd.read_csv("file8.csv")
print(df)
a_xG = [0]
h_xG = [0]
a_min = [0]
h_min = [0]
a_xGc = []
h_xGc = []
k = 0
j = 0
hteam = df['team'].iloc[0]
ateam = df['team'].iloc[-1]
for x in range(len(df['xg'])):
    if df['team'][x]==ateam:
        a_xG.append(df['xg'][x])
        a_min.append(df['minute'][x])
    if df['team'][x]==hteam:
        h_xG.append(df['xg'][x])
        h_min.append(df['minute'][x])
xyz = 0
for i in range(len(a_xG)):
    xyz = xyz + a_xG[i]
print("Away team xG is", xyz)
abc = 0
for i in range(len(h_xG)):
    abc = abc + h_xG[i]
print("Home team xG is", abc)
for i in range(0, len(a_xG)):
    j += a_xG[i]
    a_xGc.append(j)
#print(a_xGc[i])
for i in range(0, len(h_xG)):
    k += h_xG[i]
    h_xGc.append(k)
fig, ax = plt.subplots(figsize=(10, 5))
fig.set_facecolor('#3d4849')
ax.patch.set_facecolor('#3d4849')
plt.xticks([0, 15, 30, 45, 60, 75, 90])
plt.xlabel("Minutes")
plt.ylabel('xG')
ax.step(x=a_min, y=a_xGc, color='#d3d3d3', label=ateam, linewidth=5, where='post')
ax.step(x=h_min, y=h_xGc, color='#fd3607', label=hteam, linewidth=5, where='post')
plt.show()



