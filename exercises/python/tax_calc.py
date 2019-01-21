class TaxCalculator:
    def calculate_tax(self,vehicle):
        if vehicle.co2_emissions == 0:
            return 0
        if vehicle.fuel_type == "ALTERNATIVE_FUEL" and vehicle.co2_emissions in range(51,76):
            return 15

