import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType
from . import models


class DepartmentType(DjangoObjectType):
    class Meta:
        model = models.Department


class EmployeeType(DjangoObjectType):
    class Meta:
        model = models.Employee

    def resolve_image(self, info, **kwargs):
        return self.image.url


class RuletSessionType(DjangoObjectType):
    class Meta:
        model = models.RuletSession


class RuletChoiceType(DjangoObjectType):
    class Meta:
        model = models.RuletChoice


class Query(ObjectType):
    department = graphene.Field(DepartmentType, id=graphene.Int())
    departments = graphene.List(DepartmentType)
    employee = graphene.Field(EmployeeType, id=graphene.Int())
    employees = graphene.List(EmployeeType)
    employees_without_department = graphene.List(EmployeeType)
    rulet_session = graphene.Field(RuletSessionType, id=graphene.Int())
    rulet_sessions = graphene.List(RuletSessionType)
    rulet_choice = graphene.Field(RuletChoiceType, id=graphene.Int())
    rulet_choices = graphene.List(RuletChoiceType, rulet_session_id=graphene.Int())

    def resolve_department(self, info, **kwargs):
        pk = kwargs.get('id')

        if pk is not None:
            try:
                return models.Department.objects.get(pk=pk)
            except models.Department.DoesNotExist:
                return None
        else:
            return None

    def resolve_departments(self, info, **kwargs):
        return models.Department.objects.all()

    def resolve_employee(self, info, **kwargs):
        pk = kwargs.get('id')

        if pk is not None:
            try:
                return models.Employee.objects.get(pk=pk)
            except models.Employee.DoesNotExist:
                return None
        else:
            return None

    def resolve_employees(self, info, **kwargs):
        return models.Employee.objects.all()

    def resolve_employees_without_department(self, info, **kwargs):
        return models.Employee.objects.filter(department=None)

    def resolve_rulet_session(self, info, **kwargs):
        pk = kwargs.get('id')

        if pk is not None:
            try:
                return models.RuletSession.objects.get(pk=pk)
            except models.RuletSession.DoesNotExist:
                return None
        else:
            return None

    def resolve_rulet_sessions(self, info, **kwargs):
        return models.RuletSession.objects.all()

    def resolve_rulet_choice(self, info, **kwargs):
        pk = kwargs.get('id')

        if pk is not None:
            try:
                return models.RuletChoice.objects.get(pk=pk)
            except models.RuletChoice.DoesNotExist:
                return None
        else:
            return None

    def resolve_rulet_choices(self, info, **kwargs):
        pk = kwargs.get('rulet_session_id')
        if pk is not None:
            try:
                return models.RuletSession.objects.get(pk=pk).rulet_choices
            except models.RuletSession.DoesNotExist:
                return None
        else:
            return None


class EmployeeInput(graphene.InputObjectType):
    id = graphene.ID()
    department_id = graphene.ID()


class DepartmentInput(graphene.InputObjectType):
    id = graphene.ID()


class ClearDepartment(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    ok = graphene.Boolean()
    department = graphene.Field(DepartmentType)

    @staticmethod
    def mutate(root, info, id: int, input: DepartmentType = None):
        ok = False
        try:
            department = models.Department.objects.get(pk=id)
        except models.Department.DoesNotExist:
            department = None

        if department is not None:
            ok = True
            for employee in department.employees.all():
                employee.department = None
                employee.save()

        return ClearDepartment(ok=ok, department=department)


class ClearAllDepartments(graphene.Mutation):
    class Arguments:
        pass

    ok = graphene.Boolean()
    departments = graphene.List(DepartmentType)

    @staticmethod
    def mutate(root, info, input: DepartmentType = None):
        ok = True
        departments = models.Department.objects.all()
        for employee in models.Employee.objects.all():
            employee.department = None
            employee.save()

        return ClearAllDepartments(ok=ok, departments=departments)


class DepartmentNotPartcicipate(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    ok = graphene.Boolean()
    department = graphene.Field(DepartmentType)

    @staticmethod
    def mutate(root, info, id: int, input: DepartmentInput = None):
        ok = False

        try:
            department = models.Department.objects.get(pk=id)
        except models.Department.DoesNotExist:
            department = None

        if len(models.RuletSession.objects.filter(active=True)) > 0 and department is not None:
            department.rulet_state = models.Department.RULET_STATE[2][0]
            department.save()
            ok = True

        return DepartmentNotPartcicipate(ok=ok, department=department)


class SetDepartmentToEmployee(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = EmployeeInput(required=True)

    ok = graphene.Boolean()
    employee = graphene.Field(EmployeeType)

    @staticmethod
    def mutate(root, info, id: int, input: EmployeeInput = None):
        ok = False
        try:
            employee = models.Employee.objects.get(pk=id)
        except models.Employee.DoesNotExist:
            employee = None

        if employee is models.Employee:
            ok = True
            try:
                models.Department.objects.get(pk=input.department_id)
                employee.department_id = input.department_id
            except models.Department.DoesNotExist:
                employee.department_id = None
            employee.save()

        return SetDepartmentToEmployee(ok=ok, employee=employee)


class Mutation(ObjectType):
    set_department_to_employee = SetDepartmentToEmployee.Field()
    clear_department = ClearDepartment.Field()
    clear_all_department = ClearAllDepartments.Field()
    department_not_participate = DepartmentNotPartcicipate.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
