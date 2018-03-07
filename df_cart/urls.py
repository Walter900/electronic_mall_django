from django.conf.urls import url
import views
urlpatterns = [

    url(r'^$', views.cart),
    url(r'^add(\d+)_(\d+)/$', views.add),
    #url(r'^logout/$', views.logout),
    #url(r'^info/$', views.info),
    #url(r'^order/', views.order),
    #url(r'^site/$', views.site),
    #url(r'^logout/$', views.logout),
    #


]