from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/")
def home():
    return "Hit List 3.0 Backend is running!"

@app.route("/jit/prob_ev", methods=["POST"])
def prob_ev():
    data = request.get_json()
    game_id = data.get("game_id", "N/A")
    market = data.get("market")
    selection = data.get("selection")
    price = float(data.get("price"))

    # Example EV logic (replace later with model)
    base_prob = 0.55
    price_decimal = 1 + (100 / abs(price)) if price < 0 else (price / 100 + 1)
    fair_odds_decimal = round(1 / base_prob, 3)
    ev = round(((base_prob * price_decimal) - 1) * 100, 2)

    if ev >= 8:
        confidence = "strong"
    elif ev >= 4:
        confidence = "medium"
    else:
        confidence = "low"

    return jsonify({
        "market": market,
        "selection": selection,
        "price_american": price,
        "price_decimal": price_decimal,
        "prob": base_prob,
        "fair_odds_decimal": fair_odds_decimal,
        "ev": ev,
        "confidence": confidence
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

