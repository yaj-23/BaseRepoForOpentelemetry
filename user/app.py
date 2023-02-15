import requests
from flask import Flask, jsonify
from opentelementry import trace
from opentelementry.sdk.trace import TracerProvider
from opentelementry.sdk.trace.export import(
    BatchSpanProcessor, 
    ConsoleSpanExporter,
)

provider = TracerProvider()
processor = BatchSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(processor)
trace.set_tracker_provider(provider)

tracer=trace.get_tracer(__name__)


app=Flask(__name__)

@app.route('/user/profile')
def get_user_profile():
    user={
        "userId": "1234",
        "email": "user@example.com",
        "organization": "example.com"
    }
    return jsonify(user)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)