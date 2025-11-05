from flask import Flask, render_template, request, jsonify
import aiml

app = Flask(__name__)

kernel = aiml.Kernel()
kernel.learn("brain1.aiml")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    response = kernel.respond(user_message)
    if not response:
        response = "I'm not sure how to respond to that yet."
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)
