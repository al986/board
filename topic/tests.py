from django.contrib.auth import get_user_model
from django.test import Client ,TestCase
from django.urls import reverse
from .models import Post

# Create your tests here.
class BoardTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = "testuser",email="test@email.com",password ="secret"
        )
        self.Post = Post.objects.create(
            title="A good title " ,body="Nice body content", auther=self.user,
        )

    def test_string_representation(self):
        Post = Post(title="A sample title")
        self.assertEqual(str(post),post.title)  

    def test_post_content(self):
        self.assertEqual(f"{self.post.title}","A good title")      
        self.assertEqual(f"{self.post.author}","testuser")
        self.assertEqual(f"{self.post.body}","Nice body content")

    def test_post_creat_view(self):
        response = self.Client.post(
            reverse("post_new"),
            {"title":"New title","body" :"New text","auther" :self.user}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,"New title")
        self.assertContains(response,"Next title")

    def test_post_update_view(self):
        response = self.Client.post( 
                reverse("post_edit" args ="1"),
            {"title":"Updte title","body" :"Updte text",},
        )   
        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self):
        response = self.Client.get(reverse("post_delete" args ="1")) 
        self.assertEqual(response.status_code, 200)