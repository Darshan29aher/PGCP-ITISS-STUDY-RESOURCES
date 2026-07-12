from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

@app.route('/api/lookup', methods=['POST'])
def lookup_domain():
    domain = request.json.get('domain')
    # VULNERABLE: The 'domain' input is directly inserted into 
    #the os.system call.
    os.system('ping -c 1 ' + domain)
    return "Server Response : Successfully executed given command!!"

if __name__ == "__main__":
    #app.run(host="0.0.0.0",port=5000) # EC2 on AWS
    #app.run(host="127.0.0.1",port=5000) # local machine
    app.run(host="192.168.1.11",port=5000) # local machine