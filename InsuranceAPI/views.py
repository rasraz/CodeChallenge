from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RiskCalculationSerializer
import json
from datetime import datetime

# View API registration and calculation of user insurance risk
class RiskCalculationView(APIView):
    """
    If the user does not have a house or a vehicle, completely skip sending these two data (even blank).
    """
    # Method for calculating user insurance risk
    def calculation(self,validated_data):
        risk_questions=sum(validated_data.get('risk_questions'))
        income=int(validated_data.get('income'))
        vehicle_data = validated_data.get('vehicle',None)
        if vehicle_data is not None:
            vehicle = vehicle_data.get('year',None)
            if vehicle is not None:
                year=int(vehicle)
                today = int(datetime.now().year)
                if (5<(today-year)):
                    if 'auto' in scores:scores['auto']+=1
        else:vehicle = None
        house_data = validated_data.get('house', None)
        if house_data is not None:house = house_data.get('ownership_status', None)
        else:house = None
        age=int(validated_data.get('age'))
        marital_status=validated_data.get('marital_status')
        scores={
            'auto':risk_questions,
            'life':risk_questions,
            'home':risk_questions,
            'disability':risk_questions,
        }
        if (income==0) or (vehicle is None) or (house is None):
            del scores['disability']
            del scores['home']
            del scores['auto']
        if (60<age):
            if 'disability' in scores:del scores['disability']
            del scores['life']
        if (age<30):
            for key in scores:scores[key] -= 2
        elif (age<40) and (30<age):
            for key in scores:scores[key] -= 1
        if (house=='mortgage'):
            if 'home' in scores:scores['home']+=1
            if 'disability' in scores:scores['disability']+=1
        if (200_000<income):
            for key in scores:scores[key] -= 1
        if (marital_status=='married'):
            if 'life' in scores:scores['life']+=1
            if 'disability' in scores:scores['disability']-=1

        keys=('auto','life','home','disability')
        for key in keys:
            if key not in scores:scores[key]='ineligible'
            else:
                if scores[key]<=0:scores[key]='economic'
                elif scores[key]==1 or scores[key]==2:scores[key]='regular'
                else:scores[key]='responsible'
        return scores
    
    # Post API to receive information sent by the user
    def post(self,request):
        serialized_data=RiskCalculationSerializer(data=request.data)
        print(request)
        if serialized_data.is_valid():
            # serialized_data.save()
            data_calculated=self.calculation(validated_data=serialized_data.data)
            return Response(data_calculated, status=status.HTTP_200_OK)
        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)