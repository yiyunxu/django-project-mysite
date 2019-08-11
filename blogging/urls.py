from django.urls import path, include
from blogging.views import stub_view, list_view, detail_view, PostViewSet, CategoryViewSet
from blogging.feeds import LatestPosts
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
    path('', list_view, name="blog_index"),
    path('latest/feed/', LatestPosts()),
    path('api_root/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

'''
from django.urls import include, path
from rest_framework import routers
from tutorial.quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
'''