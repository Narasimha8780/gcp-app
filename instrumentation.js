// instrumentation.js
const { NodeSDK } = require('@opentelemetry/sdk-node');
const { getNodeAutoInstrumentations } = require('@opentelemetry/auto-instrumentations-node');
const { TraceExporter } = require('@google-cloud/opentelemetry-exporter-gcp-trace');
const { Resource } = require('@opentelemetry/resources');
const { SemanticResourceAttributes } = require('@opentelemetry/semantic-conventions');

const sdk = new NodeSDK({
  resource: new Resource({
    // 1. SET YOUR SERVICE NAME HERE
    [SemanticResourceAttributes.SERVICE_NAME]: 'gcp-app', 
    [SemanticResourceAttributes.SERVICE_NAMESPACE]: 'production',
  }),
  // 2. EXPORT TO GOOGLE CLOUD TRACE
  traceExporter: new TraceExporter(), 
  instrumentations: [getNodeAutoInstrumentations()],
});

sdk.start();
