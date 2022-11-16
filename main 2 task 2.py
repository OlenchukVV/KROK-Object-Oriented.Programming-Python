class BaseProject:
    def __init__(self, deadline):
        self.deadline = datetime.strptime(deadline, "%d.%m.%Y").date()

        # Project id generation
        while True:
            id = randint(10000, 99999)

            try:
                with open(f"{id}.json") as project_file:
                    continue
            except:
                self.id = id
                break

        # Default price
        self.price = 1000


    # Price depending on the type of project
    def check_type(self):
        if self.__class__.__name__ == "TenDaysProject":
            self.price *= 1.6

        if self.__class__.__name__ == "InvestorsProject":
            self.price *= 0.8
        return self.price


    # Generate JSON with project information
    def write_json(self):
        project_info = {
            "project type": self.__class__.__name__,
            "deadline": str(self.deadline),
            "price": self.check_type()
        }
        with open(f"{self.id}.json", "w") as project_json:
            dump(project_info, project_json)
            return "Project added"


    # Find a project by ID and find out the current price
    def find_project(self, id):
        try:
            with open(f"{id}.json") as project_json:
                read_file = load(project_json)
                print(f"Project type: {read_file['project type']}; "
            f"current price: "
            f"{self.check_terms(read_file['deadline'], read_file['price'])}")
        except:
            print("Project not found")


    # Price depending on overdue weeks
    @staticmethod
    def check_terms(deadline, price):
        # Days passed from the deadline to the release of the project
        days_difference = (date.today() -
                           datetime.strptime(deadline,
                                             "%Y-%m-%d").date()).days

        # Overdue weeks
        weeks = days_difference // 7

        if weeks >= 20:
            return 0

        if weeks > 0:
            discount = 5
            discount *= weeks
            price *= 1 - discount / 100
        return price


# Project types

class StandartProject(BaseProject):
    def __str__(self):
        return f"{self.write_json()}"


class TenDaysProject(BaseProject):
    def __str__(self):
        return f"{self.write_json()}"


class InvestorsProject(BaseProject):
    def __str__(self):
        return f"{self.write_json()}"

print("Основні Задачі 2, Завдання 2")
print()
print("Створіть Python-програму для відображення активного статусу IT-проекта. Кожен проект має свій унікальний номер, який генерується на етапі надходження проекту в компанію. Компанія пропонує три типи реалізації проектів: «Стандартний проект», «Проект за 10 днів» та «Проект для інвесторів». «Проект за 10 днів» має націнку у 60% від загальної вартості проекту, а «Проект для інвесторів» передбачає знижку у 20% для замовника, якщо він являється інвестором компанії. За умови не вкладання в обговорені терміни, компанія несе втрати – 5% від вартості проекту за кожний прострочений тиждень.")
print()
