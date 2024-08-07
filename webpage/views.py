from django.shortcuts import render, HttpResponse

# Create your views here.


def indexPage(request):
    return render(request, 'index.html')


def aboutPage(request):
    return render(request, 'about.html')


def contactPage(request):
    return render(request, 'contact.html')


def table_Page(request):
    context = {}
    lt = list(range(0, 100))
    context["list"] = lt

    return render(request, 'table_page.html', context)


def card_Page(request):
    cardlist = {}
    lt = list(range(0, 100))
    cardlist["list"] = lt

    return render(request, 'card_page.html', cardlist)
