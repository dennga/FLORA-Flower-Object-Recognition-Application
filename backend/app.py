from flask import Flask, jsonify

# App-Instanz erstellen
app = Flask(__name__)

# API-Endpunkt definieren
@app.route('/api/status', methods=['GET'])
def get_status():
    # Eine JSON-Antwort zurückgeben
    return jsonify({
        "status": "ok",
        "message": "FLORA API ist online!"
    })

# Server starten
if __name__ == '__main__':
    app.run(debug=True)