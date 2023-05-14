from rest_framework import routers
from django.urls import include, path
from .views import (
    ReviewViewset,
    TitleViewSet,
    CommentViewset,
    APIGetToken,
    GenreViewSet,
    CategoryViewSet,
    UserViewSet,
    UserCreateView
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'titles', TitleViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'titles/(?P<title_id>\d+)/reviews',
                ReviewViewset, basename='reviews')
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewset, basename='comments'
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/token/', APIGetToken.as_view()),
    path('v1/auth/signup/', UserCreateView.as_view())
]
