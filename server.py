from flask import Flask, request, jsonify
import os
from main import pogup

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute_script():
    data = request.json
    script_path = data.get('script_path')

    if not script_path:
        return jsonify({"error": "script_path é necessário"}), 400

    if not os.path.exists(script_path):
        return jsonify({"error": "Arquivo não encontrado"}), 404

    try:
        stdout, stderr = run_script(script_path)
        return jsonify({"stdout": stdout, "stderr": stderr}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)  # Replit padrão para web