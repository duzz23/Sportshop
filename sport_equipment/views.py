from django.shortcuts import render
from django.urls import reverse_lazy

from sportshop.settings import EMAIL_HOST_USER
from .models import Equipment, Category, ContactSent
from django.views.generic import ListView, DetailView, CreateView,\
    UpdateView, DeleteView, TemplateView, FormView
from .forms import CategoryForm, ContactForm, ContactSendForm
from .tasks import send_email


def equipment_list_view(request):
    equipment_list = Equipment.objects.all()
    equipment_list_own = Equipment.objects.filter(is_own_shop=True)
    context = {
        'equipment_list': equipment_list,
        'equipment_list_own': equipment_list_own,
    }
    return render(request, 'sport_equipment/equipment_list.html', context)


# MVT - url
# def about_view(request):
#     return render(request, 'sport_equipment/about.html')

class AboutTemplateView(TemplateView):
    template_name = 'sport_equipment/about.html'


# CRUD - Category
class CategoryListView(ListView):
    model = Category
    template_name = 'sport_equipment/categories.html'
    context_object_name = 'categories'

    def get_queryset(self):
        # 1. Выборка
        return Category.objects.filter(is_active=True)

    def get_context_data(self, *args, **kwargs):
        # 4.
        context = super().get_context_data(*args, **kwargs)
        context['useful_information'] = 'ЧТо то полезное'

        categories = context['object_list']

        all_count = 0
        for category in categories:
            all_count += category.equipment_count

        context['all_count'] = all_count

        return context

    def get(self, request, *args, **kwargs):
        # 5. Гет запрос
        print('request', request)
        return super().get(request, *args, **kwargs)

class CategoryDetailView(DetailView):
    model = Category

    # def get_queryset(self):
    # 2.
    #     pass
    #
    # def get_object(self, queryset=None):
    # 3.
    #     pass


class CategoryCreateView(CreateView):
    model = Category
    success_url = reverse_lazy('sport_equipment:category-list')
    form_class = CategoryForm


    # def form_valid(self, form):
    #     # 7. Валидация формы
    #     pass
    #
    # def form_invalid(self, form):
    #     pass
    def post(self, request, *args, **kwargs):
        # 6. Post запрос
        print('request', request)
        return super().post(request, *args, **kwargs)


class CategoryUpdateView(UpdateView):
    model = Category
    fields = ('name',)
    success_url = reverse_lazy('sport_equipment:category-list')

    # def get_success_url(self):
    #     pass


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('sport_equipment:category-list')


class ContactFormView(FormView):
    template_name = 'sport_equipment/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('sport_equipment:contacts')

    def form_valid(self, form):
        print('cleaned_data', form.cleaned_data)
        return super().form_valid(form)

class ContactViewSendForm(CreateView):
    model = ContactSent
    form_class = ContactSendForm
    success_url = reverse_lazy('sport_equipment:main')
    template_name = 'sport_equipment/contact_form.html'

    def form_valid(self, form):
        form.save()
        send_email.delay(form.instance.email)
        # подключаю вполнение функции через celery delay() таска будет обрабатывать параллено
        return super().form_valid(form)
