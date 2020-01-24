from django.conf import settings
from django.core.mail import send_mail
from django.db import IntegrityError
from django.utils import timezone

from . import models
from . import emails


def get_reviewers(trip_request):
    # assuming there is a section, assign amelie and section management
    if trip_request.section:
        # if in gulf region, add Amelie as a reviewer
        if trip_request.section.division.branch.region_id == 1:
            try:
                models.Reviewer.objects.create(trip_request=trip_request, user_id=385, role_id=1, )
            except IntegrityError:
                print("not adding amelie")

        # try adding section head, division manager and rds
        try:
            models.Reviewer.objects.create(trip_request=trip_request, user=trip_request.section.head, role_id=2, )
        except (IntegrityError, AttributeError):
            print("not adding section head")
        try:
            models.Reviewer.objects.create(trip_request=trip_request, user=trip_request.section.division.head, role_id=2, )
        except (IntegrityError, AttributeError):
            print("not adding division manager")
        try:
            models.Reviewer.objects.create(trip_request=trip_request, user=trip_request.section.division.branch.head, role_id=2, )
        except (IntegrityError, AttributeError):
            print("not adding RDS")

    # should the ADMs office be invovled?
    if trip_request.conference:
        if trip_request.conference.is_adm_approval_required:
            # add the ADMs office staff
            # try:
            #     models.Reviewer.objects.create(trip_request=trip_request, user_id=749, role_id=3, )  # Kim Cotton
            # except IntegrityError:
            #     print("not adding NCR reviewer")
            # try:
            #     models.Reviewer.objects.create(trip_request=trip_request, user_id=736, role_id=4, )  # Andy White
            # except IntegrityError:
            #     print("not adding NCR recommender")
            # try:
            #     models.Reviewer.objects.create(trip_request=trip_request, user_id=758, role_id=4, )  # Stephen Virc
            # except IntegrityError:
            #     print("not adding NCR recommender")
            # try:
            #     models.Reviewer.objects.create(trip_request=trip_request, user_id=740, role_id=4, )  # Wayne Moore
            # except IntegrityError:
            #     print("not adding NCR recommender")
            try:
                models.Reviewer.objects.create(trip_request=trip_request, user_id=626, role_id=5, )  # Arran McPherson
            except IntegrityError:
                print("not adding NCR ADM")

    # finally, we always need to add the RDG
    try:
        models.Reviewer.objects.create(trip_request=trip_request, user=trip_request.section.division.branch.region.head, role_id=6, )
    except (IntegrityError, AttributeError):
        print("not adding RDG")

    trip_request.save()


def start_review_process(trip_request):
    """this should be used when a project is submitted. It will change over all reviewers' statuses to Pending"""
    # focus only on reviewers that are status = Not Submitted
    for reviewer in trip_request.reviewers.all():
        # set everyone to being queued
        reviewer.status_id = 20
        reviewer.status_date = None
        reviewer.save()


def end_review_process(trip_request):
    """this should be used when a project is unsubmitted. It will change over all reviewers' statuses to Pending"""
    # focus only on reviewers that are status = Not Submitted
    for reviewer in trip_request.reviewers.all():
        reviewer.status_id = 4
        reviewer.status_date = None
        reviewer.comments = None
        reviewer.save()


def set_request_status(trip_request):
    """
    IF POSSIBLE, THIS SHOULD ONLY BE CALLED BY THE approval_seeker() function.
    This will look at the reviewers and decide on  what the project status should be. Will return False if trip_request is denied or if trip_request is not submitted
    """

    # first order of business, if the trip_request is status "changes requested' do not continue
    if trip_request.status_id == 16:
        return False

    # Next: if the trip_request is unsubmitted, it is in 'draft' status
    elif not trip_request.submitted:
        trip_request.status_id = 8
        # don't stick around any longer. save the trip_request and leave exit the function
        trip_request.save()
        return False

    else:
        # if someone denied it at any point, the trip_request is 'denied' and all subsequent reviewers are set to "cancelled"
        is_denied = False
        for reviewer in trip_request.reviewers.all():
            # if reviewer status is denied, set the is_denied var to true
            if reviewer.status_id == 3:
                is_denied = True
            # if is_denied, all subsequent reviewer statuses should be set to "cancelled"
            if is_denied:
                reviewer.status_id = 5
                reviewer.save()
        if is_denied:
            trip_request.status_id = 10
            trip_request.save()
            # send an email to the trip_request owner
            my_email = emails.StatusUpdateEmail(trip_request)
            # # send the email object
            if settings.PRODUCTION_SERVER:
                send_mail(message='', subject=my_email.subject, html_message=my_email.message, from_email=my_email.from_email,
                          recipient_list=my_email.to_list, fail_silently=False, )
            else:
                print(my_email)

            # don't stick around any longer. save the trip_request and leave exit the function
            return False

        # The trip_request should be approved if everyone has approved it. HOWEVER, some reviewers might have been skipped
        # The total number of reviewers should equal the number of reviewer who approved [id=2] and / or were skipped [id=21].
        elif trip_request.reviewers.all().count() == trip_request.reviewers.filter(status_id__in=[2, 21]).count():
            trip_request.status_id = 11
            trip_request.save()
            # send an email to the trip_request owner
            my_email = emails.StatusUpdateEmail(trip_request)
            # # send the email object
            if settings.PRODUCTION_SERVER:
                send_mail(message='', subject=my_email.subject, html_message=my_email.message, from_email=my_email.from_email,
                          recipient_list=my_email.to_list, fail_silently=False, )
            else:
                print(my_email)
            # don't stick around any longer. save the trip_request and leave exit the function
            return False
        else:
            for reviewer in trip_request.reviewers.all():
                # if a reviewer's status is 'pending', we are waiting on them and the project status should be set accordingly.
                if reviewer.status_id == 1:
                    # if role is 'reviewer'
                    if reviewer.role_id == 1:
                        trip_request.status_id = 17
                    # if role is 'recommender'
                    elif reviewer.role_id == 2:
                        trip_request.status_id = 12
                    # if role is 'ncr reviewer'
                    elif reviewer.role_id == 3:
                        trip_request.status_id = 18
                    # if role is 'ncr recommender'
                    elif reviewer.role_id == 4:
                        trip_request.status_id = 19
                    # if role is 'adm'
                    elif reviewer.role_id == 5:
                        trip_request.status_id = 14
                    # if role is 'rdg'
                    elif reviewer.role_id == 6:
                        trip_request.status_id = 15

    trip_request.save()
    return True


def approval_seeker(trip_request):
    """
    This method is meant to seek approvals via email + set reveiwer statuses.
    It will also set the trip_request status vis a vis set_request_status()

    """

    # start by setting the trip_request status... if the trip_request is "denied" OR "draft" or "approved", do not continue
    if set_request_status(trip_request):
        next_reviewer = None
        my_email = None
        for reviewer in trip_request.reviewers.all():
            # if the reviewer's status is set to 'queued', they will be our next selection
            # we should then exit the loop and set the next_reviewer var

            # if this is a resubmission, there might still be a reviewer whose status is 'pending'. This should be the reviewer
            if reviewer.status_id == 20 or reviewer.status_id == 1:
                next_reviewer = reviewer
                break

        # if there is a next reviewer, set their status to pending
        if next_reviewer:
            next_reviewer.status_id = 1
            next_reviewer.status_date = timezone.now()
            next_reviewer.save()

            # now, depending on the role of this reviewer, perhaps we want to send an email.
            # if they are a recommender, rev...
            if next_reviewer.role_id in [1, 2, 3, 4, ]:  # essentially, just not the RDG or ADM
                my_email = emails.ReviewAwaitingEmail(trip_request, next_reviewer)

            elif next_reviewer.role_id in [5, 6]:  # if we are going for RDG signature...
                my_email = emails.AdminApprovalAwaitingEmail(trip_request)

            if my_email:
                # send the email object
                if settings.PRODUCTION_SERVER:
                    send_mail(message='', subject=my_email.subject, html_message=my_email.message, from_email=my_email.from_email,
                              recipient_list=my_email.to_list, fail_silently=False, )
                else:
                    print(my_email)

            # Then, lets set the trip_request status again to account for the fact that something happened
            set_request_status(trip_request)
