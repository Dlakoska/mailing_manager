import logging
from django.conf import settings
from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util
from mailing.utils import check_and_send_mailing

logger = logging.getLogger(__name__)


@util.close_old_connections
def delete_old_job_executions(max_age=604_800):
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timzone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            check_and_send_mailing,
            trigger=IntervalTrigger(seconds=10),
            id="check_and_send_mailing",  # The `id` assigned to each job MUST be unique
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'my_job'.")

        try:
            logger.info("Шедулер запущен")
            print("Шедулер запущен")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Шедулер остановлен")
            scheduler.shutdown()
            logger.info("Шедулер остановлен успешно")
