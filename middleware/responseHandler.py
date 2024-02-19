from flask import jsonify
from flask_babel import  _


def response_handler(message, status_code, data = {}):
    translated_message = _(message)

    status_code = _("True") if status_code == 200 else _("False")
    
    response = {
        'status' : status_code,
        'message': translated_message,
        'data': data
    }
    return jsonify(response), status_code
