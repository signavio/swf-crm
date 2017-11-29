from flask import Flask, abort, request

import json

app = Flask(__name__)

descriptor = None
data = None

with open("./descriptor.json") as f:
    descriptor = json.loads(f.read())

with open("./data.json") as f:
    data = json.loads(f.read())

@app.route("/")
def get_descriptor():
    return json.dumps(descriptor)

def merge(source, target):
  result = source.copy()
  result.update(target)

  return result

@app.route("/<kind>/options")
def get_options(kind):
    if kind not in data:
        abort(404)

        return

    nameField = "name"

    if kind == "customer" or kind == "customer-en":
        nameField = "fullName"

    options = [ merge(v, { "name": v[nameField] }) for (k, v) in data[kind].iteritems() ]

    query = request.args.get("filter", "").lower()

    if query:
        options = filter(lambda option: query in option["name"].lower() or query in option["code"], options)

    return json.dumps(sorted(options, key= lambda option: option["name"].lower()))

@app.route("/<kind>/options/<id>")
def get_option(kind, id):
    if kind not in data:
        abort(404)

        return

    options = data[kind]

    if id not in options:
        abort(404)

        return

    entry = options[id]
    nameField = "name"

    if kind == "customer" or kind == "customer-en":
        nameField = "fullName"

    return json.dumps(merge(entry, {  "name": entry[nameField] }))

@app.route("/<kind>/<id>")
def get_entry(kind, id):
    if kind not in data:
        abort(404)

        return

    options = data[kind]

    if id not in options:
        abort(404)

        return

    entry = options[id]

    return json.dumps(entry)


if __name__ == "__main__":
    app.run()
