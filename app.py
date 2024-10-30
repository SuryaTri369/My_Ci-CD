from flask import Flask, jsonify,request

app = Flask(__name__)

# Sample data
items = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
]

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items', methods=['POST'])
def add_item():
    new_item = request.json
    items.append(new_item)
    return jsonify(new_item), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

