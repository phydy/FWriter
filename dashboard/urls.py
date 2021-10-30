 from django.urls import path
from . import views
from .views import (
    OrderListView, 
    OrderDetailView, 
    AssignmentListView, 
    AssignmentDetailView, 
    #AssignmentCreateView, 
    AssignmentUpdateView,
    #FinalOrderSubmitView,
    PendingOrderListView,
    UReviewOrderListView,
    URevisionOrderListView,
    CompleteOrderListView,
    CanceledOrderListView
)

urlpatterns = [
    path('order/', OrderListView.as_view(), name = 'd-dash'),
    path('pending/', PendingOrderListView.as_view(), name = 'p-order'),
    path('review/', UReviewOrderListView.as_view(), name = 'u-review'),
    path('revision/', URevisionOrderListView.as_view(), name = 'u-revision'),
    path('comleted/', CompleteOrderListView.as_view(), name = 'o-completed'),
    path('canceled/', CanceledOrderListView.as_view(), name = 'o-canceled'),
    path('assignment/', AssignmentListView.as_view(), name = 'c-dash'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name = 'order-detail'),
    path('assignment/<int:pk>/', AssignmentDetailView.as_view(), name = 'a-detail'),
    #path('assignment/new/', AssignmentCreateView.as_view(), name = 'a-create'),
    path('assignment/<int:pk>/new/', AssignmentUpdateView.as_view(), name = 'a-update'),
    #path('submit/', FinalOrderSubmitView.as_view(), name = 'd-submit'),
    path('about/', views.about, name = 'd-about')
    
]