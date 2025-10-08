from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hit List 3.0 Backend is running!"

@app.route("/bet", methods=["POST"])
def place_bet():
    data = request.json
    # Example logic (replace this later with your betting model)
    response = {
        "status": "success",
        "message": f"Bet placed on {data.get('team')} for ${data.get('amount')}."
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
