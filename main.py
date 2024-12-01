from flask import Flask, request, jsonify, json

app = Flask(__name__)

# Loading JSON data into an in-memory Python list.
with open("characters.json", "r") as file:
    characters = json.load(file)

# Get all characters and paginate them.  C_R_UD
@app.route("/characters", methods=["GET"])
def get_characters():
    limit = int(request.args.get("limit", 2))
    skip = int(request.args.get("skip", 0))
    paginated = []
    end_index = min(skip + limit, len(characters))
    for i in range(skip, end_index):
        paginated.append(characters[i])
    return jsonify(paginated), 200


if __name__ == "__main__":
    app.run(debug=True)