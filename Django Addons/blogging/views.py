from django.views.generic import ListView, DetailView
from blogging.models import Post


class PostListView(ListView):
    template_name = "blogging/list.html"
    queryset = (
        Post.objects
        .exclude(published_date__isnull=True)
        .order_by("-published_date")
    )

    # provide posts for the template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = self.object_list   
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = "blogging/detail.html"

    def get_queryset(self):
        return Post.objects.exclude(published_date__isnull=True)


