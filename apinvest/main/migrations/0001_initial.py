# Generated by Django 4.2.16 on 2024-11-19 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активна ли карусель')),
            ],
        ),
        migrations.CreateModel(
            name='Tab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название вкладки')),
                ('slug', models.SlugField(unique=True, verbose_name='Ссылка (slug)')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активна ли вкладка')),
            ],
            options={
                'verbose_name': 'Вкладка',
                'verbose_name_plural': 'Вкладки',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок слайда')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание слайда')),
                ('image', models.ImageField(upload_to='carousel/', verbose_name='Изображение')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
                ('carousel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slides', to='main.carousel', verbose_name='Карусель')),
            ],
            options={
                'verbose_name': 'Слайд',
                'verbose_name_plural': 'Слайды',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='ContentBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_type', models.CharField(choices=[('carousel', 'Карусель'), ('info', 'Раздел с информацией'), ('image', 'Фотография'), ('video', 'Видео')], max_length=50, verbose_name='Тип блока')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок блока')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Заголовок блока')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Содержимое')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blocks/images/', verbose_name='Изображение')),
                ('video_url', models.URLField(blank=True, null=True, verbose_name='Ссылка на видео')),
                ('tab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_blocks', to='main.tab', verbose_name='Вкладка')),
            ],
            options={
                'verbose_name': 'Блок контента',
                'verbose_name_plural': 'Блоки контента',
                'ordering': ['order'],
            },
        ),
        migrations.AddField(
            model_name='carousel',
            name='content_block',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='carousel', to='main.contentblock', verbose_name='Блок контента'),
        ),
    ]