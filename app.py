from flask import Flask, render_template, request, jsonify
import pandas as pd
import random

app = Flask(__name__)
df = pd.read_csv("mood_tracks.csv")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    mood = request.form.get("mood")
    matched = df[df['mood'] == mood]
    if matched.empty:
        return jsonify(["No songs found for this mood."])
    songs = matched.sample(n=min(5, len(matched)))
    return jsonify([f"{row['name']} - {row['artists']}" for _, row in songs.iterrows()])

# if __name__ == "__main__":
#     app.run(debug=True)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)