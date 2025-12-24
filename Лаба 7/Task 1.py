class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.id = emp_id
    
    def get_info(self):
        return f"Сотрудник {self.name}(ID: {self.id})"

class Manager:
    def __init__(self, departament):
        self.departament = departament
        self.team = []
    
    def manage_project(self):
        return f"Управляю проектом в отделе {self.departament}"
    
    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self.team.append(employee)
        else:
            raise TypeError("Можно добавить только объекты Employee")
    
class Technician:
    def __init__(self, specialization):
        self.specialization = specialization

    def perform_maintenance(self):
        return f"Выполняю ТО по специализации: {self.specialization}"
    
class TechManager(Employee, Manager, Technician):
    def __init__(self, name, emp_id, departament, specialization):
        Employee.__init__(self, name, emp_id)
        Manager.__init__(self, departament)
        Technician.__init__(self, specialization)
    
    def get_team_info(self):
        if not self.team:
            return f"У менеджера {self.name} пока нет подчинённых."
        lines = [f"Команда TechManager {self.name} (отдел: {self.departament}):"]
        for emp in self.team:
            lines.append(f"{emp.get_info()}")
        return "\n".join(lines)
    

dev = Employee("Солиев Юнус", "БСИ45")
qa = Employee("Гончаренко Елена", "ККК00")


tm = TechManager("Латышев Сергей", "TК-001", "ИТ", "Сети")


tm.add_employee(dev)
tm.add_employee(qa)


print(tm.get_info())                
print(tm.manage_project())          
print(tm.perform_maintenance())     
print(tm.get_team_info())   