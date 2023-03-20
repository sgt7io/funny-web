import flask
from flask import Flask
import random

app = Flask(__name__)

jokes = [
    "Relationship status? I'll leave the relations to the database.",
    "How do you get the code for the bank vault? You checkout their branch.",
    "Why did the security conscious engineer refuse to pay their dinner bill? Because they could not verify the checksum.",
    "How many Prolog programmers does it take to change a lightbulb? Yes."
]
@app.get('/')
def tell_a_joke():
    joke = random.choice(jokes)
    return flask.render_template('joke.html', joke_text=joke)
    #return f"<p>{joke}</p>"
