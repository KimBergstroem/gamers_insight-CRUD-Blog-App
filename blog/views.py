from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import (
    FormView, 
    CreateView, 
    UpdateView, 
    DeleteView
    )
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
from .models import Post, UserProfile, Comment
from .forms import (
    CommentForm, 
    UserForm, 
    ProfileForm,
    PostForm
)

# ==============================
# Main
# ==============================
def landing_page(request):
    """
    Render the landing_page.html template
    """
    return render(request, 'landing_page.html')


def about(request):
    """
    Render the about.html template
    """
    return render(request, 'about.html')


def contactus(request):
    """
    Render the contactus.html template
    """
    return render(request, 'contactus.html')


class PostLike(View):
    """
    View for handling liking and unliking a post.
    """
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=self.request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
									        
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


# ==============================
# Profile
# ==============================
class ProfileView(LoginRequiredMixin, TemplateView):
    """
    View for displaying the user's profile.
    """
    model = UserProfile
    template_name = 'profile.html'


class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    """
    View for updating user profile information.
    """
    model = UserProfile
    user_form = UserForm
    profile_form = ProfileForm
    template_name = 'profile_update.html'

    def get(self, request, *args, **kwargs):
        # Initialize the user form with the current user's data
        user_form = UserForm(instance=request.user)
        # Get the user's profile, or create a new one if it doesn't exist
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        # Initialize the profile form with the current user's profile data
        profile_form = ProfileForm(instance=profile)
        
        context = self.get_context_data(
            user_form=user_form,
            profile_form=profile_form
        )

        return self.render_to_response(context)

    def post(self, request):
        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = UserForm(post_data, instance=request.user)
        # Get the user's profile, or create a new one if it doesn't exist
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        profile_form = ProfileForm(post_data, file_data, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully!')
            return HttpResponseRedirect(reverse_lazy('profile'))

        context = self.get_context_data(
            user_form=user_form,
            profile_form=profile_form
        )

        return self.render_to_response(context)

class ProfileDeleteView(SuccessMessageMixin, LoginRequiredMixin, generic.DeleteView):
    """
    View for deleting an user profile.
    """
    model = User
    template_name = 'profile_delete.html'
    success_message = "User has been deleted"
    success_url = reverse_lazy('landing_page')

    def delete(self, request, *args, **kwargs):
        # Log out the user
        logout(request)
        
        # Delete the user profile and related objects
        return super().delete(request, *args, **kwargs)


# ==============================
# Post
# ==============================
class PostList(generic.ListView):
    """
    View for displaying a list of blog posts on the homepage.
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):
    """
    View for displaying a single blog post and handling comments and likes.
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

class PostCreateView(CreateView):
    """
    View for creating a new blog post.
    """
    model = Post
    template_name = 'post_create.html'
    form_class = PostForm
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        form.instance.author_id = self.request.user.pk
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    """
    View for updating an existing blog post.
    """
    model = Post
    template_name = 'post_update.html'
    fields = ['title', 'featured_image', 'excerpt', 'content']


class PostDeleteView(DeleteView):
    """
    View for deleting an existing blog post.
    """
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('index')


# ==============================
# Comment
# ==============================
class CommentDeleteView(DeleteView):
    """
    View for deleting an existing comment.
    """
    model = Comment
    template_name = 'comment_delete.html'

    #Override the success_url redirect, to redirect to the blog post itself as the comment was removed
    def get_success_url(self):
        post_slug = self.object.post.slug
        return reverse('post_detail', kwargs={'slug': post_slug})  


# ==============================
# Category
# ==============================
def CategoryView(request, genre):
    """
    View for displaying a list of blog posts belonging to a specific category.

    Args:
        request (HttpRequest): The HTTP request object.
        genre (str): The category genre to filter posts by.

    Returns:
        HttpResponse: A rendered HTML page displaying category-specific blog posts.
    """
    category_posts = Post.objects.filter(category=genre)
    return render(request, 'categories.html', {'genre': genre, 'category_posts': category_posts})
