from flask import Flask

app = Flask(__name__)

# Define your route with strict_slashes set to False
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

if __name__ == "__main__":
    # Make your application listen on 0.0.0.0, port 5000
    app.run(host="0.0.0.0", port=5000)
