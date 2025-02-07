from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer

# Create your views here.

#Get Method
#Tease
@api_view(["GET"])
def index(request):
    return Response({"message": "Hello, World!"})


# Get all post Endpoint 
@api_view(["GET"])
def getpost(request):
    
    get_posts = Post.objects.all()
    serializer = PostSerializer(get_posts, many=True)
    return Response(serializer.data)



# Get single post Endpoint
@api_view(['GET'])
def singlepost(request):
    post_id = request.query_params.get('post_id')
    try:
        post = Post.objects.get(id=post_id)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    except Post.DoesNotExist:
        return Response({"Error": "The post does not exist"}, status=404)
    
    
    
#Post Method Endpoint
@api_view(["GET","POST"])
def createpost(request):
    data = request.data
    serializer = PostSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Post created successfully"}, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  
  
#  Delete   Method Endpoint 
@api_view(['DELETE'])
def deletepost(request):
    post_id = request.query_params.get('post_id')
    try:
        post = Post.objects.get(id=post_id)
        post.delete()
        return Response({"Success": "The post was successfully deleted"}, status=status.HTTP_200_OK)
    except Post.DoesNotExist:
        return Response({"Error": "The post does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    
# Update Method Endpoint
@api_view(['PUT'])
def updatepost(request):
    # Retrieve post_id properly
    post_id = request.query_params.get('post_id')  # If coming from URL query params
    if not post_id:
        return Response({"Error": "post_id is required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return Response({"Error": "The post does not exist"}, status=status.HTTP_404_NOT_FOUND)

    # Deserialize and update the post
    serializer = PostSerializer(post, data=request.data, partial=True)
    if serializer.is_valid():
        post = serializer.save()
        return Response(
            {"Success": "The post was successfully updated", "Updated Post": PostSerializer(post).data},
            status=status.HTTP_200_OK
        )
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
