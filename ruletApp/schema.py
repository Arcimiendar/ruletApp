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


schema = graphene.Schema(query=Query, mutation=Mutation)
