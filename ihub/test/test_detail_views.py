from django.utils import timezone
from django.utils.translation import activate
from django.urls import reverse_lazy
from django.test import tag
from django.views.generic import DetailView, UpdateView
from easy_pdf.views import PDFTemplateView

from ihub.test import FactoryFloor
from ihub.test.common_tests import CommonIHubTest as CommonTest
from shared_models.views import CommonDetailView
from .. import views


class TestPersonDetailView(CommonTest):
    def setUp(self):
        super().setUp()
        self.instance = FactoryFloor.PersonFactory()
        self.test_url = reverse_lazy('ihub:person_detail', args=[self.instance.pk, ])
        self.expected_template = 'ihub/person_detail.html'
        self.user = self.get_and_login_user()

    @tag("Person", "person_detail", "view")
    def test_view_class(self):
        self.assert_inheritance(views.PersonDetailView, CommonDetailView)

    @tag("Person", "person_detail", "access")
    def test_view(self):
        self.assert_not_broken(self.test_url)
        self.assert_non_public_view(test_url=self.test_url, expected_template=self.expected_template, user=self.user)

    @tag("Person", "person_detail", "context")
    def test_context(self):
        context_vars = [
            "field_list",
        ]
        self.assert_presence_of_context_vars(self.test_url, context_vars, user=self.user)


class TestOrganizationDetailView(CommonTest):
    def setUp(self):
        super().setUp()
        self.instance = FactoryFloor.OrganizationFactory()
        self.test_url = reverse_lazy('ihub:org_detail', args=[self.instance.pk, ])
        self.expected_template = 'ihub/organization_detail.html'
        self.user = self.get_and_login_user()

    @tag("Organization", "org_detail", "view")
    def test_view_class(self):
        self.assert_inheritance(views.OrganizationDetailView, CommonDetailView)

    @tag("Organization", "org_detail", "access")
    def test_view(self):
        self.assert_not_broken(self.test_url)
        self.assert_non_public_view(test_url=self.test_url, expected_template=self.expected_template, user=self.user)

    @tag("Organization", "org_detail", "context")
    def test_context(self):
        context_vars = [
            "field_list",
        ]
        self.assert_presence_of_context_vars(self.test_url, context_vars, user=self.user)


class TestEntryDetailView(CommonTest):
    def setUp(self):
        super().setUp()
        self.instance = FactoryFloor.EntryFactory()
        self.test_url = reverse_lazy('ihub:entry_detail', args=[self.instance.pk, ])
        self.expected_template = 'ihub/entry_detail.html'
        self.user = self.get_and_login_user()

    @tag("Entry", "entry_detail", "view")
    def test_view_class(self):
        self.assert_inheritance(views.EntryDetailView, CommonDetailView)

    @tag("Entry", "entry_detail", "access")
    def test_view(self):
        self.assert_not_broken(self.test_url)
        self.assert_non_public_view(test_url=self.test_url, expected_template=self.expected_template, user=self.user)

    @tag("Entry", "entry_detail", "context")
    def test_context(self):
        context_vars = [
            "field_list",
            "field_list_1",
        ]
        self.assert_presence_of_context_vars(self.test_url, context_vars, user=self.user)
