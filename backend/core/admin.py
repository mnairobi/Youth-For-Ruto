from django.contrib import admin

from core.models import (
    County,
    Leader,
    AgendaItem,
    NewsCategory,
    NewsArticle,
    Event,
    GalleryCategory,
    GalleryImage,
    MemberRegistration,
    ContactMessage,
    Donation,
    Testimonial,
    Subscriber,
    SiteSettings,
)


# ── County ────────────────────────────────────────────────────────────────

@admin.register(County)
class CountyAdmin(admin.ModelAdmin):
    list_display   = ['name', 'code', 'registered_youth']   # ← was registered_members
    search_fields  = ['name']
    list_editable  = ['registered_youth']                   # ← was registered_members


# ── Leader ────────────────────────────────────────────────────────────────

@admin.register(Leader)
class LeaderAdmin(admin.ModelAdmin):
    list_display  = [
        'full_name',
        'get_display_title',   # ← callable instead of 'title'
        'level',
        'position',            # ← was 'role'
        'county',
        'order',
        'is_active',
    ]
    list_filter   = [
        'level',       # ← was 'role'
        'position',    # ← added
        'is_active',
        'county',
    ]
    search_fields  = ['full_name', 'custom_title']
    list_editable  = ['order', 'is_active']
    fieldsets = (
        ('Basic Info', {
            'fields': (
                'full_name', 'position', 'custom_title',
                'level', 'county', 'photo', 'bio',
            )
        }),
        ('Contact', {
            'fields': ('phone', 'email'),
        }),
        ('Social Media', {
            'fields': ('twitter', 'facebook', 'instagram', 'tiktok'),
            'classes': ('collapse',),
        }),
        ('Settings', {
            'fields': ('order', 'is_active'),
        }),
    )

    # ── Custom column ─────────────────────────────────────────────
    @admin.display(description='Title')
    def get_display_title(self, obj):
        return obj.display_title


# ── AgendaItem ────────────────────────────────────────────────────────────

@admin.register(AgendaItem)
class AgendaItemAdmin(admin.ModelAdmin):
    list_display       = ['title', 'icon', 'order', 'is_active']
    list_editable      = ['order', 'is_active']
    prepopulated_fields = {'slug': ('title',)}
    search_fields      = ['title']


# ── News ──────────────────────────────────────────────────────────────────

@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display       = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display       = [
        'title', 'category', 'author',
        'is_featured', 'is_published', 'views', 'created_at',
    ]
    list_filter        = ['category', 'is_featured', 'is_published', 'created_at']
    search_fields      = ['title', 'excerpt']
    prepopulated_fields = {'slug': ('title',)}
    list_editable      = ['is_featured', 'is_published']
    date_hierarchy     = 'created_at'
    readonly_fields    = ['views', 'created_at', 'updated_at']


# ── Event ─────────────────────────────────────────────────────────────────

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display       = ['title', 'venue', 'date', 'status', 'county', 'is_featured']
    list_filter        = ['status', 'is_featured', 'county']
    search_fields      = ['title', 'venue']
    prepopulated_fields = {'slug': ('title',)}
    list_editable      = ['status', 'is_featured']
    date_hierarchy     = 'date'


# ── Gallery ───────────────────────────────────────────────────────────────

@admin.register(GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display       = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display  = ['title', 'category', 'is_featured', 'created_at']
    list_filter   = ['category', 'is_featured']
    search_fields = ['title', 'caption']
    readonly_fields = ['created_at']


# ── Member Registration ──────────────────────────────────────────────────
@admin.register(MemberRegistration)
class MemberRegistrationAdmin(admin.ModelAdmin):
    list_display    = [
        'full_name',
        'phone',
        'email',
        'gender',
        'county',
        'constituency',
        'ward',
        'is_verified',
        'created_at',
    ]
    list_filter     = ['county', 'gender', 'is_verified', 'created_at']
    search_fields   = ['full_name', 'phone', 'email', 'constituency', 'ward']
    list_editable   = ['is_verified']
    readonly_fields = ['created_at']
    date_hierarchy  = 'created_at'
    fieldsets       = (
        ('Personal Details', {
            'fields': ('full_name', 'phone', 'email', 'gender'),
        }),
        ('Location', {
            'fields': ('county', 'constituency', 'ward'),
        }),
        ('Admin', {
            'fields': ('is_verified', 'created_at'),
        }),
    )
    
# ── Contact Message ───────────────────────────────────────────────────────

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display   = [
        'full_name', 'email', 'subject',
        'is_read', 'is_replied', 'created_at',
    ]
    list_filter    = ['subject', 'is_read', 'is_replied']
    list_editable  = ['is_read', 'is_replied']
    search_fields  = ['full_name', 'email', 'message']
    readonly_fields = ['created_at']


# ── Donation ──────────────────────────────────────────────────────────────

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display  = [
        'donor_name', 'amount', 'payment_method',
        'status', 'is_anonymous', 'created_at',
    ]
    list_filter   = ['payment_method', 'status', 'is_anonymous']
    search_fields = ['donor_name', 'transaction_id', 'phone']
    readonly_fields = ['created_at']


# ── Testimonial ───────────────────────────────────────────────────────────

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display  = ['name', 'location', 'role', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    search_fields = ['name', 'quote']


# ── Subscriber ────────────────────────────────────────────────────────────

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display  = ['email', 'phone', 'is_active', 'created_at']
    list_filter   = ['is_active']
    search_fields = ['email', 'phone']
    readonly_fields = ['created_at']


# ── Site Settings (singleton) ─────────────────────────────────────────────

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Identity', {
            'fields': ('site_name', 'tagline'),
        }),
        ('Content', {
            'fields': ('about_text', 'mission', 'vision'),
        }),
        ('Contact', {
            'fields': ('phone', 'email', 'address'),
        }),
        ('Social Media', {
            'fields': ('twitter', 'instagram', 'tiktok', 'facebook', 'youtube', 'whatsapp'),
        }),
        ('M-Pesa', {
            'fields': ('mpesa_paybill', 'mpesa_account'),
        }),
    )

    def has_add_permission(self, request):
        # Only one row allowed
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Cannot delete the singleton
        return False


# ── Admin site branding ───────────────────────────────────────────────────

admin.site.site_header  = 'YR27 – Youths for Ruto 2027'
admin.site.site_title   = 'YR27 Admin'
admin.site.index_title  = 'Dashboard – 2027 Ruto Tena'