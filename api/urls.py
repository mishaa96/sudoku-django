from django.contrib.auth.decorators import login_required
from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

from django.views.generic import TemplateView

from api.views import PuzzleViewSet, SolverView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'puzzle', PuzzleViewSet, basename="generate")
# router.register(r'validate', SolverViewSet, basename="validate")

urlpatterns = router.urls

urlpatterns += [
    path('token',
         jwt_views.TokenObtainPairView.as_view(),
         name ='token_obtain_pair'),
    path('token/refresh',
         jwt_views.TokenRefreshView.as_view(),
         name ='token_refresh'),
     path('validate', SolverView.as_view(), name='validate')
]
