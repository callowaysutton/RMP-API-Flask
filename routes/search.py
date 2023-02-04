import ratemyprofessor
from flask import Blueprint, request, jsonify

cache = {}

# Makes the blueprint for the /graph route 
# Example query may be /graph?q=QUERY which returns the graph of nodes which correspond to the query
search_bp = Blueprint('search', __name__)
@search_bp.route('/search', methods=['POST'])
def search():
    request_body = request.get_json()
    if "name" not in request_body:
        return jsonify({"msg": "Please include a name in the request body!"})
    if "school" not in request_body:
        return jsonify({"msg": "Please include the school in the request body!"})
    
    professor_id = request_body["school"] + request_body["name"]
    if professor_id not in cache:
        professor = ratemyprofessor.get_professor_by_school_and_name(ratemyprofessor.get_school_by_name(request_body["school"]), request_body["name"])
        response = jsonify(
            {
            "name": professor.name,
            "department": professor.department,
            "school": professor.school.name,
            "rating": professor.rating,
            "difficulty": professor.difficulty,
            "num_ratings": professor.num_ratings
            })
        cache[professor_id] = response
        return response
    return cache[professor_id]