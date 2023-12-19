from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import AirplaneSerializer

class AirplaneListCreateView(generics.CreateAPIView):
    serializer_class = AirplaneSerializer

    def create(self, request, *args, **kwargs):
        airplanes_data = request.data

        if len(airplanes_data) > 10:
            return Response({"detail": "Cannot create more than 10 airplanes."}, status=status.HTTP_400_BAD_REQUEST)
        
        if not isinstance(airplanes_data, list):
            return Response({"detail": "Invalid data. Expected a list of dictionaries."}, status=status.HTTP_400_BAD_REQUEST)

        created_airplanes = []

        for airplane_data in airplanes_data:
            serializer = self.get_serializer(data=airplane_data)
            serializer.is_valid(raise_exception=True)

            # Calculate values without saving to the database
            fuel_consumption = serializer.validated_data["id"] * 0.80
            max_flight_minutes = (200 * serializer.validated_data["id"]) / fuel_consumption

            response_data = {
                "id": serializer.validated_data["id"],
                "passengers": serializer.validated_data["passengers"],
                "fuel_consumption_per_minute": fuel_consumption,
                "total_flight_minutes": max_flight_minutes
            }

            created_airplanes.append(response_data)

        return Response(created_airplanes, status=status.HTTP_201_CREATED)
