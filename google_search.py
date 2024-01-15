# pip install beautifulsoup4
# pip install google
from googlesearch import search
b = int(input("Search Range: "))
for a in range(b):
    query = "Search Term" # Enter Search Term
    for i in search(query, stop=5, num=5, pause=0):
        print(i)
