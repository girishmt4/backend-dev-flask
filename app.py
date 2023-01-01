from flask import Flask

app = Flask(__name__)


@app.get("/hello")
def hello_world():
    return "Hello World"


@app.get("/fancy")
def hello_fancy():
    return """
        <html>
        <body>
        <h1>
            Greetings!!
        </h1>
        <p>
            Hello, there! 
        </p>
        </body>
        </html>
    """
