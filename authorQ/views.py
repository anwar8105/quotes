# We require ListView to gather database values
from django.views.generic import ListView
from .models import AutherQ  # import our database model

# Create your views here.
class HomePageView(ListView):
    model = AutherQ
    template_name = "index.html"  # home page
    context_object_name = "all_author_quotes"
