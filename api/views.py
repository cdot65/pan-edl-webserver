from django.http import HttpResponse
from rest_framework import viewsets
from .models import EDLEntry
from .serializers import EDLEntrySerializer


class EDLEntryViewSet(viewsets.ModelViewSet):
    queryset = EDLEntry.objects.all()
    serializer_class = EDLEntrySerializer


def edl_view(_):
    entries = EDLEntry.objects.filter(is_active=True)
    content = "\n".join(str(entry.entry_value) for entry in entries)
    return HttpResponse(content, content_type='text/plain')
