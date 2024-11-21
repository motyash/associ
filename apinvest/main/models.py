from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Tab(models.Model):
    """Модель для вкладок на сайте."""
    name = models.CharField(max_length=100, verbose_name="Название вкладки")
    slug = models.SlugField(unique=True, verbose_name="Ссылка (slug)")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")
    is_active = models.BooleanField(default=True, verbose_name="Активна ли вкладка")

    class Meta:
        ordering = ['order']
        verbose_name = "Вкладка"
        verbose_name_plural = "Вкладки"

    def __str__(self):
        return self.name

class ContentBlock(models.Model):
    """Модель для блоков контента, привязанных к вкладке."""
    BLOCK_TYPES = [
        ('carousel', 'Карусель'),
        ('info', 'Раздел с информацией'),
        ('image', 'Фотография'),
        ('video', 'Видео'),
    ]

    tab = models.ForeignKey(
        Tab,
        related_name="content_blocks",
        on_delete=models.CASCADE,
        verbose_name="Вкладка"
    )
    block_type = models.CharField(max_length=50, choices=BLOCK_TYPES, verbose_name="Тип блока")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок блока")
    title = models.CharField(max_length=200, verbose_name="Заголовок блока", blank=True, null=True)
    content = models.TextField(verbose_name="Содержимое", blank=True, null=True)
    image = models.ImageField(upload_to='blocks/images/', verbose_name="Изображение", blank=True, null=True)
    video_url = models.URLField(verbose_name="Ссылка на видео", blank=True, null=True)

    class Meta:
        ordering = ['order']
        verbose_name = "Блок контента"
        verbose_name_plural = "Блоки контента"

    def __str__(self):
        return f"{self.tab.name} - {self.get_block_type_display()} - {self.order}"

class Carousel(models.Model):
    """Модель для каруселей, привязанных к блокам контента."""
    content_block = models.OneToOneField(
        ContentBlock,
        related_name="carousel",
        on_delete=models.CASCADE,
        verbose_name="Блок контента"
    )
    is_active = models.BooleanField(default=True, verbose_name="Активна ли карусель")

    def __str__(self):
        return f"Карусель в блоке: {self.content_block.title}"

class Slide(models.Model):
    """Модель для слайдов в карусели."""
    carousel = models.ForeignKey(
        Carousel,
        related_name="slides",
        on_delete=models.CASCADE,
        verbose_name="Карусель"
    )
    title = models.CharField(max_length=200, verbose_name="Заголовок слайда")
    description = models.TextField(verbose_name="Описание слайда", blank=True, null=True)
    image = models.ImageField(upload_to='carousel/', verbose_name="Изображение")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")

    class Meta:
        ordering = ['order']
        verbose_name = "Слайд"
        verbose_name_plural = "Слайды"

    def __str__(self):
        return f"{self.carousel.content_block.tab.name} - {self.title}"

# Сигнал для автоматического создания объекта Carousel
@receiver(post_save, sender=ContentBlock)
def create_carousel_for_content_block(sender, instance, created, **kwargs):
    if instance.block_type == 'carousel':
        if not hasattr(instance, 'carousel'):
            Carousel.objects.create(content_block=instance)
