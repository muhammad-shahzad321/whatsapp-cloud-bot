from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/bot", methods=["POST"])
def bot():
    # User ka message
    user_msg = request.form.get("Body").lower()

    # Reply banate hain
    reply = MessagingResponse()
    msg = reply.message()

    # Simple rules
    if "hi" in user_msg or "hello" in user_msg:
        msg.body("Assalam-o-Alaikum 👋\nMain Shahzad ka WhatsApp Bot hoon!\nHow can I help you today?")
    elif "name" in user_msg:
        msg.body("Mera naam Shahzad Bot hai 🤖")
    elif "help" in user_msg:
        msg.body("Main aapki madad kar sakta hoon.\nType karein:\n1. Info\n2. Contact\n3. Exit")
    elif "info" in user_msg:
        msg.body("Yeh Shahzad ka official WhatsApp chatbot hai — available 24/7 ✅")
    else:
        msg.body("Mujhe samajh nahi aaya 😅\nTry typing 'help' or 'hi'.")


    return str(reply)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, WhatsApp Bot is Running!"

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, WhatsApp Bot is Running!"

if __name__ == "__main__":
    app.run()

