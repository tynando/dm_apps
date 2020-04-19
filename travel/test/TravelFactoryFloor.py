import datetime
import factory
from django.utils import timezone
from faker import Faker

from shared_models.test.SharedModelsFactoryFloor import SectionFactory, UserFactory
from .. import models

faker = Faker()


class TripFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Conference
        django_get_or_create = ('name',)

    name = faker.word()
    start_date = factory.lazy_attribute(lambda o: faker.date_time_this_year(tzinfo=timezone.get_current_timezone()))
    end_date = factory.lazy_attribute(lambda o: o.start_date + datetime.timedelta(days=faker.random_int(1, 365)))


class IndividualTripRequestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.TripRequest
        # django_get_or_create = ('trip','user','is_group_request')

    trip = factory.SubFactory(TripFactory)
    section = factory.SubFactory(SectionFactory)
    user = factory.SubFactory(UserFactory)
    is_group_request = False


class ParentTripRequestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.TripRequest
        django_get_or_create = ('trip', 'user', 'is_group_request')

    trip = factory.SubFactory(TripFactory)
    section = factory.SubFactory(SectionFactory)
    user = factory.SubFactory(UserFactory)
    is_group_request = True


class ChildTripRequestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.TripRequest

    parent_request = factory.SubFactory(ParentTripRequestFactory)
    user = factory.SubFactory(UserFactory)
    is_group_request = False


class ReviewerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Reviewer
        django_get_or_create = ('trip_request', 'user', 'role')

    trip_request = factory.SubFactory(IndividualTripRequestFactory)
    user = factory.SubFactory(UserFactory)
    role = factory.lazy_attribute(lambda o: models.ReviewerRole.objects.all()[faker.random_int(0, models.ReviewerRole.objects.count() - 1)])
    status = factory.lazy_attribute(
        lambda o: models.Status.objects.filter(used_for=1)[faker.random_int(0, models.Status.objects.filter(used_for=1).count() - 1)])
    status_date = factory.lazy_attribute(lambda o: o.trip_request.start_date + datetime.timedelta(days=faker.random_int(1, 365)))


class FileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.File

    trip_request = factory.SubFactory(IndividualTripRequestFactory)
    name = factory.lazy_attribute(lambda o: faker.word())


class TripRequestCostDayXRateFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.TripRequestCost

    trip_request = factory.SubFactory(IndividualTripRequestFactory)
    cost = factory.lazy_attribute(lambda o: models.Cost.objects.all()[faker.random_int(0, models.Cost.objects.count() - 1)])

    rate_cad = factory.lazy_attribute(lambda o: faker.pyfloat(positive=True))
    number_of_days = factory.lazy_attribute(lambda o: faker.random_int(1, 10))


class TripRequestCostTotalFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.TripRequestCost

    trip_request = factory.SubFactory(IndividualTripRequestFactory)
    cost = factory.lazy_attribute(lambda o: models.Cost.objects.all()[faker.random_int(0, models.Cost.objects.count() - 1)])
    amount_cad = factory.lazy_attribute(lambda o: faker.pyfloat(positive=True))