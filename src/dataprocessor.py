import requests
from procutils import *

url = "https://gt-scheduler.github.io/crawler-v2/"

# all finalized terms, 202408 (fall 2024) isn't finalized yet
r = requests.get(url)
terms = r.json()['terms']

finalized = []
for term in terms:
    if term['finalized']:
        # print(term['term'])
        finalized.append(term['term'])

# look into @cache

# now we have all terms for which course data is finalized - can process each of their trees upfront?
t = "202402"
r2 = requests.get(url + t + ".json").json()
# x = r2["courses"]["AE 2010"]


d = {}
for course in r2["courses"]:
    # print(len(course[2]))
    # print(len(r2["courses"][course][2]))
    q = getDependentTrees(r2["courses"], course)

    d[course] = len(q) # maximum number of dependent trees, sort by that

# topologically sorted by dependent trees
sortedD = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}

# print(sortedD)
# for k,v in sortedD.items():
#     kids = r2["courses"][k][2]
    # print(f"{k} {v}")
# print(sortedD)

for k,v in sortedD.items():
    buildTree(r2["courses"][k], k)
