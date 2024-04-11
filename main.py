from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if data['ref'] == 'refs/heads/master':
        subprocess.run('git pull', shell=True)  # Exécute un git pull lorsque des commits sont poussés sur la branche master
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
