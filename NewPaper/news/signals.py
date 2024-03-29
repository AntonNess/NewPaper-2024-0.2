from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from .models import Post, PostCategory


@receiver(m2m_changed, sender=PostCategory)
def post_created(instance, **kwargs):
    if not kwargs['action'] == 'post_add':
        return

    emails = User.objects.filter(
        subscriptions__category__in=instance.postCategory.all()
    ).values_list('email', flat=True)

    subject = f'Новая статья в категории {instance.postCategory}'

    text_content = (
        f'Заголовок: {instance.title}\n'
        f'Текст: {instance.text}\n\n'
        f'Ссылка на статью: http://127.0.0.1:8000{instance.get_absolute_url()}'
    )
    html_content = (
        f'Заголовок: {instance.title}<br>'
        f'Текст: {instance.text}<br><br>'
        f'<a href="http://127.0.0.1:8000{instance.get_absolute_url()}">'
        f'Ссылка на статью</a>'
    )
    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()