import logging
from .models import Availability

logger = logging.getLogger(__name__)

class DeleteAvailability():
    try:
        Availability.objects.all().update(availability_filled=False)

        for availability in Availability.objects.filter(availability_filled=False):
            availability.days.all().update(initial_time=None, end_time=None)
            availability.save()

        logger.info("Reset completed successfully")

    except Exception as e:
        logger.exception("An error occurred during reset: %s", str(e))