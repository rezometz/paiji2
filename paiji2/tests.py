#!/usr/bin/env python
from django.test import TestCase
from django.conf import settings
from modular_blocks import modules
from htmlvalidator.client import ValidatingClient
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse


User = get_user_model()


class PaijiTests(TestCase):

    def setUp(self):

        super(PaijiTests, self).setUp()

        modules.autodiscover()

        self.client = ValidatingClient()

        self.alice = User.objects.create_user(
            'ermentrude',
            password='ermentrude_password',
        )

        self.sigefroid = User.objects.create_user(
            'sigefroid',
            password='sigefroid_password',
            sidebar_left=[name for name, _ in modules.blocks.items()],
            sidebar_right=None,
        )

    def test_lang_homepage(self):

        # without lang
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)

        # redirected to "/fr/" or ...
        response = self.client.get(response['Location'])
        self.assertEqual(response.status_code, 302)

        # redirected to "/fr/social/" or...
        response = self.client.get(response['Location'])
        self.assertEqual(response.status_code, 200)

        for code in dict(settings.LANGUAGES):
            response = self.client.get('/' + code + '/')
            self.assertEqual(response.status_code, 302)
            response = self.client.get(response['Location'])
            self.assertEqual(response.status_code, 200)

        response = self.client.get('/es/')
        self.assertEqual(response.status_code, 404)
        response = self.client.get('/ii/')
        self.assertEqual(response.status_code, 404)

    def test_user_homepage(self):

        self.client.login(
            username='ermentrude',
            password='ermentrude_password',
        )

        self.test_lang_homepage()

        self.client.logout()

        self.client.login(
            username='sigefroid',
            password='sigefroid_password',
        )

        self.test_lang_homepage()

    def test_account(self):

        self.client.logout()

        # account url without lang
        response = self.client.get(reverse('account'))
        self.assertEqual(response.status_code, 302)

        # sign-in url without lang
        response = self.client.get(response['Location'])
        self.assertEqual(response.status_code, 302)

        # sign-in url with lang
        response = self.client.get(response['Location'])
        self.assertEqual(response.status_code, 200)

        self.client.login(
            username='sigefroid',
            password='sigefroid_password',
        )

        response = self.client.get(reverse('account'))
        self.assertEqual(response.status_code, 200)
