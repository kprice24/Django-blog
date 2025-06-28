from django.shortcuts import render, get_object_or_404
from polling.models import Poll
def list_view(request):
    ctx = { 'polls': Poll.objects.all() }
    return render(request, 'polling/list.html', ctx)
def detail_view(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    if request.method == 'POST':
        poll.score += 1 if request.POST.get('vote') == 'Yes' else -1
        poll.save()
    return render(request, 'polling/detail.html', {'poll': poll})
