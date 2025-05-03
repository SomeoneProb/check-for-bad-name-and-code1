import flask
from flask import Flask, request, jsonify

app = Flask(__name__)

badnames = [
    "FAG",
]


@app.route('/api/CheckForBadName', methods=['POST', 'GET'])
def CheckForBadName():
    data = request.get_json()

    name = data.get("FunctionArgument", {}).get("name")
    forRoom = data.get("FunctionArgument", {}).get("forRoom")

    userid = data.get("CallerEntityProfile",
                      {}).get("Lineage", {}).get("MasterPlayerAccountId", "None")

    return jsonify({"result": 0})
