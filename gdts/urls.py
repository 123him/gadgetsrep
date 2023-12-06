from django.urls import include, path

from gdts import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
   path('api-auth/', include('rest_framework.urls')),
   path('createaccount',views.createaccount.as_view(),name='account'),
   path('auth_login',views.auth_login.as_view(),name='login'),
   path('viewaccount',views.viewaccount.as_view(),name='viewaccount'),
   path('delete_user',views.delete_user.as_view(),name='deleteaccount'),
   path('update_user',views.update_user.as_view(),name='updateaccount'),
   path('addproduct',views.addproduct.as_view(),name='product'),
   path('viewproduct',views.viewproduct.as_view(),name='view_product'),
   path('delete_product',views.delete_product.as_view(),name='delete_product'),
   path('update_product',views.update_product.as_view(),name='update_product'),

   path('product1',views.product1.as_view(),name='product'),
   path('mobile',views.mobile.as_view(),name='mobile')






]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)