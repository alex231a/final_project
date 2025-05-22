"""Module with celery tasks"""

import logging

from celery import shared_task # pylint: disable=E0401
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

from store.celery import app


@shared_task
def send_registration_notification(user_mail):
    """Function that sends message about registration"""
    send_mail(subject="You have successfully registered on our site",
              message=f"You have successfully registered on our site with "
                      f"email {user_mail}",
              from_email="ayakovenko.it@gmail.com",
              recipient_list=[user_mail],
              fail_silently=False,
              )


@shared_task
def send_marketing_email(user_email):
    """Function that sends message about marketing"""
    send_mail(subject="Marketing mail",
              message="Open new opportunity on our site",
              from_email="ayakovenko.it@gmail.com",
              recipient_list=[user_email],
              fail_silently=False,
              )


logger = logging.getLogger(__name__)


@shared_task
def log_user_count():
    """Function that logs user count"""
    count = get_user_model().objects.count()
    logger.info(f"Users amount is: {count}")