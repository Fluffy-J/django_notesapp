from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.shortcuts import render, redirect
from django.utils import timezone

from rest_framework import generics
from notes.api.serializers import Title_textSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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


def delete(request, id):
    if request.method =='POST':
        title = get_object_or_404(Title, id=id)
        title.delete()
        return redirect('notes:index')
    return redirect('notes:detail', id =id)


class TitleListCreate(generics.ListCreateAPIView):
    queryset = Title.objects.all()
    serializer_class = Title_textSerializer


class NoteCreate(APIView):
    def post(self, request):
        title_text = request.data.get('title')
        body_text = request.data.get('body_text')

        title = Title.objects.create(title_text=title_text, pub_date=timezone.now())
        Body.objects.create(title=title, body_text=body_text)

        serializer = Title_textSerializer(title)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class NoteUpdate(APIView):
    def put(self, request, pk):
        try:
            note = Title.objects.get(pk=pk)
        except Title.DoesNotExist:
            return Response({"error": "Note not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = Title_textSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoteDelete(APIView):
    def delete(self, request, id):
        try:
            note = Title.objects.get(id=id)
        except Title.DoesNotExist:
            return Response({"error": "Note not found"}, status=status.HTTP_404_NOT_FOUND)

        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
