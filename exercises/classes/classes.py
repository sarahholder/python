#Blueprint / machine / recipe for making instance objects
class Employee:
  
  # We don't execute this function
  # This is called a dunder method (double underscore)
  # Self is a keyword that refers to the instance
    def __init__(self, name, title, start_date):
      self.name = name
      self.title = title
      self.start_date = start_date

    def payEmployee(self):
      print(f"Yay! now {self.name} I can pay my rent")

    def __str__(self):
      return f"This is an employee named {self.name, self.title, self.start_date }"

#An instance is a combo of predictable/repeated properties with unique values
fred = Employee("Fred", "supervisor", "01/02/2020")
# fred's value is an object
fred.title = "supervisor"
fred.name = "Fred"
print(fred)

linda = Employee("Linda", "boss", "10/23/1999")
print(linda.name, linda.title, linda.start_date)

linda.payEmployee()

class Company: 

    def __init__(self, name, date_founded, product):
      self.name = name
      self.date_founded  = date_founded
      self.product = product
      self.employees = [] 

    def addEmployees(self, employees):
      self.employees.extend(employees)

    def __str__(self):
      return f'{self.name} makes {self.product}!'

widget_co = Company("Widget Co", "07/16/2020", "the finest widgets")
print(widget_co)

widget_co.addEmployees([fred])

print(widget_co.employees)






