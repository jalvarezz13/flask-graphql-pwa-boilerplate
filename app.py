from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)

bootstrap = Bootstrap5(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


from views import views_endpoints

app.register_blueprint(views_endpoints)

if __name__ == "__main__":
    app.run()
