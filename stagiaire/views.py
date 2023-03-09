import qrcode
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404,redirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Filiaire, Program, Student
from .forms import StudentForm, UserForm, FiliaireForm


def home(request):
    return render(request, 'home.html')


class FiliaireCreateView(CreateView):
    model = Filiaire
    form_class = FiliaireForm
    template_name = 'add_filiaire.html'


class FiliaireListView(ListView):
    model = Filiaire
    template_name = 'filiaire_list.html'




class ProgramListView(ListView):
    model = Program
    template_name = 'program_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(option_id=self.kwargs['option_id'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['option'] = Filiaire.objects.get(pk=self.kwargs['option_id'])
        return context


class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'


def user_register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = StudentForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = StudentForm()

    content = {
        'registered': registered,
        'form1': user_form,
        'form2': profile_form,

    }
    return render(request, 'register.html', content)


class ProgramView(CreateView):
    model = Program
    fields = '__all__'
    template_name = 'add_program.html'




class StudentListViews(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'
    ordering = ['-id']
    paginate_by = 10


@method_decorator(login_required, name='dispatch')
class StudentCreateView(CreateView):
    model = Student
    template_name = 'student_form.html'
    fields = ['user', 'promotion', 'photo', 'option', 'sex', 'end_stage']
    success_url = reverse_lazy('student_list')



@login_required
def generate_card(request, pk):
    student = get_object_or_404(Student, id=pk)
    filiaire = student.option

    # generate QR code for the filiaire's program
    qr_code = qrcode.QRCode(version=1, box_size=10, border=5)
    qr_code.add_data(filiaire.program_set.first().programme)
    qr_code.make(fit=True)
    qr_code_img = qr_code.make_image(fill_color="black", back_color="white")

    # render the student card template with the student and filiaire information
    context = {'student': student, 'filiaire': filiaire, 'qr_code_img': qr_code_img}
    return render(request, 'student_card.html', context=context)




def user_login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Vous n'avez pas été authentifier")
        else:
            return HttpResponse("Mot de passe ou username incorrect")
    else:
        return render(request, 'login.html')


def clear_students(request):
    if request.method == 'POST':
        Student.objects.all().delete()
        return redirect('student_list')
    return render(request, 'clear_students.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
