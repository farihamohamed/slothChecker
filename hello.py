from flask import Flask 
import psutil
import time
 
app = Flask(__name__)

def run_cpu_script():
    time.sleep(1)
    cpu_percent = psutil.cpu_percent(interval=1)
    return f'{cpu_percent}%'


def run_mem_script():
    return  psutil.virtual_memory()



@app.route("/")
def main():
    return "<p>Welcome to Slow Check</p>"



@app.route("/cpu")
def cpu_percent(): 
    my_time = run_cpu_script()
    return f"Current CPU  is {my_time}"
 

@app.route("/memory")
def memory_usage(): 
    my_memory = run_mem_script()
    return f'Used Memory:{my_memory[3]}'  
 