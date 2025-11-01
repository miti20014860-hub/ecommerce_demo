from django.contrib import admin
from .models import About, Contact, Terms, Privacy, Faq, Part, Section

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'description', 'ending')
    search_fields = ('title', 'subtitle', 'description', 'ending')
    search_help_text = "Search by title, subtitle, or description"
    ordering = ('title',)
    list_filter = ('subtitle',)
    readonly_fields = ('title',)
    fieldsets = (
        ('About', {'fields': ('title', 'subtitle', 'description', 'ending')}),
    )

@admin.register(Contact)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'person', 'description', 'ending')
    search_fields = ('title', 'subtitle', 'person', 'description', 'ending')
    search_help_text = "Search by title, subtitle, person, or description"
    ordering = ('title',)
    list_filter = ('subtitle',)
    readonly_fields = ('title',)
    fieldsets = (
        ('Contact', {'fields': ('title', 'subtitle', 'person', 'description', 'ending')}),
    )

@admin.register(Privacy)
class PrivacyAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'ending')
    search_fields = ('title', 'description', 'ending')
    search_help_text = "Search by title, or description"
    ordering = ('title',)
    readonly_fields = ('title',)
    fieldsets = (
        ('Privacy', {'fields': ('title', 'description', 'ending')}),
    )

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'question', 'answer')
    search_fields = ('title', 'subtitle', 'question', 'answer')
    search_help_text = "Search by title, subtitle, or question"
    ordering = ('id',)
    list_filter = ('subtitle',)
    readonly_fields = ('title',)
    fieldsets = (
        ('FAQ', {'fields': ('title', 'subtitle', 'question', 'answer')}),
    )

class PartInline(admin.TabularInline):
    model = Part
    extra = 1
    fields = ('part', 'partno', 'partname', 'partdesc')
    ordering = ('partno',)

class SectionInline(admin.TabularInline):
    model = Section
    extra = 1
    fields = ('sect', 'sectno', 'sectname', 'sectdesc')
    ordering = ('sectno',)

@admin.register(Terms)
class TermsAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle_1', 'description_1', 'subtitle_2', 'description_2')
    search_fields = ('title', 'subtitle_1', 'description_1', 'subtitle_2', 'description_2')
    search_help_text = "Search by title, subtitle, or description"    
    ordering = ('title',)
    list_filter = ( 'subtitle_1', 'subtitle_2')
    readonly_fields = ('title',)
    fieldsets = (
        ('Terms & Conditions', {'fields': ('title', 'subtitle_1', 'description_1', 'subtitle_2', 'description_2')}),
    )
    inlines = [PartInline, SectionInline]
    save_on_top = True
