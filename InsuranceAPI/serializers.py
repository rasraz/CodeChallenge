from rest_framework import serializers
from .models import DataModel

# Serializer to check the correctness of data entered by the user
class RiskCalculationSerializer(serializers.ModelSerializer):
    class Meta:
        model=DataModel
        fields="__all__"
    def validate_age(self,value):
        if value<0 or not value.is_integer():
            serializers.ValidationError('The age value must be an integer less than or equal to zero')
        return value
    def validate_dependents(self,value):
        if value<0 or not value.is_integer():
            serializers.ValidationError('The number of dependencies must be an integer less than or equal to zero')
        return value
    def validate_income(self,value):
        if value<0 or not value.is_integer():
            serializers.ValidationError('The amount of income must be an integer less than or equal to zero')
        return value
    def validate_marital_status(self,value):
        if value!='married' and value!='Single':
            serializers.ValidationError('Please choose from the specified values')
        return value
    def validate_risk_questions(self,value):
        if not isinstance(value, (list, tuple)):
            serializers.ValidationError('Please send the answers to the risk questions as an array (list or tuple).')
        if not all(x==0 or x==1 for x in value):
            serializers.ValidationError('Please enter all answers to risk questions in binary form (0 and 1).')
        return sum(value)
    def validate_house(self,value):
        if value is null:return value
        if value['ownership_status']!='owned' and value['ownership_status']!='mortgage':
            serializers.ValidationError('Please choose from the specified values')
        return value
    def validate_vehicle(self,value):
        if value is null:return value
        year=value['year']
        if year<0 or not year.isnull():
            serializers.ValidationError('Please enter the correct vehicle year format')
        try:
            date_obj = datetime.strptime(str(year), '%Y')
            return date_obj
        except ValueError:serializers.ValidationError('Please enter the correct vehicle year format')