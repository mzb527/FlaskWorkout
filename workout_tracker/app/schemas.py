from marshmallow import Schema, fields, validates, ValidationError
from app import ma

class ExerciseSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    equipment_needed = fields.Bool()

    @validates("name")
    def validate_name(self, value):
        if not value or len(value) < 3:
            raise ValidationError("Exercise name must be at least 3 characters.")

class WorkoutSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    date = fields.Date(required=True)
    duration_minutes = fields.Int(required=True)
    notes = fields.Str()

    @validates("duration_minutes")
    def validate_duration(self, value):
        if value <= 0:
            raise ValidationError("Duration must be a positive integer.")

class WorkoutExercisesSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    workout_id = fields.Int(required=True)
    exercise_id = fields.Int(required=True)
    reps = fields.Int(required=True)
    sets = fields.Int(required=True)
    duration_seconds = fields.Int(required=True)

    @validates("reps")
    def validate_reps(self, value):
        if value <= 0:
            raise ValidationError("Reps must be a positive integer.")