from django.db import models

# Выбор для поля "для кого"
WHO_CHOICES = (
    ('Учитель', 'Учитель'),
    ('Ученик', 'Ученик'),
)

AUDIO_TYPE_CHOICES = (
    ('Основное', 'Основное'),
    ('Повторение', 'Повторение'),
)

class Ebook(models.Model):
    title = models.CharField("Название", max_length=200)
    author = models.CharField("Автор", max_length=100)
    year = models.CharField("Год", max_length=10)
    grade = models.CharField("Класс", max_length=10)
    who = models.CharField("Для кого", max_length=20, choices=WHO_CHOICES)
    slug = models.SlugField("Слаг", max_length=200, unique=True)

    def __str__(self):
        return self.title

class AudioFile(models.Model):
    ebook = models.ForeignKey(Ebook, on_delete=models.CASCADE, verbose_name="Электронная книга")
    page = models.CharField("Страница", max_length=20)  # ← ЭТО поле обязательно должно быть
    audio_mark = models.CharField("Метка аудио", max_length=20)
    order = models.PositiveIntegerField("Порядок")
    audio_file = models.FileField("Аудиофайл", upload_to='audios/')
    audio_type = models.CharField("Тип аудио", max_length=20, choices=AUDIO_TYPE_CHOICES)
    description = models.TextField("Описание", blank=True)

    def __str__(self):
        return f"{self.ebook.title} - {self.page} - {self.audio_mark}"
