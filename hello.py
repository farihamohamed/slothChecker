from flask import Flask, jsonify
import psutil
import time
 
app = Flask(__name__)


@app.route("/")
def main():
    return "<p>Welcome to Slow Check</p>"



@app.route("/cpu")
def cpu_percent(): 
    time.sleep(1) #stimulating a delay 
    cpu_percent = psutil.cpu_percent(interval=1)
    return jsonify({"type": "cpu", "data": cpu_percent})  # Return as JSON so frontend can process
 

@app.route("/memory")
def memory_usage(): 
    memory = psutil.virtual_memory()
    return jsonify({"type": "memory", "data": memory.percent})  # Return as JSON
 

if __name__ == '__main__': 
    app.run(debug=True)