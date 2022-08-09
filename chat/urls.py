from django.urls import path
# from shortuuidfield import ShortUUIDField

from . import views 


urlpatterns = [
    path('',views.lobby),
    path('list/',views.listUsers),
    path('listchatrooms/',views.listChatrooms),
    path('createchatroom/<int:pk>',views.createChatRoom, name='create_chatroom'),
    path('getchatroom/<str:chatUuid>',views.getChatRoom, name='get_chatroom'),
    # createMessage

]