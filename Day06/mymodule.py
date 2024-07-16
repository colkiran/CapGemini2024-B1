
gname = "Sachin Tendulkar"

sports = ['cricket', 'Football', 'Tennis', 'Hockey', 'Swimming']

runs = {'odi': 26500, 'test': 13450, 't20': 2500}

def greet(gnm):
    print(f"Greeting Mr.{gnm}, Welcome to the event........")

class Employee:

    # double underscore init   => dunder init
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        print(f"Name is {self.name}\nSalary is {self.salary}")

# print(__name__)

if __name__ == '__main__':
    greet("Messi")

    emp = Employee("Ruben", 45000)
    emp.get_details()
