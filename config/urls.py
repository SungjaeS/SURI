from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    # path("about/", include("about.urls")),
    # path("news/", include("news.urls")),
    # path("search", include("search.urls")),
    # path("post/", include("post.urls")),
    # path("club/", include("club.urls")),
    path("blog/", include("blog.urls")),
    path("chat/", include("chat.urls")),
    # path("shop/", include("shop.urls")),
    # path("contact/", include("contact.urls")),
    path("accounts/", include("accounts.urls")),
    # path("tube/", include("tube.urls")),
    # path("cart/", include("cart.urls")),
    # path("order/", include("order.urls")),
    # path("coupon/", include("coupon.urls")),
    # path("board/", include("board.urls")),

    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)