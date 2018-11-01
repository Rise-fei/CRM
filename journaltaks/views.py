from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from journaltaks import models
from django.contrib import auth


# Create your views here.
def journal(request):
    journal_list = models.Journal.objects.all()
    return render(request, 'journal_task/journal.html', {'journal_list': journal_list})


def edit(request, pk):
    journal_list = models.Journal.objects.all()
    return render(request, 'journal_task/edit_journal.html',
                  {'journal_list': journal_list})
