from rest_framework import viewsets
from . models import Post
from . serializers import PostSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=['GET', 'POST'])
    def upvote(self, request, pk=None):
        # breakpoint()
        post = Post.objects.filter(pk=pk).first()
        post.up_votes += 1
        post.save()
        return Response({"status": "post voted up"})

    @action(detail=True, methods=["GET", "POST"])
    def downvote(self, request, pk=None):
        # breakpoint()
        post = Post.objects.filter(pk=pk).first()
        post.down_votes += 1
        post.save()
        return Response({"status": "post voted down"})

