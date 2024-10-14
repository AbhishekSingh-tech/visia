import json
from flask import Flask, jsonify, request
from prediction import predict
from model_instance import ModelProvider
from processor_instance import ProcessorProvider

application = Flask(__name__)
model_instance_object = ModelProvider()
processor_instance_object = ProcessorProvider()
model = model_instance_object.load_model()
processor = processor_instance_object.load_processor()

@application.route('/')
@application.route('/status')
def status():
    return jsonify({'status': 'ok'})


@application.route('/predictions', methods=['POST'])
def create_prediction():
    data = request.data or '{}'
    body = json.loads(data)
    return jsonify(predict(model, processor, body))
