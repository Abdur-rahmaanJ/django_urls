from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def add_nums(request, num_1, num_2):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return HttpResponse("""
        <h1>Sum Api</h1>
        <p>Sum of {} and {} is {}</p>
    """.format(num_1, num_2, num_1 + num_2))

def mult_nums(request, num_1, num_2):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return HttpResponse("""
        <h1>Mult Api</h1>
        <p>Mult of {} and {} is {}</p>
    """.format(num_1, num_2, num_1 * num_2))
