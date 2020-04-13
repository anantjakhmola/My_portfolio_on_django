from django.contrib import admin
from django.urls import path
import jobs.views
# Import the below 2 things if you want to add static files.
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', jobs.views.nick, name='home'),
                  # Step 2:writing a url:here 'nick is the work after / and after the comma we have which view file is going
                  # to import the function here the file is in jobs app
                  # Add the below line to connect the settings
                    path('jobs/<int:job_id>',jobs.views.detail,name='detail'),
              ]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
