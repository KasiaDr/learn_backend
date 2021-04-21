from django.shortcuts import render
from logging import getLogger
from django.urls import reverse_lazy
from django.http import HttpResponse
from viewer.models import Movie, Genre
from django.views import View
from django.views.generic import TemplateView, ListView, FormView, CreateView, UpdateView, DeleteView, DetailView
from viewer.forms import MovieForm

LOGGER = getLogger()


class MovieDetailsView(DetailView):
    template_name = 'detail.html'
    model = Movie


class MovieDeleteView(DeleteView):
    template_name = 'movie_confirm_delete.html'
    model = Movie
    success_url = reverse_lazy('filmy')


class MovieUpdateView(UpdateView):
    template_name = 'form.html'
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy('filmy')

    def form_valid(self, form):
        LOGGER.warning('User provided invalid data while updating a movie.')
        return super().form_valid(form)


class MoviesView(ListView):
    template_name = 'movies.html'
    model = Movie
    paginate_by = 20


class MovieCreateView(CreateView):
    template_name = 'form.html'
    form_class = MovieForm
    success_url = reverse_lazy('movie_create')

    # class MovieCreateView(FormView)
    # def form_valid(self, form):
    #     result = super().form_valid(form)
    #     cleaned_data = form.cleaned_data
    #     Movie.objects.create(
    #         title=cleaned_data['title'],
    #         genre=cleaned_data['genre'],
    #         rating=cleaned_data['rating'],
    #         released=cleaned_data['released'],
    #         description=cleaned_data['description']
    #     )
    #     return result

    def form_invalid(self, form):
        LOGGER.warning('User provided an invalid data!')
        return super().form_invalid(form)


# ta MovieView to to samo co niżej tylko extra_context= {'object_list': Movie.objects.all()}
# class MoviesView(TemplateView):
#     template_name = 'movies.html'
#     extra_context = {'movies': Movie.objects.all().order_by('-released'),
#                      'title': "Wynik TemplateView"}
#

# class MoviesView(View):
#     def get(self, request):
#         return render(
#             request, template_name='movies.html',
#             context={'movies': Movie.objects.all().order_by('-released')}
#         )


# def movies(request):
#     return render(
#         request, template_name='movies.html',
#         context={'movies': Movie.objects.all().order_by('-released')}
#     )


def hello(request):
    s1 = request.GET.get('s1', '')
    return render(request, template_name='hello.html',
                  context={'adjectives': [s1, 'beautiful', 'wonderful', 'great'],
                           'title': s1})

    # try:
    #     s = int(request.GET.get('s', ''))
    # except Exception as ex:
    #     return HttpResponse(f'Coś poszło nie tak! Błąd: {ex}')
    #
    # tekst = f"<b>Wartość s={s}</b><br>" \
    #         f"<a href='/hello/?s={s+1}'>Link zwiększający o 1</a><br>" \
    #         f"<a href='/hello/?s={s-1}'>Link zmniejszający o 1</a><br>"
    # return HttpResponse(tekst)
