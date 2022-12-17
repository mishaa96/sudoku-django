import logging
from os import stat
from django.shortcuts import render
from rest_framework import viewsets, views, status
from api.functions import solve_puzzle
from api.models import Puzzle
from rest_framework.response import Response
from api.serializers import PuzzleSerializer

# Create your views here.

class PuzzleViewSet(viewsets.ModelViewSet):
    serializer_class = PuzzleSerializer

    def get_queryset(self):
        user = self.request.user
        return Puzzle.objects.filter(user=user).filter(completed=False).order_by('-created_on')[:1]


class SolverView(views.APIView):
    def post(self, request):
        data = request.data
        # logging.info(data)
        puzzle = data.get("puzzle")
        logging.info(puzzle)
        valid, puzzle = solve_puzzle(puzzle=puzzle, validate=True)
        return Response({"status": valid}, status=status.HTTP_200_OK)



