# 3rd parth dependencies
from flask import Flask
from flask_cors import CORS

# project dependencies
from deepface import DeepFace
from deepface.api.src.modules.core.routes import blueprint
from deepface.commons.logger import Logger

logger = Logger()


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(blueprint)
    logger.info("All registered routes:")
    for rule in app.url_map.iter_rules():
        logger.info(f"  {rule.rule} -> {rule.endpoint} [{', '.join(rule.methods)}]")

    logger.info(f"Welcome to DeepFace API test v{DeepFace.__version__}!")
    return app
