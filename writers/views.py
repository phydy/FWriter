from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm #, WriterSignUpForm, ClientSignUpForm
from django.contrib import messages
#from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
#from.models import Speciality

# Create your views here.
def home(request):
    return render(request, 'writers/index.html')

'''
class ClientSignUpView(CreateView):
    model = User
    form_class = ClientSignUpForm
    template_name = 'writers/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'client'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')

class WriterCreate(CreateView):
	model = Writer
	form_class = WriterSignUpForm
	template_name = 'writers/writer_sign_up.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'writer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')
'''
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}!')
			return redirect ('login')
	else:
		form = UserRegisterForm()
	return render(request, 'writers/register.html', {'form': form})
	form_class = UserRegisterForm()


@login_required
def profile(request):
	return render(request, 'writers/profile.html')

@login_required
def terms(request):
	return render(request, 'writers/terms.html')