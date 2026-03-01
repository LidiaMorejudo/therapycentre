from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch


class DonationsViewsTests(TestCase):
    def test_donate_page_loads(self):
        url = reverse("donations:donate")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "donations/donate.html")

    def test_success_page_loads(self):
        url = reverse("donations:success")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_cancel_page_loads(self):
        url = reverse("donations:cancel")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_checkout_session_requires_post(self):
        url = reverse("donations:create_checkout_session")
        response = self.client.get(url)  # GET not allowed in your view
        self.assertEqual(response.status_code, 400)

    @patch("donations.views.stripe.checkout.Session.create")
    def test_create_checkout_session_returns_session_id(self, mock_create):
        mock_create.return_value = type("obj", (), {"id": "cs_test_123"})()

        url = reverse("donations:create_checkout_session")
        response = self.client.post(url, data={}, content_type="application/json")

        self.assertEqual(response.status_code, 200)
        self.assertIn("id", response.json())
        self.assertEqual(response.json()["id"], "cs_test_123")
        