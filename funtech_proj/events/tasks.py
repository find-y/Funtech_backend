import time

from celery import shared_task

BACKGROUND_TASK_DURATION = 20


@shared_task
def background_task(*args, **kwargs) -> str:
    """
    Имитация тяжелой задачи (типа массовой рассылки или обработки изображений),
    которая должна выполняться в фоновом режиме.
    """
    time.sleep(BACKGROUND_TASK_DURATION)
    return "Heavy backgroud task has been done !!!"
