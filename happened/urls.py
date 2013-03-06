from django.conf.urls import patterns, url
from .views import Data, Timeline


urlpatterns = patterns(
    '',

    # pylint: disable=E1101
    #         Instance of <class> has no <member>

    url(r'^timeline/$', Timeline.as_view(), name='timeline'),
    url(r'^data\.js$', Data.as_view())
)
