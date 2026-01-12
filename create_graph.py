import matplotlib.pyplot as plt
import networkx as nx
from graph import Graph
from numpy import inf

class BitstringGraph:
  def __init__(self, constraints):
    self.constraints = constraints
    self.g = nx.DiGraph()
    
    k = max([len(c) for c in constraints])

    self.suffixes = [""]

    for i in range(k-1):
      new_suffixes = []
      for s in self.suffixes:
        if s+"0" not in constraints:
          new_suffixes.append(s+"0") 
        if s+"1" not in constraints:
          new_suffixes.append(s+"1") 
      self.suffixes = new_suffixes
      
    for s in self.suffixes:
      self.g.add_node(s)
      for t in self.suffixes:
        if s + t[-1] not in constraints and s[1::] + t[-1] == t:
          self.g.add_edge(s, t)
          
    self.adj = nx.to_dict_of_lists(self.g)
    
    self.recs = {s: [] for s in self.adj}
      
    for s in self.adj:
      for k in self.adj[s]:
          self.recs[k].append((s,1))
    
  def show(self):
    nx.draw_networkx(self.g)
    plt.show()
    
  def print_recs(self):
    for s in self.recs.keys():
      print(f"{s}(n)={'+'.join([f"{r[0]}(n-{r[1]})" for r in self.recs[s]])}")

constraints = ["000","11"]
bsgraph = BitstringGraph(constraints)
bsgraph.print_recs()
bsgraph.show()