# Create your tests here.

from django.test import TestCase

from .models import Departement, Ingredient, Machine, Prix, QuantiteIngredient, Usine


class MachineModelTests(TestCase):
    def test_usine_creation(self):
        self.assertEqual(Machine.objects.count(), 0)
        Machine.objects.create(machine="four", prix=1_000)
        self.assertEqual(Machine.objects.count(), 1)


class CostModelsTests(TestCase):
    def test_usine_cost(self):
        departement = Departement.objects.create(numero=31, prix_m2=2000)
        usine = Usine.objects.create(taille=50, departement=departement)
        houblon = Ingredient.objects.create(ingredient="houblon")
        orge = Ingredient.objects.create(ingredient="orge")

        stock_houblon = QuantiteIngredient.objects.create(
            ingredient=houblon, quantite=50
        )
        stock_orge = QuantiteIngredient.objects.create(ingredient=orge, quantite=100)

        machine1 = Machine.objects.create(machine="Machine1", prix=1000)
        machine2 = Machine.objects.create(machine="Machine2", prix=2000)

        usine.machine.add(machine1)
        usine.machine.add(machine2)
        usine.stocks.add(stock_houblon)
        usine.stocks.add(stock_orge)

        self.assertEqual(Usine.objects.count(), 1)

        Prix.objects.create(ingredient=houblon, departement=departement, prix=20)
        Prix.objects.create(ingredient=orge, departement=departement, prix=10)

        expected_cost = 105000
        self.assertEqual(usine.costs(), expected_cost)
