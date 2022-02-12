from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response

from applications.store.models import Store, Visit
from applications.store.serializers import StoreSerializer, VisitSerializer


class StoresListView(GenericAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    def post(self, request, *args, **kwargs):
        """Return a list of Store objects by worker phone"""
        phone_number = request.data.get("phone_number")
        if not phone_number:
            return Response({"error": "No phone number provided."}, status=status.HTTP_400_BAD_REQUEST)
        queryset = self.get_queryset().filter(worker__phone=phone_number)
        serializer = self.get_serializer(queryset, many=True, read_only=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetVisitView(GenericAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer

    def post(self, request, *args, **kwargs):
        """Validate request data and return created visit info"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
