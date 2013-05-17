from django.contrib import admin

from tuxhe_blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'author_id', 'create_at', 'update_at')
    list_filter = ('create_at', 'update_at')
    search_fields = ('title', 'author_id__username', 'author_id__first_name')

    fieldsets = [
        ('Post', {
            'fields': ('title', 'url', 'thumbnail', 'short_content', 'content',
                       'tags', 'status')
        }),
        ('Author', {
            'classes': ('collapse',),
            'fields': ('author_id',)
        }),
        ('Change History', {
            'classes': ('collapse',),
            'fields': ('create_at', 'update_at')
        })
    ]
    readonly_fields = ('create_at', 'update_at')

admin.site.register(Post, PostAdmin)
