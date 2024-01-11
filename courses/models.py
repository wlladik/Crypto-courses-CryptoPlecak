from django.db import models
from django.urls import reverse


class Course(models.Model):
    #slug = id (but letters and nums), title, desc, image, price
    slug = models.SlugField('Uniq course name')
    title = models.CharField('Course name', max_length=120)
    desc = models.TextField('Course description')
    image = models.ImageField('Image for course', default='default.png', upload_to='course_images')
    free = models.BooleanField('Free course?', default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course-detail', kwargs={'slug': self.slug})


class Lesson(models.Model):
    # slug, title, desc, course, number, video_url
    slug = models.SlugField('Uniq lesson name')
    title = models.CharField('Lesson name', max_length=120)
    desc = models.TextField('Lesson description')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Which course?')
    number = models.IntegerField('Lesson number')
    video_url = models.CharField('Video URL', max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('lesson-detail', kwargs={'slug': self.course.slug, 'lesson_slug': self.slug})

