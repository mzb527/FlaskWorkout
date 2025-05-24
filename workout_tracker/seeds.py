from app import create_app, db
from app.models import Exercise, Workout

app = create_app()

with app.app_context():
    db.session.query(WorkoutExercises).delete()
    db.session.query(Workout).delete()
    db.session.query(Exercise).delete()

    exercises = [
        Exercise(name="Squat", category="Legs", equipment_needed=True),
        Exercise(name="Push-up", category="Chest", equipment_needed=False),
        Exercise(name="Deadlift", category="Full Body", equipment_needed=True),
    ]

    workouts = [
        Workout(date="2025-05-23", duration_minutes=45, notes="Strength training"),
        Workout(date="2025-05-24", duration_minutes=30, notes="Cardio"),
    ]

    db.session.add_all(exercises + workouts)
    db.session.commit()
    print("Database seeded successfully!")