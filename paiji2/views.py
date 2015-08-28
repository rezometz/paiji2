from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.i18n import set_language
from django.conf import settings
from django.utils.translation import get_language_info,\
    check_for_language


def confirm_language(request, code):
    if request.method == 'POST':
        return set_language(request)

    try:
        assert(check_for_language(code))
        assert(code in dict(settings.LANGUAGES))
        new_language = get_language_info(code)
    except:
        return redirect(settings.REDIRECT_URL)

    next_page = request.GET.get('next', settings.REDIRECT_URL)

    return render(request, 'paiji2/confirm_language.html', context={
        'new_language': new_language,
        'next': next_page,
    })
