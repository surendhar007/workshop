from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from django.core.urlresolvers import reverse_lazy
from braces.views import LoginRequiredMixin, AnonymousRequiredMixin
from django.views.generic.edit import FormView, UpdateView
from registration.forms import *
from registration.models import *
from django.views.generic import ListView

class HomePageView(ListView):
    template_name = "index.html"
    def get_queryset(self):
        return Chocolate.objects.all()


class UserRegistrationView(AnonymousRequiredMixin, FormView):
    template_name = "register_user.html"
    authenticated_redirect_url = reverse_lazy(u"home")
    form_class = UserRegistrationForm
    success_url = 'success.html'

    def form_valid(self, form):
        form.save()
        return FormView.form_valid(self, form)

class AddChocolateView(FormView):
    template_name="addchocolate.html"
    form_class=ChocolateAddForm
    success_url='/register/chocolate/success'

    def form_valid(self, form):
        form.save()
        return FormView.form_valid(self, form)

