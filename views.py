from flask import Blueprint, render_template, send_from_directory
from flask_graphql import GraphQLView

from schema import schema


views_endpoints = Blueprint("views", __name__, template_folder="templates")


@views_endpoints.route("/")
def index():
    return render_template("index.html")


@views_endpoints.route("/graphql", methods=["GET", "POST"])
def graphql():
    return GraphQLView.as_view("graphql", schema=schema, graphiql=True)()


@views_endpoints.route("/static/<path:path>")
def send_static(path):
    return send_from_directory("static", path)
