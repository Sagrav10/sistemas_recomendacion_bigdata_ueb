from django.urls import path
from api_recomendacion.views import UsuarioView, CalifacionView, PeliculasView, calificacionesBDView, loginView,RecomendacionContenido
from api_recomendacion.viewsRecomenderUser import  ContenidoUsuarioUsuario
urlpatterns=[
    path('usuarios/',UsuarioView.as_view(), name='usuario'),
    path('usuarios/<int:cod_usuario>',UsuarioView.as_view(), name='usuario_procesar'),
    path('calificaciones/',CalifacionView.as_view(),name='califiacionesLista'),
    path('calificaciones/<int:cod_usuario>', CalifacionView.as_view(), name='califiacionesLista'),
    path('peliculas/',PeliculasView.as_view(),name='peliculas'),
    path('bd/', calificacionesBDView.as_view(), name='bd'),
    path('login/', loginView.as_view(), name='bd'),
    path('recomendacionContenido/',RecomendacionContenido.as_view(),name="recomendacionContenido"),
    path('recomendacionUsuario/<int:cod_usuario>',ContenidoUsuarioUsuario.as_view(),name="recomendacionUsuario")
]
