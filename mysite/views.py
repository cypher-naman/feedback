from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import FeedbackForm

from .models import Feedback
from django.contrib import messages

def feedback_form(request):
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        messages.success(request,"Successfully Created.")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {"form":form}
    return render(request, 'mysite/feedback_form.html',context)
    # if request.method == 'POST':
    #     form = FeedbackForm(request.POST)
    #     context = {"form":form}
    #     if form.is_valid():
    #         form.save()
    #         return render(request, 'mysite/thanks.html',context)
    # else:
    #     form = FeedbackForm()
    # return render(request, 'mysite/feedback_form.html', {'mysite': form})

def try_to_connect(request):
    return render(request,'mysite/index.html')






def feedback_create(request):
    queryset = Feedback.objects.all()
    context = {"objectList":queryset,
    "title":'create'}
    # if request.user.is_authenticated():
    #     context = {"title":"create"}
    # else :
        # context = {"title":"invalid create"}
    return render(request,'mysite/core.html',context)

def feedback_detail(request, pk):
    instance = get_object_or_404(Feedback,pk=pk)
    context = {"Section":instance.Section_name,
    "instance":instance}
    return render(request,'mysite/detail.html',context)

def feedback_update(request, pk=None):
    instance = get_object_or_404(Feedback,pk=pk)
    form = FeedbackForm(request.POST or None, instance = instance)
    if form.is_valid():
        instance = form.save()
        instance.save()
        messages.success(request,"Successfully updated.")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {"form":form,
    "instance":instance}
    return render(request,'mysite/detail.html',context)

def feedback_delete(request, pk):
    instance = get_object_or_404(Feedback,pk=pk)
    instance.delete()
    messages.success(request,"Successfully deleted.")
    return redirect("mysite:create")
