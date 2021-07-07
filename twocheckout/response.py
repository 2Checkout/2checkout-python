import json


# helper file for parsing response from 2Checkout API in order to return an standard response
def parse(data):
    # if invalid JSON, exception is thrown
    data_params = json.loads(data)

    if 'error_code' in data_params:
        response = {'meta': {'status': 'fail', 'message': data_params['message']}, 'body': data_params}
    elif 'Errors' in data_params and data_params['Errors'] is not None:
        message = ''
        for key in data_params['Errors']:
            message += data_params['Errors'][key]

        response = {'meta': {'status': 'fail', 'message': message}, 'body': data_params}
    else:
        response = {'meta': {'status': 'success', 'message': 'ok'}, 'body': data_params}

    return response


def get(data):
    return json.loads(data)
