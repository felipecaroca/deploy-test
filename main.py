from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS
import os

load_dotenv()

app = Flask(__name__)

CORS(app)

@app.route("/", methods=["GET"])
def home():
  my_env = os.getenv('MY_ENV')
  return my_env if my_env else 'no-env :('

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5001, debug=True)