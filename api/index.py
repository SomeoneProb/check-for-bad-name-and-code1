import requests
import random
from flask import flask, jsonify, request

app = flask(__name__)

@app.route("/api/v1/CheckForBadName", methods=["POST"])
def check_for_bad_name():
    rjson = request.get_json().get("FunctionResult")
    name = rjson.get("name").upper()

    if name in ["KKK", "PENIS", "NIGG", "NEG", "NIGA", "MONKEYSLAVE", "SLAVE", "FAG", 
        "NAGGI", "TRANNY", "QUEER", "KYS", "DICK", "PUSSY", "VAGINA", "BIGBLACKCOCK", 
        "DILDO", "HITLER", "KKX", "XKK", "NIGA", "NIGE", "NIG", "NI6", "PORN", 
        "JEW", "JAXX", "TTTPIG", "SEX", "COCK", "CUM", "FUCK", "PENIS", "DICK", 
        "ELLIOT", "JMAN", "K9", "NIGGA", "TTTPIG", "NICKER", "NICKA", 
        "REEL", "NII", "@here", "!", " ", "JMAN", "PPPTIG", "CLEANINGBOT", "JANITOR", "K9", 
        "FAGGOT",
        "H4PKY", "MOSA", "NIGGER", "NIGGA", "IHATENIGGERS", "@everyone", "TTT"]:
        return jsonify({"result:" 2})
    else:
        return jsonify({"result:" 0})
    
