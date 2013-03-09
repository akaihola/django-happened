import datetime
from django.core.serializers.json import Serializer
from django.http import HttpResponse
from django.utils.timezone import is_aware
from django.views.generic import TemplateView
import time
from .models import Event


class Timeline(TemplateView):
    template_name = 'happened/timeline.html'


def default(o):
    if isinstance(o, datetime.datetime):
        return int(1000 * time.mktime(o.utctimetuple()))
    elif isinstance(o, datetime.date):
        return int(1000 * time.mktime(o.timetuple()))
    elif isinstance(o, datetime.time):
        if is_aware(o):
            raise ValueError("JSON can't represent timezone-aware times.")
        r = o.isoformat()
        if o.microsecond:
            r = r[:12]
        return r


class JavaScriptSerializer(Serializer):
    """Converts a queryset to JavaScript with date/time as new Date()"""
    internal_use_only = False

    def get_dump_object(self, obj):
        return {'start': obj.start,
                'end': obj.end,
                'content': obj.title,
                'group': obj.group,
                'className': 'className'}

serializer = JavaScriptSerializer()


class Data(TemplateView):
    def get(self, request):
        # pylint: disable=E1101
        #         Instance of <class> has no <member>

        events = Event.objects.all()
        json = serializer.serialize(events, default=default)
        expr = u'data = {0};'.format(json)
        return HttpResponse(expr, content_type='application/javascript')
