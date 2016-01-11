from django.views.generic import FormView

from .forms import SimpleForm, CreditCardForm, CartForm


# Create your views here.
class MainView(FormView):
    template_name = 'forms/index.html'
    form_class = SimpleForm
