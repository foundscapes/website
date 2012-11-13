from django.shortcuts import render_to_response
from foundscapes.site.models import Tape
# Create your views here.

def tape_index(request):
    # context = {'name': 'tape_name'}
    # return render_to_response('audio_index.html', context)
    my_tapes = Tape.objects.all()
    return render_to_response('audio_index.html', {'my_tapes': my_tapes})

# def index1(request):

def tape_detail(request):
    the_tape = Tape.objects.get(id=request.GET.get('id'))
    return render_to_response('tape_detail.html', {'the_tape': the_tape})

    
    