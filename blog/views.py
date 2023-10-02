from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.utils.text import slugify
from django.core.mail import send_mail
from django.conf import settings
from cloudinary.models import CloudinaryField
from .models import Post, UserProfile, Comment
from .forms import CommentForm, UserForm, ProfileForm, PostForm, ContactForm


# ==============================
# View functions
# ==============================
def landing_page(request):
    """
    Render the landing_page.html template
    """
    return render(request, "landing_page.html")


def about(request):
    """
    Render the about.html template
    """
    return render(request, "about.html")


def contactus_success(request):
    return render(request, 'contactus_success.html')


@login_required
def my_articles(request):
    """
    Render the my_articles.html template with user's posts and liked posts
    """
    user = request.user
    user_posts = Post.objects.filter(author=user)
    liked_posts = Post.objects.filter(likes=user)

    return render(
        request,
        "my_articles.html",
        {"user_posts": user_posts, "liked_posts": liked_posts},
    )


@login_required
def contact(request):
    """
    Render the contactus.html template
    """
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            message_name = form.cleaned_data['name']
            message_email = form.cleaned_data['email']
            message_subject = form.cleaned_data['subject']
            message_message = form.cleaned_data['message']

            send_mail(
                message_subject,  # subject
                message_message,  # message
                message_email,    # from email
                ['kimmen_b@hotmail.com'],  # to Email
            )

            return redirect('contactus_success')
    else:
        form = ContactForm()

    return render(request, "contactus.html", {'form': form})


# ==============================
# Profile
# ==============================
class ProfileView(LoginRequiredMixin, TemplateView):
    """
    View for displaying the user's profile
    """

    template_name = "profile.html"


class ProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, TemplateView):
    """
    View for updating user profile information
    """

    model = UserProfile
    user_form = UserForm
    profile_form = ProfileForm
    success_message = "Profile have been updated"
    template_name = "profile_update.html"

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests for updating user profile information
        """
        # Initialize the user form with the current user's data
        user_form = UserForm(instance=request.user)
        # Get the user's profile, or create a new one if it doesn't exist
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        # Initialize the profile form with the current user's profile data
        profile_form = ProfileForm(instance=profile)

        context = self.get_context_data(
            user_form=user_form, profile_form=profile_form
        )

        return self.render_to_response(context)

    def post(self, request):
        """
        Handles the submission of user profile update forms
        """
        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = UserForm(post_data, instance=request.user)
        # Get the user's profile, or create a new one if it doesn't exist
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        profile_form = ProfileForm(post_data, file_data, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile is updated successfully!")
            return HttpResponseRedirect(reverse_lazy("profile"))
        context = self.get_context_data(
            user_form=user_form, profile_form=profile_form
        )

        return self.render_to_response(context)


class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    """
    View for deleting an user profile
    """

    model = User
    template_name = "profile_delete.html"
    success_url = reverse_lazy("landing_page")

    def delete(self, request, *args, **kwargs):
        """
        Handles the deletion of an user profile and related objects
        """
        # Log out the user
        logout(request)

        # Delete the user profile and related objects
        return super().delete(request, *args, **kwargs)


# ==============================
# Post
# ==============================
class PostList(LoginRequiredMixin, ListView):
    """
    View for displaying a list of blog posts on the homepage
    """

    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class UsersPosts(PostList):
    """
    View for displaying a list of blog posts made by user
    """
    def get_queryset(self):
        """
        Returns a queryset of blog posts created by
        the current user, ordered by creation date
        """
        return self.request.user.blog_posts.all().order_by("-created_on")


class PostDetail(LoginRequiredMixin, View):
    """
    View for displaying a single blog post and handling comments and likes
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Retrieve and display a blog post with comments and likes
        """
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
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Handle user comments on a blog post and render the post detail view
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False

        # Check if the current user has liked the post
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        # Create a CommentForm instance and populate
        # it with data from the request
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            messages.success(request, "Your comment have been added!")
            # Redirect to the post detail page to avoid form resubmission
            return redirect("post_detail", slug=slug)
        else:
            # If the form is not valid, create a new empty CommentForm
            comment_form = CommentForm()
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )


class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    View for creating a new blog post
    """
    model = Post
    template_name = "post_create.html"
    form_class = PostForm
    success_message = "Post have been created"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        """
        Custom logic to handle form validation when creating a new blog post
        """
        form.instance.author_id = self.request.user.pk
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)


class PostUpdateView(
    LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, UpdateView
):
    """
    View for updating an existing blog post
    """
    model = Post
    template_name = "post_update.html"
    form_class = PostForm
    success_message = "Post updated successfully"

    def test_func(self):
        """
        Check if the current user is the author of the post being updated
        """
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    View for deleting an existing blog post
    """
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("index")

    def test_func(self):
        """
        Check if the current user is the author of the post being deleted
        """
        post = self.get_object()
        return self.request.user == post.author


class PostLike(LoginRequiredMixin, View):
    """
    View for handling liking and unliking a post
    """
    def post(self, request, slug, *args, **kwargs):
        """
        Toggle user's like for a post and redirect to post detail
        """
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=self.request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse("post_detail", args=[slug]))


# ==============================
# Comment
# ==============================
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    View for deleting an existing comment
    """
    model = Comment
    template_name = "comment_delete.html"

    def get_success_url(self):
        """
        Override the success_url redirect, to redirect to
        the blog post itself as the comment was removed
        """
        post_slug = self.object.post.slug
        return reverse("post_detail", kwargs={"slug": post_slug})

    def test_func(self):
        """
        Check if the current user is the owner of the comment being deleted
        """
        comment = self.get_object()
        return self.request.user == comment.user


# ==============================
# Category
# ==============================
@login_required
def CategoryView(request, category_id):
    """
    Display a list of blog posts belonging to a specific category
    """
    category_posts = Post.objects.filter(category=category_id)
    return render(
        request,
        "categories.html",
        {"category_id": category_id, "category_posts": category_posts},
    )


# ==============================
# Error handling
# ==============================
def handler403(request, exception):
    """
    Custom 403 page
    """
    return render(request, "403.html", status=403)


def handler404(request, exception):
    """
    Custom 404 page
    """
    return render(request, "404.html", status=404)


def handler405(request, exception):
    """
    Custom 405 page
    """
    return render(request, "405.html", status=405)


def handler500(request):
    """
    Custom 500 page
    """
    return render(request, "500.html", status=500)
