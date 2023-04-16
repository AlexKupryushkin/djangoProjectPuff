from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from .forms import *
from .models import Divan, Orders
from .cart import DivanCart


class HomeListView(View):

    """домашняя страница"""

    def get(self, request):
        return render(
            request, "soft/home.html"
        )


class DivanListView(View):
    def get(self, request):
        return render(
            request, "soft/main.html",
        )


class Divan1ListView(View):

    """прямые диваны"""

    def get(self, request):
        return render(
            request, "soft/list.html",
            {
                'divans': Divan.objects.filter(type=1),
            }
        )


class Divan2ListView(View):

    """угловые диваны"""

    def get(self, request):
        return render(
            request, "soft/list.html",
            {
                'divans': Divan.objects.filter(type=2)
            }
        )


class DivanView(View):
    def get(self, request, divan_id: int):
        return render(
            request, "soft/detail.html",
            {
                "divan": get_object_or_404(Divan, id=divan_id),
                "cart": DivanCart(request)
            }
        )


# ------------------

# def adddivan(request):

'''добавление дивана'''


#     if request.method == 'POST':
#         form = AddDivanForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             try:
#                 Divan.objects.create(**form.cleaned_data)
#                 return redirect('home')
#             except:
#                 form.add_error(None, 'Ошибка добавления!')
#     else:
#         form = AddDivanForm()
#     return render(request, 'soft/adddivan.html', {'title': 'Добавление!',
#                                                   'form': form})

# ------------------


class AddDivanView(View):

    """добавление дивана в корзину"""

    def post(self, request, divan_id: int):
        divan = get_object_or_404(Divan, id=divan_id)
        form = DivansAddForm(request.POST)
        if form.is_valid():
            cart = DivanCart(request)
            cart.add(
                divan=divan,
                quantity=form.cleaned_data["count"],
                update_quantity=True,
            )
        return redirect("show-cart")


class ShowCartView(View):

    """просмотр корзины"""

    def get(self, request):
        cart = DivanCart(request).create_objects()
        if cart:
            return render(
                request, "soft/cart.html", {"cart": cart,
                                            "form": CreateOrderForm()
                                            }
            )
        return redirect("show-cart")

    def post(self, request):
        form = CreateOrderForm(request.POST)
        cart = DivanCart(request).create_objects()

        if form.is_valid():

            for divan_order in cart.create_objects().divans:
                order = Orders.objects.create(
                    divan=divan_order,
                    count=divan_order.count,
                    phone=form.cleaned_data["phone"],
                    address=form.cleaned_data["address"],
                    name=form.cleaned_data["name"],
                )
                request.session["orders"].append(order.id)

            cart.clear()

            return render(request, "soft/thanks.html")

        return render(request, "soft/cart.html", {"cart": cart,
                                                  "form": form
                                                  }
                      )


# DataMixin,

class DataMixin:
    pass


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'soft/register.html'
    success_url = reverse_lazy('login')

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     c_def = self.get_user_context(title="Регистрация")
    #     return dict(list(context.items()) + list(c_def.items()))

# class RegisterUser(View):
#
#     def get(self, request):
#         return render(
#             request, "soft/register.html"
#         )
