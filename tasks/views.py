from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Task
from .serializers import TaskSerializer
from users.models import TaskUser

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_tasks(request):
    print("logged in user is:",request.user) #request.user = logged in user
    tasks = Task.objects.filter(user=request.user)
    # tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@permission_classes([IsAdminUser])
def get_admin_tasks(request):
    print("USER IS:",request.user)
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

from rest_framework.response import Response
from users.models import TaskUser



# register
@api_view(['POST'])
def register(request):
   user = TaskUser.objects.create_user(
               username=request.data['username'],
               email=request.data['email'],
               password=request.data['password']
           )
   user.is_active = True
#    user.is_staff = True
   user.save()
   return Response("new user born")