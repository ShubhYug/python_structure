from flask_swagger_ui import get_swaggerui_blueprint
from flask import  send_from_directory

def setup_swagger_ui(app):
    SWAGGER_URL = '/api/docs'  # URL for accessing the Swagger UI page
    API_URL = '/api_doc/swagger.yaml'  # URL to your API documentation JSON file

    swagger_ui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Your API Name"
        }
    )

    app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

    @app.route('/api_doc/swagger.yaml')
    def send_swagger_json():
        print()
        return send_from_directory('api_doc', 'swagger.yaml')
