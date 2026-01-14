from flask import Flask, jsonify, render_template, request
from bitstring_graph import BitstringGraph

app = Flask(__name__)

@app.route("/graph.json")
def graph_json():
  forbidden: str | None = request.args.get('forbidden', type=str)
  if forbidden == None:
    raise ValueError("No forbidden bitword submitted!")
  forbidden_list = forbidden.split(',')
  bs = BitstringGraph(forbidden_list)
  return jsonify(bs.to_cytoscape())
  
@app.route("/")
def main():
  return render_template("index.html")

if __name__ == "__main__":
    app.run()