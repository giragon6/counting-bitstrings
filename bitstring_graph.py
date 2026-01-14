import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.figure import Figure

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
  bsgraph = BitstringGraph(["110"])
  bsgraph.print_recs()
