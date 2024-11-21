from django.contrib import admin
import nested_admin
from django import forms
from .models import Tab, ContentBlock, Carousel, Slide

class SlideInline(nested_admin.NestedTabularInline):
    model = Slide
    extra = 1
    ordering = ['order']

class CarouselInline(nested_admin.NestedStackedInline):
    model = Carousel
    inlines = [SlideInline]
    extra = 0
    readonly_fields = ('is_active',)
    can_delete = False  # Запретить удаление карусели

class ContentBlockForm(forms.ModelForm):
    class Meta:
        model = ContentBlock
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ContentBlockForm, self).__init__(*args, **kwargs)
        block_type = None
        if self.instance and self.instance.block_type:
            block_type = self.instance.block_type
        else:
            block_type = self.data.get('block_type')

        # Скрываем или показываем поля в зависимости от block_type
        if block_type == 'carousel':
            self.fields['content'].widget = forms.HiddenInput()
            self.fields['image'].widget = forms.HiddenInput()
            self.fields['video_url'].widget = forms.HiddenInput()
        elif block_type == 'info':
            self.fields['image'].widget = forms.HiddenInput()
            self.fields['video_url'].widget = forms.HiddenInput()
        elif block_type == 'image':
            self.fields['content'].widget = forms.HiddenInput()
            self.fields['video_url'].widget = forms.HiddenInput()
        elif block_type == 'video':
            self.fields['content'].widget = forms.HiddenInput()
            self.fields['image'].widget = forms.HiddenInput()
        else:
            # Если block_type не выбран, скрываем все дополнительные поля
            self.fields['content'].widget = forms.HiddenInput()
            self.fields['image'].widget = forms.HiddenInput()
            self.fields['video_url'].widget = forms.HiddenInput()

class ContentBlockInline(nested_admin.NestedStackedInline):
    model = ContentBlock
    form = ContentBlockForm
    inlines = [CarouselInline]
    extra = 0
    ordering = ['order']

@admin.register(Tab)
class TabAdmin(nested_admin.NestedModelAdmin):
    list_display = ('name', 'slug', 'order', 'is_active')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ContentBlockInline]
    ordering = ['order']

    class Media:
        js = ('admin/js/admin_dynamic_fields.js',)
