from django.shortcuts import get_object_or_404, render
from django.template import loader


from .models import Title, Body

def index(request):
    latest_title_list = Title.objects.order_by("-pub_date")[:5]
    template = loader.get_template("notes/index.html")
    context = {"latest_title_list": latest_title_list}
    return render(request, "notes/index.html", context)


def detail(request, title_id):
    title = get_object_or_404(Title, pk=title_id)
    body = title.body_set.get(pk=title.id)
    return render(request, "notes/detail.html", {"title": title, "body": body})