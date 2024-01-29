import random
from django.views.generic import TemplateView
from .models import Model1, Model2

from django.views.generic import TemplateView
from .models import Model1, Model2, CC1


def generate_random_string():
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10))


def create_random_data():
    Model1.objects.all().delete()
    Model2.objects.all().delete()

    for _ in range(3):
        Model1.objects.create(
            f1=random.randint(1, 100),
            f2=generate_random_string(),
            f3=random.random(),
            f4=random.random()
        )

    for _ in range(3):
        Model2.objects.create(
            f1=random.randint(1, 100),
            f2=generate_random_string(),
            f3=random.random(),
            f4=random.random()
        )


def getCombinedData():
    m1s = Model1.objects.all()
    m2s = Model2.objects.all()
    return list(zip(m1s, m2s))


class Link1View(TemplateView):

    template_name = 'link1.html'

    def get_context_data(self, **kwargs):
        create_random_data()

        context = super().get_context_data(**kwargs)
        combined_data = getCombinedData()
        data = []
        for m1, m2 in combined_data:
            data.append(CC1(m1, m2).get_link1_data())
        context['data'] = data
        return context


class Link2View(TemplateView):
    template_name = 'link2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        input_value = float(self.request.GET.get('eval', 0))
        combined_data = getCombinedData()
        data = []
        for m1, m2 in combined_data:
            fields = CC1(m1, m2).get_link2_data()
            fields['total'] = sum(fields.values())+input_value
            data.append(fields)

        context['data'] = data
        return context
