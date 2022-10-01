from http import HTTPStatus

from flask import Flask


class HttpMockSampleServer:
    def __init__(self):
        app = Flask(__name__)

        @app.route('/sample/person/', methods=['GET'])
        def get_sample_person():
            return "/sample/person GET method!", HTTPStatus.OK

        @app.route('/sample/person/', methods=['POST'])
        def post_sample_person():
            return "/sample/person POST method!", HTTPStatus.CREATED

        @app.route('/sample/person/', methods=['PUT'])
        def put_sample_person():
            return "/sample/person PUT method!", HTTPStatus.ACCEPTED

        @app.route('/sample/person/', methods=['PATCH'])
        def patch_sample_person():
            return "/sample/person PATCH method!", HTTPStatus.ACCEPTED

        @app.route('/sample/person/', methods=['DELETE'])
        def delete_sample_person():
            return "/sample/person DELETE method!", HTTPStatus.OK

        @app.route('/', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
        def error_sample_person():
            return "Hack your brain!", HTTPStatus.BAD_REQUEST

        app.run(host='127.0.0.1', port=105)
