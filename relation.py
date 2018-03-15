import pandas as pd
import json
class node(object):
    def __init__(self, name, id):
        self.name = name
        self.id = id

class relation(object):
    def __init__(self, pearon, spearman):
        self.pearon = pearon
        self.spearman = spearman

class link(object):
    def __init__(self, s, d, relation):
        self.s = s
        self.d = d
        self.relation = relation
class all2json(object):
    def __init__(self, nodes, links):
        self.nodes = nodes
        self.links = links
df = pd.read_csv('cars.csv',sep=',')
del df['Model']
del df['Origin']
#del df['Year']
print(df)
nodes = []
column_name = [column for column in df]
for i in range(len(column_name)):
    nodes.append(node(column_name[i], i))
#print(json.dumps(nodes, default=lambda obj : obj.__dict__))
links = []
pearsons = df.corr()
print(pearsons)
# print(pearsons['MPG']['Cylinders'])
spearmans = df.corr('spearman')
print(spearmans)
# print(spearmans['MPG']['Cylinders'])
for i in range(len(column_name)-1):
    for j in range(i+1,len(column_name)):
        links.append((link(s=i, d=j, relation= relation(pearon=pearsons[column_name[i]][column_name[j]],spearman=spearmans[column_name[i]][column_name[j]]))))
all_data = all2json(nodes,links)
print(all_data)
with open('1.txt','w') as f:
    json.dump(all_data,f,default=lambda obj : obj.__dict__)



