class Funcionarios:
    def __init__(self, name: str, birth: str, sector: str, address: str, salary: float):
        self.name = name
        self.birth = birth
        self.sector = sector
        self.address = address
        self.salary = salary
        self.login = None
        self.birth_day = None
        self.birth_month = None
        self.birth_year = None

    def generate_login(self):
        names = self.name.lower().split(' ')
        first_name = names[0]
        for last_name in names[1:]:
            first_letter = last_name[0]
            first_name += first_letter
        self.login = first_name
    
    def get_birth_day(self):
        self.birth_day = self.birth[:2]
    
    def get_birth_month_pt(self):
        months = {
            "01": "Janeiro",
            "02": "Fevereiro",
            "03": "Março",
            "04": "Abril",
            "05": "Maio",
            "06": "Junho",
            "07": "Julho",
            "08": "Agosto",
            "09": "Setembro",
            "10": "Outubro",
            "11": "Novembro",
            "12": "Dezembro",
        }
        self.birth_month = months.get(self.birth[3:5])
    
    def get_birh_year(self):
        self.birth_year = self.birth[6:]
    
    def update_salary(self):
        if self.sector.lower() == 'operação':
            self.salary = self.salary * 0.67
        elif self.sector.lower() == 'fiscal':
            self.salary = self.salary * 0.93
    

    
eric = Funcionarios("Eric William Alvim Rodrigues", "16/12/1990", "Operação", "teste", 1000.00)
eric.generate_login()
eric.get_birth_day()
eric.get_birth_month_pt()
eric.get_birh_year()
eric.update_salary()
print(eric.login)
print(eric.birth_day)
print(eric.birth_month)
print(eric.birth_year)
print(eric.salary)
