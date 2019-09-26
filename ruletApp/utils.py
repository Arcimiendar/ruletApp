from . import models


def set_department_from_cookie(cls):
    class NewView(cls):
        def get_context_data(self, *args, **kwargs):
            context = super().get_context_data(*args, **kwargs)
            try:
                context['department'] = models.Department.objects.get(pk=self.request.COOKIES['department'])
            except KeyError:
                pass
            return context
    return NewView
