from flask import Flask, request
import py_eureka_client.eureka_client as eureka_client

port = 8000
eureka_client.init(eureka_server="http://localhost:8761/eureka",
                   app_name="payment-ms",
                   instance_port=port)

app = Flask(__name__)

@app.route("/info", methods=['GET'])
def hello():
    return "Hello from payment-ms (Python/Flask)"

if __name__ == "__main__":
    print(f">> Running payment-ms on port {port}")
    app.run(host='0.0.0.0', port = port)