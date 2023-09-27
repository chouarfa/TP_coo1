# Create your models here.
from django.db import models


class Departement(models.Model):
    departement_name = models.CharField(max_length=250)
    numero = models.IntegerField()
    prix_m2 = models.CharField(max_length=10)

    def __str__(self):
        return self.departement_name


class Machine(models.Model):
    nom_machine = models.CharField(max_length=250)
    prix = models.CharField(max_length=200)

    def __str__(self):
        return self.nom_machine


class Ingredient(models.Model):
    nom_ingredient = models.CharField(max_length=250)

    def __str__(self):
        return self.nom_ingredient


class QuantiteIngredient(models.Model):
    quantite = models.IntegerField()
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)

    def __str__(self):
        return self.quantite


class Action(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.PROTECT)
    commande = models.CharField(max_length=50)
    duree = models.IntegerField()
    ingredient = models.ManyToManyField(QuantiteIngredient)
    action = models.CharField(max_length=250)

    def __str__(self):
        return self.action


class Recette(models.Model):
    nom_recette = models.CharField(max_length=250)
    action = models.ForeignKey(Action, on_delete=models.PROTECT)

    def __str__(self):
        return self.nom_recette


class Prix(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    departement = models.ForeignKey(Departement, on_delete=models.PROTECT)
    prix = models.IntegerField()

    def __str__(self):
        return self.ingredient


class Usine(models.Model):
    nom = models.CharField(max_length=250)
    zone = models.CharField(max_length=50)
    departement = models.ForeignKey(Departement, on_delete=models.PROTECT)
    taille = models.IntegerField()
    machine = models.ManyToManyField(Machine)
    recette = models.ManyToManyField(Recette)
    stocks = models.ManyToManyField(QuantiteIngredient)

    def __str__(self):
        return self.nom
