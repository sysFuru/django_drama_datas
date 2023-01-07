from django.http import HttpRequest
from django.contrib.auth import get_user_model

from django.test import TestCase, Client, RequestFactory
#from drama_datas.views import top

from drama_datas.models import DramaData
from django.urls import resolve
from drama_datas.views import top, drama_data_new, drama_data_edit, drama_data_detail

# Create your tests here.

UserModel = get_user_model()

"""
# トップページ
class TopPageViewTest(TestCase):

    # 200を返すか
    def test_top_return_200(self):
        request = HttpRequest()
        response = top(request)
        self.assertEqual(response.status_code, 200)
    
    # Hello Worldが表示されるか
    def test_top_returns_expected_content(self):
        request = HttpRequest()
        response = top(request)
        self.assertEqual(response.content, b"Hello World")
    
    # Hello Worldが表示されるか
    def test_top_returns_expected_content(self):
        response = self.client.get("/")
        self.assertEqual(response.content, b"Hello World")
    """
class TopPageRenderDramaDatasTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(
            username = "test_user",
            email = "test@example.com",
            password = "top_secret_pass0001",
        )
        self.drama_data = DramaData.objects.create(
            title = "sample",
            year = 2021,
            created_by = self.user,
        )

    def test_should_return_drama_data_title(self):
        request = RequestFactory().get("/")
        request.user = self.user
        response = top(request)
        self.assertContains(response, self.drama_data.title)

    def test_should_return_username(self):
        request = RequestFactory().get("/")
        request.user = self.user
        response = top(request)
        self.assertContains(response, self.drama_data.username) 

class TopPageTest(TestCase):
    def test_top_page_returns_200_and_expected_title(self):
        response = self.client.get("/")
        self.assertContains(response, "sample", status_code=200)
    
    def test_top_page_uses_expected_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "drama_datas/top.html")

class CreateDramaDataTest(TestCase):
    def test_should_resolve_drama_data_new(self):
        found = resolve("/drama_datas/new/")
        self.assertEqual(drama_data_new, found.func)

class DramaDataDetailTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(
            username = "test_user",
            email="test@example.com",
            password="secret",
        )
        self.drama_data = DramaData.objects.create(
            title="title",
            year = 2021,
            created_by = self.user,
        )

    def test_should_use_expected_template(self):
        response = self.client.get("/drama_datas/%s/" % self.drama_data.id)
        self.assertTemplateUsed(response, "drama_datas/drama_data_detail.html")
    
    def test_top_page_returns_200_and_expected_heading(self):
        response = self.client.get("/drama_datas/%s/" % self.drama_data.id)
        self.assertContains(response, self.drama_data.title, status_code=200)
    """
    def test_should_resolve_drama_data_detail(self):
        found = resolve("/drama_datas/1/")
        self.assertEqual(drama_data_detail, found.func)
    """

class EditDramaDataTest(TestCase):
    def test_should_resolve_drama_data_edit(self):
        found = resolve("/drama_datas/1/edit/")
        self.assertEqual(drama_data_edit, found.func)