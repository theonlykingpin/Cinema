from django.urls import reverse
from django.contrib.auth.models import User

class AccountsTests(TestCase):
    
    def test_user_registration(self):
        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'password1': 'password123',
            'password2': 'password123',
            'email': 'testuser@example.com'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful registration
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_user_login(self):
        User.objects.create_user(username='testuser', password='password123')
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful login

    def test_profile_update(self):
        user = User.objects.create_user(username='testuser', password='password123')
        self.client.login(username='testuser', password='password123')
        response = self.client.post(reverse('profile_update'), {
            'username': 'testuser_updated',
            'email': 'testuser_updated@example.com'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful profile update
        user.refresh_from_db()
        self.assertEqual(user.username, 'testuser_updated')
        self.assertEqual(user.email, 'testuser_updated@example.com')
