class Contract(object):
    def __init__(self, vehicle, customer):
		self.vehicle = vehicle
		self.customer = customer


class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        Contract.__init__(self, vehicle, customer)
		self.monthly_payments = monthly_payments

	def total_value(self):
		discount = 0
		if isinstance(self.customer, Employee):
			discount = 0.1

		interest = 1
		if isinstance(self.vehicle, Car):
			interest = 1.07
		elif isinstance(self.vehicle, Motorcycle):
			interest = 1.03
		elif isinstance(self.vehicle, Truck):
			interest = 1.11

		return (self.vehicle.sale_price() + (interest * self.monthly_payments * self.vehicle.sale_price() / 100)) * (1 - discount)

	def monthly_value(self):
		return self.total_value() / self.monthly_payments

class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        Contract.__init__(self, vehicle, customer)
		self.length_in_months = length_in_months

	def total_value(self):
		discount = 0
		if isinstance(self.customer, Employee):
			discount = 0.1

		interest = 1
		if isinstance(self.vehicle, Car):
			interest = 1.2
		elif isinstance(self.vehicle, Motorcycle):
			interest = 1.
		elif isinstance(self.vehicle, Truck):
			interest = 1.7

		return (self.vehicle.sale_price() + (self.vehicle.sale_price() * interest / self.length_in_months)) * (1 - discount)

	def monthly_value(self):
		return self.total_value() / self.length_in_months
