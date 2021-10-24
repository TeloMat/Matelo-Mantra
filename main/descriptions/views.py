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
        success = description.edit_description(response)
        if success:
            return HttpResponseRedirect("/api/descriptions/")
        # Maybe add an error message
        return HttpResponseRedirect("/api/home/")

    form = EditDescription(description)
    return render(response, "main/descriptions/description.html", {"description": description, "form": form})


def deleteDesc(response, id):
    if not response.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    Description.objects.get(id=id).delete_description()
    return redirect('/api/descriptions/')


def listDesc(response):
    if response.user.is_authenticated:
        desc_list = Description.objects.all()
        return render(response, "main/descriptions/descriptionList.html", {"list": desc_list})
    return HttpResponseRedirect('/login/')


def createDescription(response):
    if not response.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    if response.method == "POST":
        success = Description().create_description(response)
        if success:
            # Call description save method if form is valid
            return HttpResponseRedirect("/api/descriptions/")
        # Maybe add an error message
        return HttpResponseRedirect("/api/home/")
    form = CreateNewDescription()
    return render(response, "main/descriptions/descriptionCreate.html", {"form": form})


def get_curr_description(request):
    if request.method == 'GET':
        description = Description.objects.get(public=True)
        serializer = DescriptionSerializer(description)
        return JsonResponse(serializer.data, safe=False)
