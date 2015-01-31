from mygame import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from main.views import LoginView
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('main.views',
    # Examples:
    # url(r'^$', 'mygame.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'index', name='home'),
    url(r'^login/$', LoginView.as_view(), name = 'login'),
    url(r'^logout/$', 'log_out', name = 'logout'),
    url(r'^test/$', 'test', name='test'),
    url(r'^stats/$', 'stats', name='stats'),
    url(r'^question/(?P<qid>\d+)$', 'get_question', name='question'),
    url(r'^correct/(?P<qid>\d+)/(?P<tid>\d+)$', 'score_answer', name='score_answer')
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
