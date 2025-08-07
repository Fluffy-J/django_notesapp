from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Title, Body

def index(request):
    latest_title_list = Title.objects.order_by("-pub_date")[:5]
    template = loader.get_template("notes/index.html")
    context = {"latest_title_list": latest_title_list}
    return render(request, "notes/index.html", context)


def detail(request, title_id):
    title = get_object_or_404(Title, pk=title_id)
    body = title.body
    return render(request, "notes/detail.html", {"title": title, "body": body})


def make_note(request):
    return render(request, "pages/makenote.html")


def create(request):
    if request.method == 'POST':
        title_text = request.POST.get('title')
        body_text = request.POST.get('body_text')

        title = Title.objects.create(title_text = title_text, pub_date = timezone.now())
        Body.objects.create(title=title, body_text=body_text)

        return redirect('notes:make_note')

    return render(request, 'pages/makenote.html')