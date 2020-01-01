from django.views.generic import ListView
from .models import Post


class CasePageView(ListView):
    model = Post
    template_name = 'portfolio.html'
