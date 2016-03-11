from django.contrib import admin

# Register your models here.
#from the folder posts and file models imort the class Post
from posts.models import Post

# go to docs.djangoproject.com/en/1.9/ref/admin/#modeladmin-options to look up 
#models for admin 
class PostModelAdmin(admin.ModelAdmin):
    #this the 'updated' and 'timestamp' from posts will be displayed
    list_display = ['updated', 'timestamp']
    #change where the link is. Will not be on title but rather on 'updated' column
    list_display_links = ['updated']
    #side bar comes out with filter. Filter by day year etc
    list_filter = ['updated', 'timestamp']
    #put a search bar in that will search keywords in title or content
    search_fields = ['title', 'content']
    class Meta:
        model = Post


#admin.site.register(Post, PostAdmin)
