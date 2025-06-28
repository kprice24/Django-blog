from django.contrib import admin
from blogging.models import Post, Category


# Pick Categories while editing a Post
class CategoryInline(admin.TabularInline):         
    model = Category.posts.through                
    extra = 1                                      


# Custom Post admin
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]
    list_display = ("title", "author", "published_date")
    search_fields = ("title",)


# Custom Category admin hides the posts field
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ("posts",)                           
    list_display = ("name",)
