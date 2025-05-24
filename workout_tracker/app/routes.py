from flask import Blueprint, request, jsonify
from app import db
from app.models import Exercise, Workout, WorkoutExercises
from app.schemas import ExerciseSchema, WorkoutSchema, WorkoutExercisesSchema

api_bp = Blueprint("api", __name__)

exercise_schema = ExerciseSchema()
workout_schema = WorkoutSchema()
workout_exercise_schema = WorkoutExercisesSchema()

@api_bp.route("/exercises", methods=["POST"])
def create_exercise():
    data = request.json
    errors = exercise_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    
    new_exercise = Exercise(**data)
    db.session.add(new_exercise)
    db.session.commit()
    return jsonify(exercise_schema.dump(new_exercise)), 201

@api_bp.route("/workouts", methods=["POST"])
def create_workout():
    data = request.json
    errors = workout_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    
    new_workout = Workout(**data)
    db.session.add(new_workout)
    db.session.commit()
    return jsonify(workout_schema.dump(new_workout)), 201

@api_bp.route("/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises", methods=["POST"])
def add_exercise_to_workout(workout_id, exercise_id):
    data = request.json
    errors = workout_exercise_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    
    new_entry = WorkoutExercises(workout_id=workout_id, exercise_id=exercise_id, **data)
    db.session.add(new_entry)
    db.session.commit()
    return jsonify(workout_exercise_schema.dump(new_entry)), 201

@api_bp.route("/workouts", methods=["GET"])
def get_workouts():
    workouts = Workout.query.all()
    return jsonify(workout_schema.dump(workouts, many=True)), 200

@api_bp.route("/exercises", methods=["GET"])
def get_exercises():
    exercises = Exercise.query.all()
    return jsonify(exercise_schema.dump(exercises, many=True)), 200