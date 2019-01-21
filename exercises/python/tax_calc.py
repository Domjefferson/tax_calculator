class TaxCalculator:
    def calculate_tax(self,vehicle):
        if vehicle.co2_emissions == 0:
            return 0