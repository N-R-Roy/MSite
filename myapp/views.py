import datetime
import time
from urllib.parse import urlencode

from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings

from myapp.models import PersonInfo, Song, Employee, MyModel, MyModel2
from .forms import PersonForm, AddForm, UpdateForm, EmployeeForm

from django.views.generic import TemplateView, RedirectView, View
from django.views import generic
from django import views
from django.core.files.storage import FileSystemStorage


# def index(request):
#     person_list = PersonInfo.objects.all()
#     p_form = PersonForm()
#     return render(request, "myapp/index.html", {'person_list': person_list, 'p_form': p_form})


class Index(generic.ListView):
    model = PersonInfo
    template_name = "myapp/index.html"
    context_object_name = 'person_list'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.request.session['heloo'])
        self.request.session.set_test_cookie()
        # context["person_list"] = PersonInfo.objects.all()
        context["time"] = datetime.datetime.now()
        return context


class AddressCView(generic.ListView):
    model = PersonInfo
    template_name = "myapp/index.html"
    context_object_name = 'person_list'
    paginate_by = 2

    def get_queryset(self):
        return PersonInfo.objects.filter(address__icontains=self.kwargs['address'])


class PreLoadView(RedirectView):
    # url = ""
    pattern_name = "myapp:show_page_view"

    def get_redirect_url(self, *args, **kwargs):
        # print(">>>>>>>>>>>>>>>>>>>>>>>>>")
        # print(kwargs["num1"])
        # print(kwargs["num2"])
        # print(">>>>>>>>>>>>>>>>>>>>>>>>>")
        # if int(kwargs["id"]) > 500:
        #     self.url = reverse_lazy("myapp:show_page_view", args=(kwargs["id"], kwargs["id2"],))
        # else:
        #     self.url = reverse_lazy("myapp:index")
        # base_url = reverse_lazy('myapp:mv_page')
        # query_string = urlencode({'num1': "500", 'num2': "700"})
        # self.url = '{}?{}'.format(base_url, query_string)
        return super().get_redirect_url(*args, **kwargs)


class ShowPageView(TemplateView):
    template_name = "myapp/show_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["id_v"] = kwargs.get('id')
        return context


class MView(View):
    template_name = "myapp/mv_page.html"

    def get(self, request):
        data = request.GET
        nm1 = data.get("num1")
        nm2 = data.get("num2")
        print(request.COOKIES)
        print((int(nm1) + int(nm2)))
        if (int(nm1) + int(nm2)) > 500:
            return reverse_lazy("myapp:preload", args=(222, 333,))
        return render(request, self.template_name, {'nm1': nm1, 'nm2': nm2})


class PersonDetailView(generic.DetailView):
    model = PersonInfo
    template_name = "myapp/person_detail.html"
    context_object_name = "person"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["time"] = datetime.datetime.now()
        return context


class AddPersonForm(generic.FormView):
    template_name = "myapp/add_form.html"
    form_class = AddForm
    success_url = reverse_lazy("myapp:index")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CreatePersonView(generic.CreateView):
    model = PersonInfo
    fields = ['name', 'address', 'age']
    # form_class = AddForm  # instead of model and fields use model form_class
    template_name = 'myapp/create_person.html'
    success_url = reverse_lazy("myapp:index")


class UpdatePersonView(generic.UpdateView):
    model = PersonInfo
    fields = ['name', 'address']
    template_name = 'myapp/update_person.html'
    success_url = reverse_lazy("myapp:index")


class DeletePersonView(generic.DeleteView):
    model = PersonInfo
    template_name = 'myapp/delete_person.html'
    success_url = reverse_lazy("myapp:index")


class SongListView(generic.ListView):
    model = Song
    context_object_name = 'song_list'
    template_name = 'myapp/song_list.html'


class CreateSongView(generic.CreateView):
    model = Song
    fields = ['title', 'singer']
    template_name = "myapp/create_song.html"


def employee_vw(request):
    # print(request.method)
    if request.method == 'POST':
        print("Hello")
        # form = EmployeeForm(request.POST, request.FILES)
        name = request.POST['ename']
        # print(name)
        file = request.FILES['efile']
        # print(str(file))
        # print(str(file.content_type))
        # print(str(file.name))
        # print(str(file.size))

        fs = FileSystemStorage(location=settings.MEDIA_ROOT + "/employee_image/")

        file_name = fs.save(file.name, file)

        emp = Employee(name=name, file="employee_image/" + str(file_name))
        emp.save()
        # url = fs.url(name)
        # return HttpResponse(str(url))
        return HttpResponseRedirect(reverse_lazy("myapp:emp_list"))
    else:
        request.session['heloo'] = "Hello"
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
            print("Work")
        else:
            print("Please enable cookies and try again.")
        form = EmployeeForm()
        return render(request, 'myapp/employee.html', {'form': form})


class EmployeeList(generic.ListView):
    model = Employee
    template_name = "myapp/employee_list.html"
    context_object_name = 'emp_list'

    def get_queryset(self):
        empp_list = Employee.objects.all()
        # empp_list = Employee.objects.all()[:2]
        return empp_list


class MyView(generic.View):
    def get(self, request):
        return render(request, "myapp/my_form_file.html")

    def post(self, request):
        user_file = request.FILES['file']

        fs = FileSystemStorage(location='media/my_photo/')

        filename = fs.save(user_file.name, user_file)

        user_name = request.POST['name']

        f_obj = MyModel2(name=user_name, image="my_photo/" + str(filename))
        f_obj.save()

        return HttpResponseRedirect(reverse_lazy("myapp:file_obj_list"))


class FileListView(generic.ListView):
    model = MyModel2
    template_name = "myapp/file_obj_list.html"
    context_object_name = "f_obj_list"
