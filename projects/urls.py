from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'projects'

urlpatterns = [
    path('close/', views.CloserTemplateView.as_view(), name="close_me"),
    path('', views.IndexTemplateView.as_view(), name="index"),

    # PROJECTS #
    ############
    path('my-list/', views.MyProjectListView.as_view(), name="my_project_list"),
    path('my-section/', views.MySectionListView.as_view(), name="my_section_list"),
    path('projects/', views.ProjectListView.as_view(), name="project_list"),
    path('projects/new/', views.ProjectCreateView.as_view(), name="project_new"),
    path('projects/<int:pk>/view', views.ProjectDetailView.as_view(), name="project_detail"),
    path('projects/<int:pk>/print', views.ProjectPrintDetailView.as_view(), name="project_print"),
    path('projects/<int:pk>/edit', views.ProjectUpdateView.as_view(), name="project_edit"),
    path('projects/<int:pk>/delete', views.ProjectDeleteView.as_view(), name="project_delete"),
    path('projects/<int:pk>/submit', views.ProjectSubmitUpdateView.as_view(), name="project_submit"),

    # STAFF #
    #########
    path('project/<int:project>/staff/new/', views.StaffCreateView.as_view(), name="staff_new"),
    path('staff/<int:pk>/edit/', views.StaffUpdateView.as_view(), name="staff_edit"),
    path('staff/<int:pk>/delete/', views.staff_delete, name="staff_delete"),
    path('staff/<int:pk>/overtime-calculator/', views.OverTimeCalculatorTemplateView.as_view(), name="ot_calc"),

    # USER #
    ########
    path('user/new/', views.UserCreateView.as_view(), name="user_new"),

    # Collaborator #
    ################
    path('project/<int:project>/collaborator/new/', views.CollaboratorCreateView.as_view(), name="collab_new"),
    path('collaborator/<int:pk>/edit/', views.CollaboratorUpdateView.as_view(), name="collab_edit"),
    path('collaborator/<int:pk>/delete/', views.collaborator_delete, name="collab_delete"),

    # Collaborative Agreements #
    ############################
    path('project/<int:project>/agreement/new/', views.AgreementCreateView.as_view(), name="agreement_new"),
    path('agreement/<int:pk>/edit/', views.AgreementUpdateView.as_view(), name="agreement_edit"),
    path('agreement/<int:pk>/delete/', views.agreement_delete, name="agreement_delete"),

    # O&M COST #
    ############
    path('project/<int:project>/om-cost/new/', views.OMCostCreateView.as_view(), name="om_new"),
    path('om-cost/<int:pk>/edit/', views.OMCostUpdateView.as_view(), name="om_edit"),
    path('om-cost/<int:pk>/delete/', views.om_cost_delete, name="om_delete"),
    path('om-cost/<int:project>/clear-empty/', views.om_cost_clear, name="om_clear"),
    path('om-cost/<int:project>/populate-all/', views.om_cost_populate, name="om_populate"),

    # CAPITAL COST #
    ################
    path('project/<int:project>/capital-cost/new/', views.CapitalCostCreateView.as_view(), name="capital_new"),
    path('capital-cost/<int:pk>/edit/', views.CapitalCostUpdateView.as_view(), name="capital_edit"),
    path('capital-cost/<int:pk>/delete/', views.capital_cost_delete, name="capital_delete"),

    # G&C COST #
    ############
    path('project/<int:project>/gc-cost/new/', views.GCCostCreateView.as_view(), name="gc_new"),
    path('gc-cost/<int:pk>/edit/', views.GCCostUpdateView.as_view(), name="gc_edit"),
    path('gc-cost/<int:pk>/delete/', views.gc_cost_delete, name="gc_delete"),


    # Reports #
    ###########
    path('reports/search/', views.ReportSearchFormView.as_view(), name="report_search"),
    path('reports/master-spreadsheet/fiscal-year/<int:fiscal_year>/sections/<str:sections>/', views.master_spreadsheet, name="report_master"),
    path('reports/section-head-spreadsheet/fiscal-year/<int:fiscal_year>/user/<int:user>', views.master_spreadsheet, name="report_sh"),
    path('reports/pdf-printout/fiscal-year/<int:fiscal_year>', views.PDFProjectPrintoutReport.as_view(), name="pdf_printout"),
    path('reports/workplan-summary/fiscal-year/<int:fiscal_year>', views.workplan_summary, name="workplan_summary"),

    # SHARED #
    ##########
    path('toggle-funding-source/<str:type>/<int:pk>/', views.toggle_source, name="toggle_source"),
    path('toggle-section-head-approved/<int:project>/', views.toggle_project_approval, name="toggle_project_approval"),


]
