from flask import Flask, render_template, request, jsonify
from app.chatbot import RecyclingChatbot

app = Flask(__name__)
chatbot = RecyclingChatbot()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    message = request.json["message"]
    response = chatbot.handle_query(message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)