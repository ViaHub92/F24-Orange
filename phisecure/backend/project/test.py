from flask import Flask

app = Flask(__name__)

@app.route('/students')
def students():
    return {'students': ["Hunter", "Ethan", "Joshua", "Ralph", "Dylan"]}

if __name__ == "__main__":
    app.run(debug=True)