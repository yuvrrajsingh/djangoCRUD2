from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from .forms import StudentRegistration
from .models import User
from django.views.generic.base import TemplateView, RedirectView, View

# Create your views here.

class UserAddShowView(TemplateView):

    template_name = 'crud/addandshow.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['form'] = StudentRegistration()
        data['stud'] = User.objects.all()
        return data

    def post(self, request):
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')

class EditView(View):

    def get(self,request, i):
        y = User.objects.get(id=i)
        fm = StudentRegistration(instance=y)
        return render(request, 'crud/updatestud.html', {'form':fm})

    def post(self, request, i):
        y = User.objects.get(id=i)
        fm = StudentRegistration(request.POST, instance=y)
        if fm.is_valid():
            fm.save()
        return redirect("/")

#
# def edit(request, i):
#     y = User.objects.get(id=i)
#     if request.method == 'POST':
#         f = StudentRegistration(request.POST, instance=y)
#         if f.is_valid():
#             f.save()
#
#         return redirect('/')
#
#
#     else:
#         f = StudentRegistration(instance=y)
#
#         return render(request, 'crud/updatestud.html', {'form':f, 'id':i})



class DeleteView(RedirectView):
    url = '/'
    def get_redirect_url(self, *args, **kwargs):

        d = User.objects.get(id = kwargs['i'])
        d.delete()
        return super().get_redirect_url(*args, **kwargs)
