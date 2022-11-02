from rest_framework.viewsets import ViewSet
from spotterapi.models.Profile import Profile
from spotterapi.models.Session import Session
from spotterapi.models.SessionExercise import SessionExercise
from spotterapi.models.Exercise import Exercise
from spotterapi.serializers.session_serializer import SessionSerializer
from rest_framework.response import Response
from rest_framework import status

class SessionView (ViewSet):
    
    def retrieve(self, pk):
        
        print(pk)
        
        session = Session.objects.get(pk = pk)
        
        
        serializer = SessionSerializer(session)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def list(self, request):
        
        profile = Profile.objects.get(pk = request.auth.user.id)
        sessions = Session.objects.filter(profile = profile)
       
        
        serializer = SessionSerializer(sessions, many = True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
        

    
      
        