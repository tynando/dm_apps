from django.test import TestCase, tag
from django.urls import reverse_lazy
from django.utils.translation import activate
from django.contrib.auth.models import User

from whalesdb import views, models, forms

from django.contrib.auth.models import User


class CommonTest(TestCase):
    test_url = None
    test_expected_template = None
    login_url_base = '/accounts/login_required/?next='
    login_url_en = login_url_base + "/en/"
    login_url_fr = login_url_base + "/fr/"

    # All views should at a minimum have a title field
    def context_fields(self, response):
        self.assertIn("title", response.context)


class TestIndexView(CommonTest):

    def setUp(self):
        super().setUp()

        self.test_url = reverse_lazy('whalesdb:index')
        self.test_expected_template = 'whalesdb/index.html'

    # Users should be able to view the whales index page which corresponds to the whalesdb/index.html template
    @tag('index_view', 'response', 'access')
    def test_index_view_en(self):
        activate('en')

        response = self.client.get(self.test_url)

        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(self.test_expected_template)

    # Users should be able to view the whales index page corresponding to the whalesdb/index.html template, in French
    @tag('index_view', 'response', 'access')
    def test_index_view_fr(self):
        activate('fr')

        response = self.client.get(self.test_url)

        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(self.test_expected_template)

    # The index view should return a context to be used on the index.html template
    # this should consist of a "Sections" dictionary containing sub-sections
    @tag('index_view', 'context')
    def test_index_view_context(self):
        activate('en')

        response = self.client.get(self.test_url)

        # expect to see section in the context
        self.assertIn("section", response.context)

        # expect to see an 'entry form' section as the first element of section
        entry_forms = response.context['section'][0]

        self.assertEquals('Entry Forms', entry_forms['title'])

        # Expected there to be a station list object
        stn_list = entry_forms['forms'][0]
        self.assertEquals('Station List', stn_list['title'])

        # Expected there to be a project list object
        prj_list = entry_forms['forms'][1]
        self.assertEquals('Project List', prj_list['title'])

        # Expected there to be a project list object
        mor_list = entry_forms['forms'][2]
        self.assertEquals('Mooring Setup List', mor_list['title'])


class ListTest(CommonTest):

    def setUp(self):
        super().setUp()

        self.test_expected_template = 'whalesdb/whale_filter.html'

    # Users doesn't have to be logged in to view a list
    def list_en(self):
        activate('en')

        response = self.client.get(self.test_url)

        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(self.test_expected_template)

    # Users doesn't have to be logged in to view a list
    def list_fr(self):
        activate('fr')

        response = self.client.get(self.test_url)

        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(self.test_expected_template)

    # List context should return:
    #   - a title to display in the html template
    #   - a list of fields to display
    #   - a url to use for the create button
    #   - a url to use for the detail links
    def list_context_fields(self):
        activate('en')

        response = self.client.get(self.test_url)

        super().context_fields(response)
        self.assertIn("fields", response.context)
        self.assertIn("create_url", response.context)
        self.assertIn("details_url", response.context)

        return response


class TestListStation(ListTest):

    def setUp(self):
        super().setUp()

        self.test_url = reverse_lazy('whalesdb:list_stn')

    # User should be able to view lists without login required
    @tag('stn_list', 'response', 'access')
    def test_stn_list_en(self):
        super().list_en()

    # User should be able to view lists without login required
    @tag('stn_list', 'response', 'access')
    def test_stn_list_fr(self):
        super().list_fr()

    # make sure project list context returns expected context objects
    @tag('stn_list', 'response', 'context')
    def test_stn_list_context_fields(self):
        response = super().list_context_fields()

        self.assertEqual("whalesdb:create_stn", response.context['create_url'])
        self.assertEqual("whalesdb:details_stn", response.context['details_url'])


class TestListProject(ListTest):

    def setUp(self):
        super().setUp()

        self.test_url = reverse_lazy('whalesdb:list_prj')

    # User should be able to view lists without login required
    @tag('prj_list', 'response', 'access')
    def test_prj_list_en(self):
        super().list_en()

    # User should be able to view lists without login required
    @tag('prj_list', 'response', 'access')
    def test_prj_list_fr(self):
        super().list_fr()

    # make sure project list context returns expected context objects
    @tag('prj_list', 'response', 'context')
    def test_prj_list_context_fields(self):
        response = super().list_context_fields()

        self.assertEqual("whalesdb:create_prj", response.context['create_url'])
        self.assertEqual("whalesdb:details_prj", response.context['details_url'])


class TestListMooring(ListTest):

    def setUp(self):
        super().setUp()

        self.test_url = reverse_lazy('whalesdb:list_mor')

    # User should be able to view lists without login required
    @tag('mor_list', 'response', 'access')
    def test_mor_list_en(self):
        super().list_en()

    # User should be able to view lists without login required
    @tag('mor_list', 'response', 'access')
    def test_mor_list_fr(self):
        super().list_fr()

    # make sure project list context returns expected context objects
    @tag('mor_list', 'response', 'context')
    def test_mor_list_context_fields(self):
        response = super().list_context_fields()

        self.assertEqual("whalesdb:create_mor", response.context['create_url'])
        self.assertEqual("whalesdb:details_mor", response.context['details_url'])


class CreateTest(CommonTest):

    expected_form = None
    expected_view = None
    expected_success_url = None
    data = None

    def setUp(self):
        super().setUp()

        # CreateViews intended to be used from a views.ListCommon should use the _entry_form.html template
        self.test_expected_template = 'whalesdb/_entry_form.html'

    # use when a user needs to be logged in.
    def login(self):
        test_password = "test1234"
        user = User.objects.create_user(username="Regular", first_name="Joe", last_name="Average",
                                                     email="Average.Joe@dfo-mpo.gc.ca", password=test_password)
        user.save()

        self.client.login(username=user.username, password=test_password)

        return user

    # Users must be logged in to create new objects
    # user not logged in, should get 302 redirect to login page.
    def create_login_redirect_en(self):
        activate('en')

        response = self.client.get(self.test_url)

        self.assertEquals(302, response.status_code)
        self.assertTemplateUsed(self.test_expected_template)

    # user not logged in, should get 302 redirect to login page.
    def create_login_redirect_fr(self):
        activate('fr')

        response = self.client.get(self.test_url)

        # user not logged in, should get 302 redirect to login page.
        self.assertEquals(302, response.status_code)
        self.assertTemplateUsed(self.test_expected_template)

    # If a user is logged in and not 'whalesdb_access' they should not be redirected
    def create_logged_in_not_access(self):
        activate('en')

        regular_user = self.login()

        self.assertEqual(int(self.client.session['_auth_user_id']), regular_user.pk)

        response = self.client.get(self.test_url)
        self.assertEquals(200, response.status_code)

    # If a user is logged in and has 'whalesdb_access' they should not be redirected
    def create_logged_in_has_access(self):
        pass

    # check that the creation view is using the correct form
    def create_form(self):
        activate("en")

        view = self.expected_view

        self.assertEquals(self.expected_form, view.form_class)

    # All CommonCreate views should at a minimum have a title.
    # This will return the response for other create view tests to run further tests on context if required
    def create_context_fields(self):
        activate('en')

        self.login()
        response = self.client.get(self.test_url)

        super().context_fields(response)

        return response

    # test that upon a successful form the view redirects to the expected success url
    #   - Requires: self.test_url
    #   - Requires: self.data
    #   - Requires: self.expected_success_url
    def successful_url(self):
        activate('en')

        self.login()
        response = self.client.post(self.test_url, self.data)

        self.assertRedirects(response=response, expected_url=self.expected_success_url)


class TestCreateProject(CreateTest):
    data = {
        "prj_name": 'PRJ_001',
        "prj_description": "Some project description here",
        "prj_url": "https//noneOfYourBusiness.com"
    }

    def setUp(self):
        super().setUp()

        self.test_url = reverse_lazy('whalesdb:create_prj')

        # Since this is intended to be used as a pop-out form, the html file should start with an underscore
        self.test_expected_template = 'whalesdb/_entry_form.html'

        self.expected_view = views.CreatePrj

        self.expected_form = forms.PrjForm

        self.expected_success_url = reverse_lazy("whalesdb:list_prj")

    # Users must be logged in to create new stations
    @tag('create_prj', 'response', 'access')
    def test_prj_create_en(self):
        super().create_login_redirect_en()

    # Users must be logged in to create new stations
    @tag('create_prj', 'response', 'access')
    def test_prj_create_fr(self):
        super().create_logged_in_not_access()

    # Logged in user should get to the _entry_form.html template
    @tag('create_prj', 'response', 'access')
    def test_prj_create_en(self):
        super().create_logged_in_not_access()

    # Test that projects is using the project form
    @tag('create_prj', 'form')
    def test_prj_create_form(self):
        super().create_form()

    # test that the context is returning the required context fields
    # at a minimum this should include a title field
    # Each view might require specific context fields
    @tag('create_prj', 'context')
    def test_create_prj_context_fields(self):
        super().create_context_fields()

    # test that given some valid data the view will redirect to the list
    @tag('create_prj', 'redirect')
    def test_create_prj_successful_url(self):
        super().successful_url()


class TestCreateStation(CreateTest):
    data = {
            "stn_name": "STN_001",
            "stn_code": "STN",
            "stn_revision": "1",
            "stn_planned_lat": "25",
            "stn_planned_lon": "50",
            "stn_planned_depth": "10",
            "stn_notes": "Some Notes"
        }

    def setUp(self):
        super().setUp()

        self.test_url = reverse_lazy('whalesdb:create_stn')

        # Since this is intended to be used as a pop-out form, the html file should start with an underscore
        self.test_expected_template = 'whalesdb/_entry_form.html'

        self.expected_view = views.CreateStn

        self.expected_form = forms.StnForm

        self.expected_success_url = reverse_lazy("whalesdb:list_stn")

    # Users must be logged in to create new stations
    @tag('create_stn', 'response', 'access')
    def test_stn_create_login_redirect_en(self):
        super().create_login_redirect_en()

    # Users must be logged in to create new stations
    @tag('create_stn', 'response', 'access')
    def test_stn_create_login_redirect_fr(self):
        super().create_login_redirect_fr()

    # Logged in user should get to the _entry_form.html template
    @tag('create_stn', 'response', 'access')
    def test_stn_create_en(self):
        super().create_logged_in_not_access()

    # Test that using the project form
    @tag('create_stn', 'form')
    def test_stn_create_form(self):
        super().create_form()

    # test that the context is returning the required context fields
    # at a minimum this should include a title field
    # Each view might require specific context fields
    @tag('create_stn', 'context')
    def test_create_stn_context_fields(self):
        super().create_context_fields()

    # test that given some valid data the view will redirect to the list
    @tag('create_stn', 'redirect')
    def test_create_stn_successful_url(self):
        super().successful_url()


class TestCreateMooring(CreateTest):
    data = {
        "mor_name": "MOR_001",
        "mor_max_depth": "10",
        "mor_link_setup_image": "https://somelink.com/images/img001.png",
        "mor_additional_equipment": "None",
        "mor_general_moor_description": "This is a mooring description",
        "more_notes": "Notes",
    }

    def setUp(self):
        super().setUp()

        self.test_url = reverse_lazy('whalesdb:create_mor')

        # Since this is intended to be used as a pop-out form, the html file should start with an underscore
        self.test_expected_template = 'whalesdb/_entry_form.html'

        self.expected_view = views.CreateMor
        self.expected_form = forms.MorForm
        self.expected_success_url = reverse_lazy("whalesdb:list_mor")

    # Users must be logged in to create new stations
    @tag('create_mor', 'response', 'access')
    def test_mor_create_login_redirect_en(self):
        super().create_login_redirect_en()

    # Users must be logged in to create new stations
    @tag('create_mor', 'response', 'access')
    def test_mor_create_login_redirect_fr(self):
        super().create_login_redirect_fr()

    # Logged in user should get to the _entry_form.html template
    @tag('create_mor', 'response', 'access')
    def test_mor_create_en(self):
        super().create_logged_in_not_access()

    # Test is using the project form
    @tag('create_mor', 'form')
    def test_mor_create_form(self):
        super().create_form()

    # test that the context is returning the required context fields
    # at a minimum this should include a title field
    # Each view might require specific context fields
    @tag('create_mor', 'context')
    def test_create_mor_context_fields(self):
        super().create_context_fields()

    # test that given some valid data the view will redirect to the list
    @tag('create_mor', 'redirect')
    def test_create_mor_successful_url(self):
        super().successful_url()


class TestDetailsStation(CommonTest):
    station_dic = None

    def createStn(self):
        if self.station_dic:
            return self.station_dic

        self.station_dic = {}

        stn_1 = models.StnStation(stn_name='Station 1', stn_code='ST1', stn_revision=1, stn_planned_lat=52,
                                  stn_planned_lon=25, stn_planned_depth=1)
        stn_1.save()

        self.station_dic['stn_1'] = stn_1

        return self.station_dic

    def setUp(self):
        super().setUp()

        stn_dic = self.createStn()

        self.test_url = reverse_lazy('whalesdb:details_stn', args=(stn_dic['stn_1'].pk,))
        self.test_expected_template = 'whalesdb/station_details.html'

    # Station Details are visible to all
    @tag('details_stn', 'response', 'access')
    def test_details_stn_en(self):
        activate('en')

        response = self.client.get(self.test_url)

        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(self.test_expected_template)

    # Station Details are visible to all
    @tag('details_stn', 'response', 'access')
    def test_details_stn_fr(self):
        activate('fr')

        response = self.client.get(self.test_url)

        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(self.test_expected_template)


class TestDetailsMooring(CommonTest):
    mooring_dic = None

    def createMor(self):
        if self.mooring_dic:
            return self.mooring_dic

        self.mooring_dic = {}

        mor_1 = models.MorMooringSetup(mor_name="MOR001", mor_max_depth=100, mor_link_setup_image="https://somelink.com")
        mor_1.save()

        self.mooring_dic['mor_1'] = mor_1

        return self.mooring_dic

    def setUp(self):
        super().setUp()

        mor_dic = self.createMor()

        self.test_url = reverse_lazy('whalesdb:details_mor', args=(mor_dic['mor_1'].pk,))
        self.test_expected_template = 'whalesdb/mormooringsetup_detail.html'

    # Station Details are visible to all
    @tag('details_mor', 'response', 'access')
    def test_details_mor_en(self):
        activate('en')

        response = self.client.get(self.test_url)

        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(self.test_expected_template)

    # Station Details are visible to all
    @tag('details_mor', 'response', 'access')
    def test_details_mor_fr(self):
        activate('fr')

        response = self.client.get(self.test_url)

        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(self.test_expected_template)

    # Test that the context contains the proper fields
    @tag('details_mor', 'context')
    def test_context_fields_mor(self):
        activate('fr')

        response = self.client.get(self.test_url)

        super().context_fields(response)