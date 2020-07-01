
from django.urls import path
from UserAuth import views

app_name = 'UserAuth'


urlpatterns = [
    path('register/',views.register,name = 'register'),
    path('user_login/',views.user_login,name = 'user_login'),
    #path('admin/', admin.site.urls),
    #path('base/',views.base,name = 'base'),

]
