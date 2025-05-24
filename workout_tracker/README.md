Workout Tracker API
Project Overview
The Workout Tracker API is a Flask-based backend service that allows users to create, delete, and view workouts and exercises. It also enables associating exercises with workouts for tracking reps, sets, and duration.
Tech Stack
- Flask - Web framework
- Flask-SQLAlchemy - ORM for database management
- Flask-Migrate - Handles database migrations
- Flask-Marshmallow - Serialization and validation
- SQLite - Lightweight database storage
Installation and Setup
Clone Repository
git clone <https://github.com/mzb527/FlaskWorkout>
cd workout_tracker
Set Up Virtual Environment
python -m venv venv
venv\Scripts\activate


Install Dependencies
pip install -r requirements.txt


Initialize Database
flask db init
flask db migrate -m "Initial migration"
flask db upgrade


Seed Database
python seeds.py


Run the Application
python run.py


The application runs at http://127.0.0.1:5555.
API Endpoints
Workout Endpoints
List All Workouts
GET /workouts


Response: List of all workouts.
Create a Workout
POST /workouts


Request JSON:
{
  "date": "2025-05-23",
  "duration_minutes": 45,
  "notes": "Strength training"
}


Response: Created workout.
Delete a Workout
DELETE /workouts/<id>


Response: Deletes the workout.
Exercise Endpoints
List All Exercises
GET /exercises


Response: List of all exercises.
Create an Exercise
POST /exercises


Request JSON:
{
  "name": "Deadlift",
  "category": "Full Body",
  "equipment_needed": true
}


Response: Created exercise.
Delete an Exercise
DELETE /exercises/<id>


Response: Deletes the exercise.
Workout-Exercise Relationship
Add Exercise to Workout
POST /workouts/<workout_id>/exercises/<exercise_id>/workout_exercises


Request JSON:
{
  "reps": 10,
  "sets": 3,
  "duration_seconds": 60
}


Response: Adds exercise to workout.
Testing the API
Use Postman or curl to interact with the API. Example:
curl -X POST http://127.0.0.1:5555/exercises -H "Content-Type: application/json" -d '{"name": "Squat", "category": "Legs", "equipment_needed": true}'






