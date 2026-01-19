from flask import Flask, jsonify, render_template, request, send_file
from counting_bitstrings.bitstring_graph import BitstringGraph

app = Flask(__name__)

bsgraph = None

def get_bsgraph(forbidden: list) -> BitstringGraph:
  global bsgraph
  if bsgraph == None or not bsgraph.constraints == forbidden:
    bsgraph = BitstringGraph(forbidden)
  return bsgraph

@app.route("/graph.json")
def graph_json():
  forbidden: str | None = request.args.get('forbidden', type=str)
  if forbidden == None:
    raise ValueError("No forbidden bitword submitted!")
  forbidden_list = forbidden.split(',')
  bs = get_bsgraph(forbidden_list)
  return jsonify(bs.to_cytoscape())

@app.route("/get-term")
def get_term():
  n: int | None = request.args.get('n', type=int)
  if n == None:
    raise ValueError("No term number submitted!")
  forbidden: str | None = request.args.get('forbidden', type=str)
  if forbidden == None:
    raise ValueError("No forbidden bitword submitted!")
  forbidden_list = forbidden.split(',')
  res = get_bsgraph(forbidden_list).get_term_explicitly(n)
  return jsonify(res)

@app.route("/get-sequence")
def get_sequence():
  num_terms: int | None = request.args.get('numTerms', type=int)
  if num_terms == None:
    raise ValueError("No number of terms submitted!")
  forbidden: str | None = request.args.get('forbidden', type=str)
  if forbidden == None:
    raise ValueError("No forbidden bitword submitted!")
  forbidden_list = forbidden.split(',')
  bs = get_bsgraph(forbidden_list)
  sequence = []
  for i in range(num_terms):
    t = bs.get_term(i)
    sequence.append(t)
  return jsonify(sequence)
  
@app.route("/")
def main():
  return render_template("index.html")

@app.route("/overview")
def overview():
    return send_file('static/overview.pdf', mimetype='application/pdf')

if __name__ == "__main__":
    app.run()