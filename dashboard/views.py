from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Order, Assignment #,Final_copy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
import os
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.db.models import Q
from .forms import OrderForm, AssignmentForm
#from writers.decorators import writer_required, client_required
#from django.utils.decorators import method_decorator

@login_required
def dash(request):
    context = {'orders': Order.objects.filter(Q(user_to=request.user)).order_by('-date_posted')}
    return render(request, 'dashboard/home.html', context)


#@method_decorator(writer_required, name='dispatch')
class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'dashboard/home.html'
    context_object_name = 'orders'

    def get_queryset(self):
        orders = Order.objects.filter(Q(user_assigned=self.request.user)).order_by('-date_posted')
        return orders

#@method_decorator(writer_required, name='dispatch')
class PendingOrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'dashboard/home.html'
    context_object_name = 'orders'

    def get_queryset(self):
        orders = Order.objects.filter(Q(user_assigned=self.request.user), status ='pending').order_by('-date_posted')
        return orders


#@method_decorator(writer_required, name='dispatch')
class UReviewOrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'dashboard/home.html'
    context_object_name = 'orders'

    def get_queryset(self):
        orders = Order.objects.filter(Q(user_assigned=self.request.user), status ='under_review').order_by('-date_posted')
        return orders


#@method_decorator(writer_required, name='dispatch')
class URevisionOrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'dashboard/home.html'
    context_object_name = 'orders'

    def get_queryset(self):
        orders = Order.objects.filter(Q(user_assigned=self.request.user), status ='under_revision').order_by('-date_posted')
        return orders


#@method_decorator( writer_required, name='dispatch')
class CompleteOrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'dashboard/home.html'
    context_object_name = 'orders'

    def get_queryset(self):
        orders = Order.objects.filter(Q(user_assigned=self.request.user), status ='completed').order_by('-date_posted')
        return orders


#@method_decorator( writer_required, name='dispatch')
class CanceledOrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'dashboard/home.html'
    context_object_name = 'orders'

    def get_queryset(self):
        orders = Order.objects.filter(Q(user_assigned=self.request.user), status ='canceled').order_by('-date_posted')
        return orders

#@method_decorator(client_required, name='dispatch')
class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order

#@method_decorator( client_required, name='dispatch')
class AssignmentListView(LoginRequiredMixin, ListView):
    model = Assignment
    template_name = 'dashboard/home.html'
    context_object_name = 'assignments'

    def get_queryset(self):
        assignments = Assignment.objects.filter(Q(owner=self.request.user)).order_by('-date_posted')
        return assignments

#@method_decorator( client_required, name='dispatch')
class AssignmentDetailView(LoginRequiredMixin, DetailView):
    model = Assignment


'''
@method_decorato([login_required, client_required], name='dispatch')
class AssignmentCreateView(LoginRequiredMixin, CreateView):
    model = Assignment
    fields = ['order_file', 'title', 'topic', 'content', 'time_due']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
'''

#@method_decorator( client_required, name='dispatch')
class AssignmentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Assignment
    fields = ['order_file', 'title', 'topic', 'content', 'time_due']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        assignment = self.get_object()
        if self.request.user == assignment.owner:
            return True
        return False
'''
class FinalOrderSubmitView(LoginRequiredMixin, CreateView):
    model = Final_copy
    fields = ['order', 'file_to_submit', 'complete']
'''


@login_required
#@writer_required
def submit(request):
    if request.method =="POST":
        form = OrderForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('d-dash')
    else:
        form = OrderForm()
    return render(request, 'dashboard/final_copy_form.html', {"form": form})


@login_required
#@client_required
def create(request):
    if request.method =="POST":
        form = AssignmentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('c-dash')
    else:
        form = AssignmentForm()
    return render(request, 'dashboard/assignment_form.html', {"form": form})


@login_required
def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response=HttpResponse(fh.read(), content_type="application/order_file")
            response['Content-Disposition'] = 'inline; filename='+os.path.basename(file_path)
            return response
    raise Http404

def about(request):
    return render(request, 'dashboard/about.html')



# Create your views here.
