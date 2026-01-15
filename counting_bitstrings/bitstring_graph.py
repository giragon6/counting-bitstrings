import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.figure import Figure

class BitstringGraph:
  def __init__(self, constraints):
    self.constraints = constraints
    self.g = nx.DiGraph()
    
    lengths = [len(c) for c in constraints]
    k = max(lengths)
    unique_lengths = list(set(lengths))

    self.suffixes = [""]

    for i in range(k-1):
      new_suffixes = []
      for s in self.suffixes:
        legal0 = True
        legal1 = True
        for l in unique_lengths:
          print(s + "0 and " + s + "1")
          if s[l-1::]+"0" in constraints or (len(s) == l-1 and s+"0" in constraints):
            legal0 = False
          if s[l-1::]+"1" in constraints or (len(s) == l-1 and s+"1" in constraints):
            legal1 = False
        if legal0:
          new_suffixes.append(s+"0") 
        if legal1:
          new_suffixes.append(s+"1") 
      self.suffixes = new_suffixes
      
    for s in self.suffixes:
      self.g.add_node(s)
      for t in self.suffixes:
        if s + t[-1] not in constraints and s[1::] + t[-1] == t:
          self.g.add_edge(s, t)
          
    self.adj = nx.to_dict_of_lists(self.g)
    
    self.recs = {(s,0): [] for s in self.adj}
      
    for s in self.adj:
      for k in self.adj[s]:
          self.recs[(k,0)].append((s,1))
    
  def show(self):
    nx.draw_networkx(self.g)
    plt.show()
    
  def to_cytoscape(self):
    nodes = [{"data": {"id": n}} for n in self.g.nodes()]
    edges = [{"data": {"source": u, "target": v}} for u, v in self.g.edges()]
    return {"nodes": nodes, "edges": edges}
    
  def print_recs(self):
    for s in self.recs.keys():
      print(f"{s[0]}(n)={'+'.join([f"{r[0]}(n-{r[1]})" for r in self.recs[s]])}")
      
if __name__ == "__main__":
  bsgraph = BitstringGraph(["1010", "11"])
  bsgraph.print_recs()
  bsgraph.show()
