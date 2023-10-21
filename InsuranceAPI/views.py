from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import RiskCalculationSerializer

# View API registration and calculation of user insurance risk
class RiskCalculationView(APIView):
    # Method for calculating user insurance risk
    def calculation(self,data):
        scores={
            'auto':0,
            'life':0,
            'home':0,
            'disability':0,
        }
        if (int(data.income==0)) and (vehicle is null) and (house is null):
            del scores['disability']
            del scores['home']
            del scores['auto']
        if (60<int(data.age)):
            if 'disability' in scores:del scores['disability']
            del scores['life']
        if (int(data.age)<30):
            for key in scores:scores[key] -= 2
        elif (int(data.age)<40) and (30<int(data.age)):
            for key in scores:scores[key] -= 1
        if (data.house=='mortgage'):
            if 'home' in scores:scores['home']+=1
            if 'disability' in scores:scores['disability']+=1
        if (200_000<int(data.income)):
            for key in scores:scores[key] -= 1
        if (data.marital_status=='married'):
            if 'life' in scores:scores['life']+=1
            if 'disability' in scores:scores['disability']-=1
        year=int(data.vehicle.year)
        today = int(datetime.now().year)
        if (5<(today-year)):
            if 'auto' in scores:scores['auto']+=1
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
        if serialized_data.is_valid():
            serialized_data.save()
            data_calculated=self.calculation(serialized_data.data)
            return Response(data_calculated, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)