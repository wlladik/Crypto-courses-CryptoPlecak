from django.shortcuts import render
from cloudipsp import Api, Checkout
import time
from django.views.generic import ListView, DetailView
from .models import Course, Lesson


class HomePage(ListView):
    model = Course
    template_name = 'courses/home.html'
    context_object_name = 'courses'
    ordering = ['id']

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(HomePage, self).get_context_data(**kwargs)
        ctx['title'] = 'Home page'
        return ctx


class CourseDetailPage(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(CourseDetailPage, self).get_context_data(**kwargs)
        course = Course.objects.filter(slug=self.kwargs['slug']).first()
        ctx['title'] = course
        ctx['lessons'] = Lesson.objects.filter(course=course).order_by('number')
        return ctx


class LessonDetailPage(DetailView):
    model = Course
    template_name = 'courses/lesson_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(LessonDetailPage, self).get_context_data(**kwargs)
        # course = Course.objects.filter(slug=self.kwargs['slug']).first()
        lesson = Lesson.objects.filter(slug=self.kwargs['lesson_slug']).first()
        lesson.video_url = lesson.video_url.split("=")[1]
        ctx['title'] = lesson
        ctx['lesson'] = lesson
        return ctx


def subscription_page(request):
    api = Api(merchant_id=1396424,
              secret_key='test')
    checkout = Checkout(api=api)
    data = {
        "currency": "USD",
        "amount": 4400,
        "order_desc": "Subscription payment",
        "order_id": str(time.time()),
        "merchant_data": "example@gmail.com"
    }
    url = checkout.url(data).get('checkout_url')
    courses = Course.objects.all()
    return render(request, 'courses/subscription.html', {'title': 'Subscriptions', 'courses': courses})


def callback_payment(request):
    if request.method == 'POST':
        data = request.POST
