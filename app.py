from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def accueil():
    return """
    <h1>talsk</h1>

    <form method="POST" action="/recevoir">
        <input name="message1" placeholder="message1">
        <input name="message2" placeholder="message2">
        <input name="message3" placeholder="message3">

        <button type="submit">Envoyer</button>
    </form>
    """

@app.route("/recevoir", methods=["POST"])
def recevoir():
    message1 = request.form.get("message1")
    message2 = request.form.get("message2")
    message3 = request.form.get("message3")

    print("Message 1 :", message1 )
    print("Message 2 :", message2)
    print("Message 3 :", message3)
  retur "les 3 messages on etait recu"
