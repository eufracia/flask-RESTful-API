from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    todos = [
        {'todo': 'clean up garage', 'time': 2},
        {'todo': 'buy some presents', 'time': 1}
     ]

    return jsonify(todo=todos)

if __name__ == '__main__':
    app.run(debug=True)
