from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models.fichas import Ficha
from ..serializers.ficha_serializer import FichaSerializer


class FichaViewSet(viewsets.ModelViewSet):
    queryset = Ficha.objects.all()
    serializer_class = FichaSerializer

    @action(detail=True, methods=["get"])
    def export(self, request, pk=None):
        ficha = self.get_object()
        serializer = self.get_serializer(ficha)
        data = serializer.data
        # ensure schema_version included
        return Response(data)

    @action(detail=False, methods=["post"])
    def import_json(self, request):
        # import a ficha from a posted JSON body
        obj = request.data
        # validate schema using serializer helper
        FichaSerializer.validate_import_json(obj)
        # If it passes, create Ficha
        serializer = self.get_serializer(data=obj)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
