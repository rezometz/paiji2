#!/usr/bin/env python
from django.test import TestCase
from django.conf import settings
from modular_blocks import modules
from htmlvalidator.client import ValidatingClient
from django.contrib.auth import get_user_model


User = get_user_model()


class PaijiTests(TestCase):

    def setUp(self):

        super(PaijiTests, self).setUp()

        modules.autodiscover()

        self.client = ValidatingClient()

        self.alice = User.objects.create_user(
            'ermentrude',
            password='ermentrude_passwd',
        )

        self.sigefroid = User.objects.create_user(
            'sigefroid',
            password='sigefroid_passwd',
            sidebar_left=[name for name, _ in modules.blocks.items()],
            sidebar_right=None,
        )

    def test_lang_homepage(self):

        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)

        for code in dict(settings.LANGUAGES):
            response = self.client.get('/' + code + '/')
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
