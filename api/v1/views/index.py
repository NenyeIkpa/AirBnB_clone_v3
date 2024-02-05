"""
    create routes(end points)
"""
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status')
def display_status():
    """ displays status """
    return jsonify(
            {
                "status": "ok"
                }
            )


@app_views.route('/stats')
def get_count():
    """ displays total number of objects in
    a class or total of all classes """
    classes = {
        "Amenity": "amenities",
        "City": "cities",
        "Place": "places",
        "Review": "reviews",
        "State": "states",
        "User": "users"
    }
    stats = {}
    for cls, endpoint in classes.items():
        stats[endpoint] = storage.count(cls)
    return jsonify(stats)


@app_views.errorhandler(404)
def not_found(error):
    """ handles 404 """
    response = jsonify({"error": "Not found"})
    response.status_code = 404
    abort(response)
