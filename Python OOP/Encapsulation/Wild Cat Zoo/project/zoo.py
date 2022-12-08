from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget < price:
            return "Not enough budget"
        if self.__animal_capacity == len(self.animals):
            return "Not enough space for animal"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if self.__workers_capacity == len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        sum_salaries = sum(a.salary for a in self.workers)
        if self.__budget < sum_salaries:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= sum_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        sum_money_for_care = sum(a.money_for_care for a in self.animals)
        if self.__budget < sum_money_for_care:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= sum_money_for_care
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        lions = [repr(a) for a in self.animals if isinstance(a, Lion)]
        tigers = [repr(a) for a in self.animals if isinstance(a, Tiger)]
        cheetahs = [repr(a) for a in self.animals if isinstance(a, Cheetah)]
        result += f"----- {len(lions)} Lions:\n"
        for lion in lions:
            result += lion + "\n"
        result += f"----- {len(tigers)} Tigers:\n"
        for tiger in tigers:
            result += tiger + "\n"
        result += f"----- {len(cheetahs)} Cheetahs:\n"
        for cheetah in cheetahs:
            result += cheetah + "\n"
        return result.strip()


    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        keepers = [repr(a) for a in self.workers if isinstance(a, Keeper)]
        caretakers = [repr(a) for a in self.workers if isinstance(a, Caretaker)]
        vets = [repr(a) for a in self.workers if isinstance(a, Vet)]
        result += f"----- {len(keepers)} Keepers:\n"
        for keeper in keepers:
            result += keeper + "\n"
        result += f"----- {len(caretakers)} Caretakers:\n"
        for caretaker in caretakers:
            result += caretaker + "\n"
        result += f"----- {len(vets)} Vets:\n"
        for vet in vets:
            result += vet + "\n"
        return result.strip()
