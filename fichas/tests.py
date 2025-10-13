# Create your tests here.
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class FichaAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_and_export_ficha(self):
        data = {
            "nome": "Ficha Padrão",
            "nivel": 1,
            "atributos": {"for": 10, "des": 10, "con": 10, "int": 10, "sab": 10, "car": 10},
            "schema_version": 1
        }
        res = self.client.post("/api/fichas/", data, format="json")
        assert res.status_code == status.HTTP_201_CREATED
        # export
        fid = res.data["id"]
        res2 = self.client.get(f"/api/fichas/{fid}/export/")
        assert res2.status_code == status.HTTP_200_OK
        assert res2.data["nome"] == "Ficha Padrão"
