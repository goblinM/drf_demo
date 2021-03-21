from django.shortcuts import render
from rest_framework import authentication, permissions
from rest_framework.decorators import api_view, throttle_classes, authentication_classes, permission_classes, \
    parser_classes, renderer_classes
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView


class RequestView(APIView):
    def get(self, request):
        data = request.query_params
        print(data)
        return Response('')

    def post(self, request):
        data = request.data
        print(data)
        return Response('')


class UserView(APIView):
    authentication_classes = ()
    permission_classes = ()
    # throttle_classes = ()
    # renderer_classes = ()
    # parser_classes = ()
    # content_negotiation_class = ()
    # metadata_class = ()

    def dispatch(self, request, *args, **kwargs):
        """
        请求到来之后，都要请求dispatch方法，dispath方法根据不同的请求方式出发get/post/put等方法
        注意：APIView中，dispath方法有好多好多功能
        """
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return Response({"message": 'hello world'})

    def post(self, request, *args, **kwargs):
        return Response({'message': 'hello John'})


@api_view(["GET", "POST"])
@authentication_classes([])
@permission_classes([])
def user_view(request):
    if request.method == 'POST':
        return Response({'message': 'hello John'})
    return Response({"message": 'hello world'})
