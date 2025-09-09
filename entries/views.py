from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from datetime import datetime

from .models import Entry


class LockedView(LoginRequiredMixin):
    login_url = "login"


class EntryListView(LockedView, ListView):
    model = Entry
    context_object_name = 'entry_list'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Entry.objects.all().order_by("-date_created")
        
        # Search filter (title + content)
        search = self.request.GET.get('search', '').strip()
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | Q(content__icontains=search)
            )
        
        # Date filter
        date_filter = self.request.GET.get('date', '').strip()
        if date_filter:
            try:
                filter_date = datetime.strptime(date_filter, '%Y-%m-%d').date()
                queryset = queryset.filter(date_created__date=filter_date)
            except ValueError:
                pass  # Invalid date format, ignore filter
        
        # Date range filters
        date_range = self.request.GET.get('date_range', '').strip()
        if date_range == 'today':
            queryset = queryset.filter(date_created__date=datetime.now().date())
        elif date_range == 'week':
            from datetime import timedelta
            week_ago = datetime.now().date() - timedelta(days=7)
            queryset = queryset.filter(date_created__date__gte=week_ago)
        elif date_range == 'month':
            from datetime import timedelta
            month_ago = datetime.now().date() - timedelta(days=30)
            queryset = queryset.filter(date_created__date__gte=month_ago)
        
        # Weekday filter (1=Sunday, 2=Monday, ..., 7=Saturday in Django)
        weekday = self.request.GET.get('weekday', '').strip()
        if weekday and weekday.isdigit():
            weekday_num = int(weekday)
            if 1 <= weekday_num <= 7:
                queryset = queryset.filter(date_created__week_day=weekday_num)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass filter parameters to template
        context['current_search'] = self.request.GET.get('search', '')
        context['current_date'] = self.request.GET.get('date', '')
        context['current_date_range'] = self.request.GET.get('date_range', '')
        context['current_weekday'] = self.request.GET.get('weekday', '')
        
        # Count total entries and filtered entries
        context['total_entries'] = Entry.objects.count()
        context['filtered_count'] = self.get_queryset().count()
        
        # Check if any filters are active
        context['has_filters'] = any([
            context['current_search'],
            context['current_date'],
            context['current_date_range'],
            context['current_weekday'],
        ])
        
        return context


class EntryDetailView(LockedView, DetailView):
    model = Entry


class EntryCreateView(LockedView, SuccessMessageMixin, CreateView):
    model = Entry
    fields = ["title", "content"]
    success_url = reverse_lazy("entry-list")
    success_message = "Your new entry was created!"


class EntryUpdateView(LockedView, SuccessMessageMixin, UpdateView):
    model = Entry
    fields = ["title", "content"]
    success_message = "Your entry was updated!"

    def get_success_url(self):
        return reverse_lazy("entry-detail", kwargs={"pk": self.object.pk})


class EntryDeleteView(LockedView, SuccessMessageMixin, DeleteView):
    model = Entry
    success_url = reverse_lazy("entry-list")
    success_message = "Your entry was deleted!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


class CustomLoginView(auth_views.LoginView):
    template_name = 'entries/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('entry-list')
