from rest_framework import serializers
# from .models import DataModel

# Serializer to check the correctness of data entered by the user
class RiskCalculationSerializer(serializers.Serializer):
    age = serializers.IntegerField()
    dependents = serializers.IntegerField()
    income = serializers.IntegerField()
    marital_status = serializers.ChoiceField(choices=["married", "Single"])
    risk_questions = serializers.ListField(child=serializers.IntegerField())
    vehicle = serializers.DictField(child=serializers.IntegerField(),allow_empty=True,required=False)
    house = serializers.DictField(child=serializers.ChoiceField(choices=["owned", "mortgage"]),allow_empty=True,required=False)




