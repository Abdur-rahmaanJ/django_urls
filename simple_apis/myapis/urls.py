from django.urls import path, include
from . import views

urlpatterns = [
    path('maths/sum/<int:num_1>/<int:num_2>', views.add_nums),
    path('maths/mult/<int:num_1>/<int:num_2>', views.mult_nums),
]