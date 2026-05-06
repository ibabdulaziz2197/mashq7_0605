# 10
class Movie:
    def __init__(self, title, duration, rating):
        self.title = title
        self._duration = duration
        self.__rating = rating

    def play(self):
        print(f"Playing {self.title}")

    def rate(self, x):
        self.__rating = x

    def info(self):
        print(f"Title: {self.title}")
        print(f"Duration: {self._duration}")
        print(f"Rating:{self.__rating}")



m = Movie("Avengers", 120, 8)

m.play()
m.rate(9)
m.info()

# 11
class Animal:
    def __init__(self, name, _age):
        self.name = name
        self._age = _age

    def eat(self):
        print("Eating...")

    def sleep(self):
        print("Sleeping...")


class Dog(Animal):
    def __init__(self, name, _age, _breed):
        super().__init__(name, _age)
        self._breed = _breed

    def bark(self):
        print("Woof")

    def info(self):
        print(f"Name: {self.name}, Age: {self._age}, Breed: {self._breed}")


# obyekt yaratish
dog = Dog("Rex", 3, "Husky")


dog.eat()
dog.bark()

# 12
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, _grade):
        super().__init__(name, age)
        self._grade = _grade

    def study(self):
        print("Studying...")

    def take_exam(self):
        print(f"Grade:{self._grade}")


# obyekt yaratish
student = Student("Ali", 18, 85)

# natija
student.study()
student.take_exam()

# 13
class Vehicle:
    def __init__(self, speed):
        self._speed = speed


class Car(Vehicle):
    def __init__(self, speed, fuel):
        super().__init__(speed)
        self._fuel = fuel

    def drive(self):
        self._speed += 20

    def refuel(self, x):
        self._fuel += x


car = Car(100, 40)

car.drive()
car.refuel(20)

print("Speed:", car._speed)
print("Fuel:", car._fuel)


# 14
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    def work(self):
        print(f"{self.name} ishlayapti.")

    def increase_salary(self, x):
        self._salary += x
        print(f"Yangi salary: {self._salary}")


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self._team_size = team_size

    def manage(self):
        print(f"{self.name} {self._team_size} kishilik jamoani boshqarmoqda.")


    def work(self):
        print(f"{self.name} menejer sifatida strategik ish qilmoqda.")
emp = Employee("Ali", 1000)
emp.work()
emp.increase_salary(200)

mgr = Manager("Vali", 2000, 5)
mgr.work()
mgr.manage()
mgr.increase_salary(500)


# 15
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)



rect = Rectangle(5, 4)

print("Area:", rect.area())
print("Perimeter:", rect.perimeter())
