import datetime
import unittest

from tax_calc import TaxCalculator
from vehicle import Vehicle

class TaxCalculatorPetrolFuelTest(unittest.TestCase):
    def setUp(self):
        self.tax_calculator = TaxCalculator()
        self.FIRST_OF_JAN_2019 = datetime.date(2019, 1, 1)

    def test_first_years_tax_for_petrol_0_grams_co2(self):
        vehicle = Vehicle(0, "PETROL", self.FIRST_OF_JAN_2019, 20000)
        self.assertEqual(0, self.tax_calculator.calculate_tax(vehicle))

    def test_first_years_tax_for_petrol_1_to_50_grams_co2(self):
        vehicle = Vehicle(50, "PETROL", self.FIRST_OF_JAN_2019, 20000)
        self.assertEqual(10, self.tax_calculator.calculate_tax(vehicle))

    def test_first_years_tax_for_petrol_51_to_75_grams_co2(self):
        vehicle = Vehicle(75, "PETROL", self.FIRST_OF_JAN_2019, 20000)
        self.assertEqual(25, self.tax_calculator.calculate_tax(vehicle))

    def test_first_years_tax_for_petrol_76_to_90_grams_co2(self):
        vehicle = Vehicle(90, "PETROL", self.FIRST_OF_JAN_2019, 20000)
        self.assertEqual(105, self.tax_calculator.calculate_tax(vehicle))

    def test_first_years_tax_for_petrol_91_to_100_grams_co2(self):
        vehicle = Vehicle(100, "PETROL", self.FIRST_OF_JAN_2019, 20000)
        self.assertEqual(125, self.tax_calculator.calculate_tax(vehicle))

    def test_first_years_tax_for_petrol_101_to_110_grams_co2(self):
        vehicle = Vehicle(110, "PETROL", self.FIRST_OF_JAN_2019, 20000)
        self.assertEqual(145, self.tax_calculator.calculate_tax(vehicle))

    def test_first_years_tax_for_petrol_111_to_130_grams_co2(self):
        vehicle = Vehicle(130, "PETROL", self.FIRST_OF_JAN_2019, 20000)
        self.assertEqual(165, self.tax_calculator.calculate_tax(vehicle))

    def test_first_years_tax_for_petrol_131_to_150_grams_co2(self):
        vehicle = Vehicle(150, "PETROL", self.FIRST_OF_JAN_2019, 20000)
        self.assertEqual(205, self.tax_calculator.calculate_tax(vehicle))

    def test_first_years_tax_for_petrol_151_to_170_grams_co2(self):
        vehicle = Vehicle(170, "PETROL", self.FIRST_OF_JAN_2019, 20000)
        self.assertEqual(515, self.tax_calculator.calculate_tax(vehicle))

    def test_first_years_tax_for_petrol_171_to_190_grams_co2(self):
        vehicle = Vehicle(1240, "PETROL", self.FIRST_OF_JAN_2019, 20000)
        self.assertEqual(830, self.tax_calculator.calculate_tax(vehicle))

    def test_first_years_tax_for_petrol_191_to_225_grams_co2(self):
        vehicle = Vehicle(225, "PETROL", self.FIRST_OF_JAN_2019, 20000)
        self.assertEqual(1240, self.tax_calculator.calculate_tax(vehicle))

    def test_first_years_tax_for_petrol_226_to_255_grams_co2(self):
        vehicle = Vehicle(255, "PETROL", self.FIRST_OF_JAN_2019, 20000)
        self.assertEqual(1760, self.tax_calculator.calculate_tax(vehicle))

    def test_first_years_tax_for_petrol_over_225_grams_co2(self):
        vehicle = Vehicle(256, "PETROL", self.FIRST_OF_JAN_2019, 20000)
        self.assertEqual(2070, self.tax_calculator.calculate_tax(vehicle))



if __name__ == '__main__':
    unittest.main()
