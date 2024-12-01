from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Loading JSON data into a list.
try:
    with open("characters.json", "r") as file:
        characters = json.load(file)
except FileNotFoundError:
    print("the characters.json file not found.")


# Get all characters and paginate them.
@app.route("/characters", methods=["GET"])
def get_characters():
    """
    Retrieve a paginated list of characters from the JSON data.

    Query Parameters:
    - limit (int): The maximum number of items to return. Default is 3.
    - skip (int): The number of items to skip from the beginning of the list. Default is 3.

    Returns:
    - JSON response containing the paginated list of characters.
    - HTTP status code 200.
    """
    try:
        trim_upper_bound = int(request.args.get("limit", 3))
        trim_lower_bound = int(request.args.get("skip", 0))
    except ValueError:
        return jsonify({"error": "Invalid limit or skip value"}), 400

    # to avoid out-of-bound errors we make sure that we are not exceeding the limit of our list.
    max_limit = min(trim_lower_bound + trim_upper_bound, len(characters))

    paginated = []

    # Append characters from the chosen range (pagination) to the list.
    for i in range(trim_lower_bound, max_limit):
        paginated.append(characters[i])

    return jsonify(paginated), 200    # converting my dictionary to a JSON for the API as useful HTTP response.

# get an specific character by its ID   C_R_UD - By ID
@app.route("/characters/<int:id>", methods=["GET"])
def get_character_by_id(id):
    """
    Retrieve a specific character by its ID.

    Args:
    id (int): The ID of the character to retrieve.

    Returns:
    - JSON response containing the character data if found.
    - HTTP status code 200 if the character is found.
    - JSON response with an error message if the character is not found.
    - HTTP status code 404 if the character is not found.
    """
    for single_character in characters:
        if single_character["id"] == id:
            return jsonify(single_character), 200  # converting my dictionary to a JSON for the API as useful HTTP response.
    return jsonify({"error": "Character not found"}), 404   # the character does not exist in my list



if __name__ == "__main__":
    app.run(debug=True)