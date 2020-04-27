from django.utils.translation import gettext as _

from lib.functions.custom_functions import listrify
from shared_models import models as shared_models
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.db.models import Count, TextField
from django.db.models.functions import Concat
from django.http import HttpResponseRedirect, HttpResponse, Http404
# from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView, TemplateView, FormView
from django_filters.views import FilterView
from . import models
from . import forms
from . import filters
from . import reports

# for Dashboard 1 test
from django.http import JsonResponse
from django.shortcuts import render
from vault.models import Outing
from django.core import serializers


def dashboard_with_pivot(request):
    return render(request, 'vault/dashboard_with_pivot.html', {})


def pivot_data(request):
    dataset = Outing.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)


# end Dashboard 1 test section

class VaultAccessRequired(LoginRequiredMixin, UserPassesTestMixin):
    login_url = '/accounts/login_required/'

    def test_func(self):
        return True

    def dispatch(self, request, *args, **kwargs):
        user_test_result = self.get_test_func()()
        if not user_test_result and self.request.user.is_authenticated:
            return HttpResponseRedirect('/accounts/denied/')
        return super().dispatch(request, *args, **kwargs)

def in_vault_admin_group(user):
    if "vault_admin" in [g.name for g in user.groups.all()]:
        return True

class VaultAdminAccessRequired(LoginRequiredMixin, UserPassesTestMixin):
    login_url = '/accounts/login_required/'

    def test_func(self):
        return in_vault_admin_group(self.request.user)

    def dispatch(self, request, *args, **kwargs):
        user_test_result = self.get_test_func()()
        if not user_test_result and self.request.user.is_authenticated:
            return HttpResponseRedirect('/accounts/denied/')
        return super().dispatch(request, *args, **kwargs)


def in_vault_edit_group(user):
    """this group includes the admin group so there is no need to add an admin to this group"""
    if user:
        if in_vault_admin_group(user) or user.groups.filter(name='vault_edit').count() != 0:
            return True

class VaultEditRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        return in_vault_edit_group(self.request.user)

    def dispatch(self, request, *args, **kwargs):
        user_test_result = self.get_test_func()()
        if not user_test_result and self.request.user.is_authenticated:
            return HttpResponseRedirect('/accounts/denied/')
        return super().dispatch(request, *args, **kwargs)



@login_required(login_url='/accounts/login_required/')
def index(request):
    return render(request, 'vault/index.html')


# #
# # # SPECIES #
# # ###########
# #
#

class SpeciesListView(VaultAccessRequired, FilterView):
    template_name = "vault/species_list.html"
    filterset_class = filters.SpeciesFilter
    queryset = models.Species.objects.annotate(
        search_term=Concat('code', 'english_name', 'french_name', 'latin_name', 'id', output_field=TextField()))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["my_object"] = models.Species.objects.first()
        context["field_list"] = [
            'id',
            'code',
            'french_name',
            'english_name',
            'latin_name',
            'vor_code',
            'quebec_code',
            'maritimes_code',
            'aphia_id',
        ]
        return context


#
class SpeciesDetailView(VaultAccessRequired, DetailView):
    model = models.Species

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["field_list"] = [
            'id',
            'code',
            'english_name',
            'french_name',
            'latin_name',
            'vor_code',
            'quebec_code',
            'aphia_id',
        ]
        return context


#
class SpeciesUpdateView(VaultEditRequiredMixin, UpdateView):
    model = models.Species
    form_class = forms.SpeciesForm

    def form_valid(self, form):
        my_object = form.save()
        messages.success(self.request, _(f"Species record successfully updated for : {my_object}"))
        return super().form_valid(form)


class SpeciesCreateView(VaultEditRequiredMixin, CreateView):
    model = models.Species
    form_class = forms.SpeciesForm

    def form_valid(self, form):
        my_object = form.save()
        messages.success(self.request, _(f"Species record successfully created for : {my_object}"))
        return super().form_valid(form)


class SpeciesDeleteView(VaultEditRequiredMixin, DeleteView):
    model = models.Species
    permission_required = "__all__"
    success_url = reverse_lazy('vault:species_list')
    success_message = 'The species was successfully deleted!'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


#
# #
# # # OBSERVATIONPLATFORM #
# # ###########
# #
#
class ObservationPlatformListView(VaultAccessRequired, FilterView):
    template_name = "vault/observationplatform_list.html"
    filterset_class = filters.ObservationPlatformFilter
    queryset = models.ObservationPlatform.objects.annotate(
        search_term=Concat('authority', 'owner', 'make_model', 'name', 'longname', 'id', output_field=TextField()))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["my_object"] = models.ObservationPlatform.objects.first()
        context["field_list"] = [
            'id',
            'observation_platform_type',
            'authority',
            'make_model',
            'owner',
            'name',
            'longname',
            'foldername|folder name'
        ]
        return context


#
class ObservationPlatformDetailView(VaultAccessRequired, DetailView):
    model = models.ObservationPlatform

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["field_list"] = [
            'id',
            'observation_platform_type',
            'authority',
            'make_model',
            'owner',
            'name',
            'longname',
        ]
        return context


#
class ObservationPlatformUpdateView(VaultEditRequiredMixin, UpdateView):
    model = models.ObservationPlatform
    form_class = forms.ObservationPlatformForm

    def form_valid(self, form):
        my_object = form.save()
        messages.success(self.request, _(f"ObservationPlatform record successfully updated for : {my_object}"))
        return super().form_valid(form)


class ObservationPlatformCreateView(VaultEditRequiredMixin, CreateView):
    model = models.ObservationPlatform
    form_class = forms.ObservationPlatformForm

    def form_valid(self, form):
        my_object = form.save()
        messages.success(self.request, _(f"ObservationPlatform record successfully created for : {my_object}"))
        return super().form_valid(form)


class ObservationPlatformDeleteView(VaultEditRequiredMixin, DeleteView):
    model = models.ObservationPlatform
    permission_required = "__all__"
    success_url = reverse_lazy('vault:observationplatform_list')
    success_message = 'The observation plaform was successfully deleted!'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


#
# #
# # # INSTRUMENTS #
# # ###########
# #
#
class InstrumentListView(VaultAccessRequired, FilterView):
    template_name = "vault/instrument_list.html"
    filterset_class = filters.InstrumentFilter
    queryset = models.Instrument.objects.annotate(
        search_term=Concat('id', 'name', 'nom', output_field=TextField()))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["my_object"] = models.Instrument.objects.first()
        context["field_list"] = [
            'id',
            'instrument_type',
            'name',
            'nom',
            # 'metadata',

        ]
        return context


#
class InstrumentDetailView(VaultAccessRequired, DetailView):
    model = models.Instrument

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["field_list"] = [
            'id',
            'name',
            'nom',
            # 'metadata',
            'instrument_type',

        ]
        return context


#
class InstrumentUpdateView(VaultEditRequiredMixin, UpdateView):
    model = models.Instrument
    form_class = forms.InstrumentForm

    def form_valid(self, form):
        my_object = form.save()
        messages.success(self.request, _(f"Instrument record successfully updated for : {my_object}"))
        return super().form_valid(form)


class InstrumentCreateView(VaultEditRequiredMixin, CreateView):
    model = models.Instrument
    form_class = forms.InstrumentForm

    def form_valid(self, form):
        my_object = form.save()
        messages.success(self.request, _(f"Instrument record successfully created for : {my_object}"))
        return super().form_valid(form)


class InstrumentDeleteView(VaultEditRequiredMixin, DeleteView):
    model = models.Instrument
    permission_required = "__all__"
    success_url = reverse_lazy('vault:instrument_list')
    success_message = 'The instrument was successfully deleted!'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


#
# #
# # # OUTINGS #
# # ###########
# #
#
class OutingListView(VaultAccessRequired, FilterView):
    template_name = "vault/outing_list.html"
    filterset_class = filters.OutingFilter
    queryset = models.Outing.objects.annotate(
        search_term=Concat('id', 'region', 'purpose', 'start_date', 'start_time', 'end_time', 'duration', 'identifier_string',
                           'observation_platform_id', output_field=TextField()))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["my_object"] = models.Outing.objects.first()
        context["field_list"] = [
            'id',
            'observation_platform_id',
            'region',
            'purpose',
            'start_date',
            'start_time',
            'end_time',
            'duration',
            'identifier_string',

        ]
        return context


#
class OutingDetailView(VaultAccessRequired, DetailView):
    model = models.Outing

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["field_list"] = [
            'id',
            'observation_platform_id',
            'region',
            'purpose',
            'start_date',
            'start_time',
            'end_time',
            'duration',
            'identifier_string',

        ]
        return context


#
class OutingUpdateView(VaultEditRequiredMixin, UpdateView):
    model = models.Outing
    form_class = forms.OutingForm

    def form_valid(self, form):
        my_object = form.save()
        messages.success(self.request, _(f"Outing record successfully updated for : {my_object}"))
        return super().form_valid(form)


class OutingCreateView(VaultEditRequiredMixin, CreateView):
    model = models.Outing
    form_class = forms.OutingForm

    def form_valid(self, form):
        my_object = form.save()
        messages.success(self.request, _(f"Outing record successfully created for : {my_object}"))
        return super().form_valid(form)


class OutingDeleteView(VaultEditRequiredMixin, DeleteView):
    model = models.Outing
    permission_required = "__all__"
    success_url = reverse_lazy('vault:outing_list')
    success_message = 'The outing was successfully deleted!'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


#
# #
# # # PERSON #
# # ###########
# #
#
class PersonListView(VaultAdminAccessRequired, FilterView):
    template_name = "vault/person_list.html"
    filterset_class = filters.PersonFilter
    queryset = models.Person.objects.annotate(
        search_term=Concat('id', 'first_name', 'last_name', 'organisation', 'email', 'phone', 'roles', output_field=TextField()))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["my_object"] = models.Person.objects.first()
        context["field_list"] = [
            'id',
            'first_name',
            'last_name',
            'organisation',
            'email',
            'phone',
            'roles',

        ]
        return context


class PersonDetailView(VaultAdminAccessRequired, DetailView):
    model = models.Person

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["field_list"] = [
            'id',
            'first_name',
            'last_name',
            'organisation',
            'email',
            'phone',
            'roles',
        ]
        return context


class PersonUpdateView(VaultAdminAccessRequired, UpdateView):
    model = models.Person
    form_class = forms.PersonForm

    def form_valid(self, form):
        my_object = form.save()
        messages.success(self.request, _(f"Person record successfully updated for : {my_object}"))
        return super().form_valid(form)


class PersonCreateView(VaultAdminAccessRequired, CreateView):
    model = models.Person
    form_class = forms.PersonForm

    def form_valid(self, form):
        my_object = form.save()
        messages.success(self.request, _(f"Person record successfully created for : {my_object}"))
        return super().form_valid(form)


class PersonDeleteView(VaultAdminAccessRequired, DeleteView):
    model = models.Person
    permission_required = "__all__"
    success_url = reverse_lazy('vault:person_list')
    success_message = 'The person was successfully deleted!'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


#
# #
# # # OBSERVATION #
# # ###########
# #
#
class ObservationListView(VaultAccessRequired, FilterView):
    template_name = "vault/observation_list.html"
    filterset_class = filters.ObservationFilter
    queryset = models.Observation.objects.annotate(
        search_term=Concat('id', 'outing', 'instrument', 'datetime', 'latitude', 'longitude', 'observer', 'metadata', 'opportunistic',
                           output_field=TextField()))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["my_object"] = models.Observation.objects.first()
        context["field_list"] = [
            'id',
            'outing',
            'instrument',
            'datetime',
            'latitude',
            'longitude',
            'observer',
            'metadata',
            'opportunistic',

        ]
        return context


class ObservationDetailView(VaultAccessRequired, DetailView):
    model = models.Observation

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["field_list"] = [
            'id',
            'outing',
            'instrument',
            'datetime',
            'latitude',
            'longitude',
            'observer',
            'metadata',
            'opportunistic',
        ]
        return context


class ObservationUpdateView(VaultEditRequiredMixin, UpdateView):
    model = models.Observation
    form_class = forms.ObservationForm

    def form_valid(self, form):
        my_object = form.save()
        messages.success(self.request, _(f"Observation record successfully updated for : {my_object}"))
        return super().form_valid(form)


class ObservationCreateView(VaultEditRequiredMixin, CreateView):
    model = models.Observation
    form_class = forms.ObservationForm

    def form_valid(self, form):
        my_object = form.save()
        messages.success(self.request, _(f"Observation record successfully created for : {my_object}"))
        return super().form_valid(form)


class ObservationDeleteView(VaultEditRequiredMixin, DeleteView):
    model = models.Observation
    permission_required = "__all__"
    success_url = reverse_lazy('vault:observation_list')
    success_message = 'The observation was successfully deleted!'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
