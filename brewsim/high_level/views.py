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
    model = Departement

    def render_to_response(self, context, **response_kwargs):
        return HttpResponse(dumps(self.object.json()))


class DepartementApiDetailView(DetailView):
    model = Departement

    def render_to_response(self, context, **response_kwargs):
        return HttpResponse(dumps(self.object.json_extended()))


class MachineDetailView(DetailView):
    model = Machine

    def render_to_response(self, context, **response_kwargs):
        return HttpResponse(dumps(self.object.json()))


class MachineApiDetailView(DetailView):
    model = Machine

    def render_to_response(self, context, **response_kwargs):
        return HttpResponse(dumps(self.object.json_extended()))


class ActionDetailView(DetailView):
    model = Action

    def render_to_response(self, context, **response_kwargs):
        return HttpResponse(dumps(self.object.json()))


class ActionApiDetailView(DetailView):
    model = Action

    def render_to_response(self, context, **response_kwargs):
        return HttpResponse(dumps(self.object.json_extended()))


class RecetteDetailView(DetailView):
    model = Recette

    def render_to_response(self, context, **response_kwargs):
        return HttpResponse(dumps(self.object.json()))


class RecetteApiDetailView(DetailView):
    model = Recette

    def render_to_response(self, context, **response_kwargs):
        return HttpResponse(dumps(self.object.json_extended()))


class PrixDetailView(DetailView):
    model = Prix

    def render_to_response(self, context, **response_kwargs):
        return HttpResponse(dumps(self.object.json()))


class PrixApiDetailView(DetailView):
    model = Prix

    def render_to_response(self, context, **response_kwargs):
        return HttpResponse(dumps(self.object.json_extended()))


class IngredientDetailView(DetailView):
    model = Ingredient

    def render_to_response(self, context, **response_kwargs):
        return HttpResponse(dumps(self.object.json()))


class IngredientApiDetailView(DetailView):
    model = Ingredient

    def render_to_response(self, context, **response_kwargs):
        return HttpResponse(dumps(self.object.json_extended()))


class QuantiteIngredientDetailView(DetailView):
    model = QuantiteIngredient

    def render_to_response(self, context, **response_kwargs):
        return HttpResponse(dumps(self.object.json()))


class QuantiteIngredientApiDetailView(DetailView):
    model = QuantiteIngredient

    def render_to_response(self, context, **response_kwargs):
        return HttpResponse(dumps(self.object.json_extended()))


class UsineDetailView(DetailView):
    model = Usine

    def render_to_response(self, context, **response_kwargs):
        return HttpResponse(dumps(self.object.json()))


class UsineApiDetailView(DetailView):
    model = Usine

    def render_to_response(self, context, **response_kwargs):
        return HttpResponse(dumps(self.object.json_extended()))
