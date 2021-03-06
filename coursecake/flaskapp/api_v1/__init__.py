# packaging for api_v1
from flask import Blueprint
from flask_restx import Api

# Import namespaces
from .hello import api as nsHello
from .courses import api as nsCourses

blueprint = Blueprint("api_v1", __name__, url_prefix="/api/v1")

api = Api(
    blueprint,
    title="CourseCake",
    version="1.0",
    description="Reworked API using Flask-RestX"
    )

api.add_namespace(nsHello)
api.add_namespace(nsCourses)
