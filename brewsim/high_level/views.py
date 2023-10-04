# Create your views here.
from json import dumps

from django.http import HttpResponse
from django.views.generic import DetailView

from .models import Departement, Ingredient, QuantiteIngredient, Usine


class DepartementDetailView(DetailView):
    models = Departement

    def render_to_response(self, context, **response_kwargs):
        return HttpResponse(dumps(self.objects.json()))


class QuantiteDetailView(DetailView):
    models = Ingredient

    def render_to_response(self, context, **response_kwargs):
        return HttpResponse(dumps(self.objects.json()))


class QuantiteIngredientDetailView(DetailView):
    models = QuantiteIngredient

    def render_to_response(self, context, **response_kwargs):
        return HttpResponse(dumps(self.objects.json()))


class UsineDetailView(DetailView):
    models = Usine

    def render_to_response(self, context, **response_kwargs):
        return HttpResponse(dumps(self.objects.json()))
