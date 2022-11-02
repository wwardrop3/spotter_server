
from rest_framework.serializers import Serializer
from models.SessionExercise import SessionExercise
from models.Session import Session

class SessionExerciseSerializer(Serializer):
    
    session = Session()
    
    class Meta:
        model = SessionExercise
        fields = ("id", "reps", "weight", "exercise", "session", "sets")