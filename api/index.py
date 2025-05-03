badnames = [
    "FAG", "fag",
]


@app.route('/api/v1/CheckForBadName', methods=['POST', 'GET'])
def CheckForBadName():
    data = request.get_json()

    name = data.get("FunctionArgument", {}).get("name")
    forRoom = data.get("FunctionArgument", {}).get("forRoom")

    userid = data.get("CallerEntityProfile",
                      {}).get("Lineage", {}).get("MasterPlayerAccountId", "None")

    return jsonify({"result": 0})
