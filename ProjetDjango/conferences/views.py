from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Conference
from django.views.generic import ListView,DetailView

def conferenceList(request):
    liste=Conference.objects.order_by('-start_date')
    return render(request,'conferences/conferenceList.html',{'conferenceList': liste})


class ConferenceListView(ListView):
    model=Conference
    template_name='conferences/conference_list.html'
    context_object_name="conferences"
    def get_queryset(self):
        return Conference.objects.order_by('-start_date')
    
    
class DetailViewConference(DetailView):
    model=Conference
    template_name='conferences/conference_detail_view.html'
    context_object_name="conferences"

    
