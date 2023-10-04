# Create your views here.
from json import dumps

from django.http import HttpResponse
from django.views.generic import DetailView

from .models import (
    Action,
    Departement,
    Ingredient,
    Machine,
    Prix,
    QuantiteIngredient,
    Recette,
    Usine,
)


class DepartementDetailView(DetailView):
    models = Departement

    def render_to_response(self, context, **response_kwargs):
        return HttpResponse(dumps(self.objects.json()))


class MachineDetailView(DetailView):
    models = Machine

    def render_to_response(self, context, **response_kwargs):
        return HttpResponse(dumps(self.objects.json()))


class ActionDetailView(DetailView):
    models = Action

    def render_to_response(self, context, **response_kwargs):
        return HttpResponse(dumps(self.objects.json()))


class RecetteDetailView(DetailView):
    models = Recette

    def render_to_response(self, context, **response_kwargs):
        return HttpResponse(dumps(self.objects.json()))


class PrixDetailView(DetailView):
    models = Prix

    def render_to_response(self, context, **response_kwargs):
        return HttpResponse(dumps(self.objects.json()))


class IngredientDetailView(DetailView):
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
