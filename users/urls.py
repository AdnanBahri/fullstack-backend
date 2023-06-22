from django.urls import path
from .views import UserCreateView, UserList, ProfileList, ProfileViewSets
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/accounts/profile/me', ProfileViewSets)

urlpatterns = [
    path('api/accounts/register/', UserCreateView.as_view(), name='register'),
    path('api/accounts/profiles/', ProfileList.as_view(), name='profiles'),
    path('api/accounts/list/', UserList.as_view(), name='users'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]+router.urls
