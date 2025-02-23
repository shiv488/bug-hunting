from flask import Flask, render_template, request, jsonify
import subprocess
import os

app = Flask(__name__)

# Function to run shell commands
def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    target = request.form['target']
    scan_type = request.form['scan_type']
    
    if scan_type == "subdomain":
        command = f"subfinder -d {target}"
    elif scan_type == "port":
        command = f"nmap -sV {target}"
    elif scan_type == "xss":
        command = f"dalfox url {target}"
    elif scan_type == "sql":
        command = f"sqlmap -u {target} --batch --risk=3 --level=5"
    else:
        return jsonify({"error": "Invalid scan type"})
    
    output = run_command(command)
    return jsonify({"result": output})

if __name__ == '__main__':
    app.run(debug=True)
