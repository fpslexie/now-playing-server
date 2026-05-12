from flask import Flask, request, jsonify

app = Flask(**name**)

# Храним текущий трек
current_track = {
    "artist": "—",
    "title": "Ничего не играет"
}


@app.route('/now', methods=\['GET'\])
def get_now():
    return jsonify(current_track)

@app.route('/update', methods=\['POST'\])
def update_track():
    global current_track
    data = request.json
    current_track = {
        "artist": data.get("artist", "Unknown"),
        "title": data.get("title", "Unknown")
    }
    print(f"Обновлено: {current_track}")
    return jsonify({"status": "ok"})

@app.route('/')
def home():
    return f'''
    <h1>Now Playing</h1>
    <p>Сейчас играет: <b>{current_track\["artist"\]} – {current_track\["title"\]}</b></p>
    <p><a href="/now">Открыть как JSON</a></p>
    '''

if **name** == '**main**':
    app.run(host='0.0.0.0', port=10000)
