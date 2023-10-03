# Create your models here.
from django.db import models


class Departement(models.Model):
    departement = models.CharField(max_length=250)
    numero = models.IntegerField()
    prix_m2 = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.departement}{self.numero}"


class Machine(models.Model):
    machine = models.CharField(max_length=250)
    prix = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.machine}{self.prix}"


class Ingredient(models.Model):
    ingredient = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.ingredient}"


class QuantiteIngredient(models.Model):
    quantite = models.IntegerField()
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.ingredient}{self.quantite}"


class Action(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.PROTECT)
    commande = models.CharField(max_length=50)
    duree = models.IntegerField()
    ingredient = models.ManyToManyField(QuantiteIngredient)
    action = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.action}"


class Recette(models.Model):
    recette = models.CharField(max_length=250)
    action = models.ForeignKey(Action, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.recette}"


class Prix(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    departement = models.ForeignKey(Departement, on_delete=models.PROTECT)
    prix = models.IntegerField()

    def __str__(self):
        return f"{self.ingredient}{self.departement}{self.prix}"


class Usine(models.Model):
    nom = models.CharField(max_length=250)
    zone = models.CharField(max_length=50)
    departement = models.ForeignKey(Departement, on_delete=models.PROTECT)
    taille = models.IntegerField()
    machine = models.ManyToManyField(Machine)
    recette = models.ManyToManyField(Recette)
    stocks = models.ManyToManyField(QuantiteIngredient)

    def __str__(self):
        return (
            f"{self.departement}{self.taille}{self.machine}{self.recette}{self.stocks}"
        )

    # Création des objets pour chaque classe
