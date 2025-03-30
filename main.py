from flask import Flask, json, jsonify
from dotenv import load_dotenv
from flask_cors import CORS
import os

load_dotenv()

app = Flask(__name__)

CORS(app)

@app.route("/", methods=["GET"])
def home():
  my_env = os.getenv('MY_ENV')
  try:
    with open('test.json', 'r', encoding='utf-8') as file:
      data = json.load(file)  
      data["myenv"] = my_env
      return jsonify(data) 
  except Exception as e:
    return jsonify({"error": str(e)}), 500  # Manejo de errores
  
  return my_env if my_env else 'no-env :('

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5001, debug=True)