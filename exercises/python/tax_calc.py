import datetime

class TaxCalculator:
    def calculate_tax(self, vehicle):
        if vehicle.date_of_first_registration == datetime.now.year:
            self.calculate_tax_first_year(vehicle)
        else:
            self.calculate_tax_after_first_year(vehicle)


    def calculate_tax_first_year(self,vehicle):
        if vehicle.co2_emissions == 0:
            return 0

        if vehicle.fuel_type == "ALTERNATIVE_FUEL" and vehicle.co2_emissions in range(51,76):
            return 15

        if vehicle.fuel_type == "DIESEL":
          if vehicle.co2_emissions in range(1, 51):
              return 25
          elif vehicle.co2_emissions in range(51, 76):
              return 105
          elif vehicle.co2_emissions in range(76, 91):
              return 125
          elif vehicle.co2_emissions in range(91, 101):
              return 145
          elif vehicle.co2_emissions in range(101, 111):
              return 165
          elif vehicle.co2_emissions in range(111, 131):
              return 205
          elif vehicle.co2_emissions in range(131, 151):
              return 515
          elif vehicle.co2_emissions in range(151, 171):
              return 830
          elif vehicle.co2_emissions in range(171, 191):
              return 820
          elif vehicle.co2_emissions in range(191, 226):
              return 1760

    def calculate_tax_after_first_year(self, vehicle):

        if vehicle.fuel_type == "PETROL":
            return 140
        elif vehicle.fuel_type == "ELECTRIC":
            return 0
        elif vehicle.fuel_type == "ALTERNATIVE_FUEL":
            return 130


   
