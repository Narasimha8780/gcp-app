# app.py
from flask import Flask
import os

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.cloud_trace import CloudTraceSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.semconv.resource import ResourceAttributes
from opentelemetry.instrumentation.flask import FlaskInstrumentor

resource = Resource.create({
    ResourceAttributes.SERVICE_NAME: "gcp-app",
    ResourceAttributes.SERVICE_NAMESPACE: "production"
})

provider = TracerProvider(resource=resource)
trace.set_tracer_provider(provider)

cloud_trace_exporter = CloudTraceSpanExporter()
provider.add_span_processor(BatchSpanProcessor(cloud_trace_exporter))

tracer = trace.get_tracer(__name__)

app = Flask(__name__)

FlaskInstrumentor().instrument_app(app)

@app.route("/")
def hello():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask Hello World</title>
        <style>
            body { font-family: Arial, sans-serif; background-color: #f0f0f0; text-align: center; padding: 100px; }
            h1 { color: #333; }
        </style>
    </head>
    <body>
        <h1>Hello, World! branch-push-test-is-successful-for-CI-CD</h1>
    </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 9090))
    app.run(host="0.0.0.0", port=port)
