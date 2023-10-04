# Create your models here.
from django.db import models


class Departement(models.Model):
    departement = models.CharField(max_length=250)
    numero = models.IntegerField()
    prix_m2 = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.departement}{self.numero}"

    def json(self):
        return {
            "numero": self.numero,
            "prix_m2": float(self.prix_m2),
        }


class Machine(models.Model):
    machine = models.CharField(max_length=250)
    prix = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.machine}{self.prix}"

    def costs(self):
        return int(self.prix)

    def json(self):
        return {
            "machine": self.machine,
            "prix": float(self.prix_m2),
        }


class Ingredient(models.Model):
    ingredient = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.ingredient}"

    def json(self):
        return {"ingredient": self.ingredient}


class QuantiteIngredient(models.Model):
    quantite = models.IntegerField()
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.ingredient}{self.quantite}"

    def costs(self, departement):
        print(f"calcul du cout pour {self.quantite} {self.ingredient} {departement}")
        return (
            self.ingredient.prix_set.get(departement__numero=departement).prix
            * self.quantite
        )

    def json(self):
        return {
            "ingredient": self.ingredient.id,
            "quantite": self.quantite,
        }

    def json_extended(self):
        return {
            "ingredient": self.ingredient.json(),
            "quantite": self.quantite,
        }


class Action(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.PROTECT)
    commande = models.CharField(max_length=50)
    duree = models.IntegerField()
    ingredient = models.ManyToManyField(QuantiteIngredient)
    action = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.action}"

    def json(self):
        return {
            "machine": self.recette.id,
            "commande": self.commande,
            "action": self.action.id,
        }

    def json_extended(self):
        return {
            "machine": self.recette.json(),
            "commande": self.commande,
            "action": self.action.json(),
        }


class Recette(models.Model):
    recette = models.CharField(max_length=250)
    action = models.ForeignKey(Action, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.recette}{self.action}"

    def json(self):
        return {
            "recette": self.recette,
            "action": self.action.id,
        }

    def json_extended(self):
        return {
            "recette": self.recette,
            "action": self.action.json(),
        }


class Prix(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    departement = models.ForeignKey(Departement, on_delete=models.PROTECT)
    prix = models.IntegerField()

    def __str__(self):
        return f"{self.ingredient}{self.departement}{self.prix}"

    def json(self):
        return {
            "ingredient": self.ingredient.id,
            "departement": self.departement.id,
            "prix": self.prix,
        }

    def json_extended(self):
        return {
            "ingredient": self.ingredient.json(),
            "departement": self.departement.json(),
            "prix": self.prix,
        }


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

    def costs(self):
        total = 0
        for m in self.machine.all():
            total += m.costs()
        stock_total = 0
        for m in self.stocks.all():
            stock_total += m.costs(self.departement.numero)

        return self.taille * self.departement.prix_m2 + total + stock_total

    def json(self):
        return {
            "departement": self.departement.id,
            "taille": self.taille,
            "machine": [m.id for m in self.machine.all()],
        }

    def json_extended(self):
        return {
            "departement": self.departement.json(),
            "taille": self.taille,
            "machine": [m.json() for m in self.machine.all()],
        }
