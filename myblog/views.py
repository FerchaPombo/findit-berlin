from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from .models import Post, Comment 
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View 
from django.views.generic.edit import FormMixin
from .forms import CommentForm 


# Create Classes for my views 

class PostListView(ListView):
    model = Post 
    template_name = 'myblog/post_list.html'

class PostDetailView(FormMixin, DetailView):
    model = Post 
    template_name = 'myblog/post_detail.html'
    form_class = 'CommentForm'

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'slug': self.object.slug})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm(initial={'post': self.object})
        return context

    def post(self, request, *args, **kwargs):
        form = self.get.form()
        if form.is_valid():
            return self.form.valid(form)
        else:
            return self.form.invalid(form)

@login_required
def like_post(request, pk):
    post = get_object_or_404(Post = pk=pk)
    if post.likes.filtered(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.remove(request.user)
    return HttpResponseRedirect(reverse_lazy('post_detail', kwargs={'slug': post.slug}))


@login_required
def add_comment(request, slug):
    post = get_object_or_404(Post, slug:slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is.valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

    return HttpResponseRedirect(reverse_lazy('post_detail', kwargs={'slug': post.slug}))


