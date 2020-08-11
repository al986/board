def test_post_list_view(self):
    response =self.client.get(reverse("home"))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response,"Nice body content")
    self.assertTemplateUsed(response,"home.html")

def test_post_detail_view(self):
    response =self.client.get("/post/1/")
    no_response =self.client.get("/post/1000/")
    self.assertEqual(response.status_code, 200)
    self.assertEqual(no_response.status_code, 404)
    self.assertContains(response,"A good title")
    self.assertTemplateUsed(response,"post_detail.html")


