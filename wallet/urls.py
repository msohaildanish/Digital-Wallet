from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^wallet/$', views.WalletList),
    url(r'^wallet/(?P<pk>[0-9]+)/$', views.WalletDetail),
    url(r'^wallet/current/$',views.getAmountinWalletforStore),
    url(r'^wallet/transaction/$',views.debitView),
]

urlpatterns = format_suffix_patterns(urlpatterns)