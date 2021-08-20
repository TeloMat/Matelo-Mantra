from django.http import HttpResponseForbidden, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render

from .forms import EditDescription, CreateNewDescription
from .models import Description
from .serializers import DescriptionSerializer


def indexDesc(response, id):
    if not response.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    description = Description.objects.get(id=id)
    if response.method == "POST":
        form = EditDescription(description, response.POST)
        if form.is_valid():
            description.name = form.cleaned_data["name"]
            description.text = form.cleaned_data["text"]
            description.public = form.cleaned_data["public"]
            description.save()
            if response.FILES.get('picture'):
                description.picture.save(description.name + "_pp.jpg", response.FILES.get('picture'))
            return redirect('/api/descriptions/')

    form = EditDescription(description)
    return render(response, "main/descriptions/description.html", {"description": description, "form": form})


def deleteDesc(response, id):
    if not response.user.is_authenticated:
        return HttpResponseRedirect('/login/')

    desc = Description.objects.get(id=id)
    desc.picture.delete()
    desc.delete()
    return redirect('/api/descriptions/')


def listDesc(response):
    if response.user.is_authenticated:
        dList = Description.objects.all()
        return render(response, "main/descriptions/descriptionList.html", {"list": dList})
    return HttpResponseRedirect('/login/')


def createDescription(response):
    if not response.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    if response.method == "POST":
        form = CreateNewDescription(response.POST)
        print(form.errors)
        if form.is_valid():

            name = form.cleaned_data["name"]
            text = form.cleaned_data["text"]
            quote = form.cleaned_data["quote"]
            public = form.cleaned_data["public"]
            desc = Description(name=name, text=text, quote=quote, public=public)
            desc.save()

            if response.FILES.get('picture'):
                desc.picture.save(desc.name + "_pp.jpg", response.FILES.get('picture'))
            if response.FILES.get('musician'):
                desc.picture.save(desc.name + "_menu1.jpg", response.FILES.get('musician'))
            if response.FILES.get('traveler'):
                desc.picture.save(desc.name + "_menu2.jpg", response.FILES.get('traveler'))
            if response.FILES.get('writer'):
                desc.picture.save(desc.name + "_menu3.jpg", response.FILES.get('writer'))

            desc.save()
            return HttpResponseRedirect("/api/descriptions/")

    form = CreateNewDescription()
    return render(response, "main/descriptions/descriptionCreate.html", {"form": form})


def get_curr_description(request):
    if request.method == 'GET':
        description = Description.objects.get(public=True)
        serializer = DescriptionSerializer(description)
        return JsonResponse(serializer.data, safe=False)
