from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "App SecureDev funcionando. Prueba /hello?name=Estudiante"

@app.route('/hello')
def hello():
    name = request.args.get('name', 'Invitado')
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)