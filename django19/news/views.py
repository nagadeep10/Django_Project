from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render,get_object_or_404,redirect
from .models import post
from .forms import postform


def news_create(request):
    #if request.method == "POST":
    #    print request.POST.get("title")
    #    print request.POST.get("content")
    form=postform(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        # print form.cleaned_data.get("title")
        instance.save()
        messages.success(request,"Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form" : form,
    }
    return render(request, "news_create.html", context)


def news_list(request): # search items
    queryset_list=post.objects.all()
    paginator = Paginator(queryset_list, 5)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context={
        "object_list":queryset,
        "temp": "list",
        "title": "News"
    }
    #if request.user.is_authenticated():
    #    context = {"temp": "list","title":"News"}
    #else:
    #    context = {"temp": "Plz Log in", "title": "Log in"}
    return render(request,"news_list.html",context)
    # return HttpResponse("<h1>Hii</h1>")

def news_update(request,var=None):
    instance = get_object_or_404(post, id=var)
    form = postform(request.POST or None,request.FILES or None,instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        # print form.cleaned_data.get("title")
        instance.save()
        messages.success(request, "Saved")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "temp": "detail", "title": instance.title, "instance": instance,"form": form,
    }
    return render(request, "news_create.html", context)

def news_delete(request,var=None):
    instance = get_object_or_404(post, id=var)
    instance.delete()
    messages.success(request, "Successfully Deleted")
    return redirect("list")


def news_detail(request,var=None): # retrieve
    instance=get_object_or_404(post,id=var)
    context={"temp":"detail","title":instance.title,"instance":instance}
    return render(request,"news_detail.html",context)
    #return HttpResponse("<h1>Hii</h1>")


# Create your views here.
