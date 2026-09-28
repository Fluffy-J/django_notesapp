from django.utils import timezone

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from notes.api.serializers import Title_textSerializer
from notes.models import Title, Body

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