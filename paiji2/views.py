from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.i18n import set_language
from django.conf import settings


def confirm_language(request, code):
    if request.method == 'POST':
        return set_language(request)

    languages = settings.LANGUAGES
    new_language = None
    for language_code, language_name in languages:
        if language_code == code:
            new_language = (language_code, language_name)

    if new_language is None:
        return redirect(reverse(settings.REDIRECT_URL))

    next_page = request.GET.get('next', settings.REDIRECT_URL)

    return render(request, 'paiji2/confirm_language.html', context={
        'language': new_language,
        'next': next_page,
    })
