from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

def redirect_to_tweet(request):
    return redirect('/tweet/')  # Redirects root URL to /tweet/

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tweet/', include('tweet_beginner_app.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', redirect_to_tweet),  # Redirect root to /tweet/
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
