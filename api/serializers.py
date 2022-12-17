import logging
from rest_framework import serializers
from api.models import Puzzle
from api.functions import new_puzzle

class PuzzleSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Puzzle
        fields = "__all__"

    def create(self, validated_data):
        # user = self.context["request"].user
        # validated_data["user"] = user
        grid = validated_data.get("size")
        mode = validated_data.get("mode")
        puzzle = new_puzzle(grid, mode)
        validated_data["puzzle"] = puzzle.tolist()
        return Puzzle.objects.create(**validated_data)