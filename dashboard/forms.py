from django.forms import ModelForm
from .models import Assignment, Order

class AssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = ['order_file', 'title', 'topic', 'content', 'time_due']
        

    def save(self, commit=True):
        assignment = super().save(commit=False)
        return assignment


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['file_upload']

    def save(self, commit=True):
        order = super().save(commit=False)
        return order