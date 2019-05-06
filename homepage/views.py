from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
import django.utils.translation


def testlang(request):
    return HttpResponse(_('Welcome to language translation!'))


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the home page of the app.")


# def about(request):
#     title = 'Software for the Global Market 2 2018-2019'
#     author = 'Replace this with your name'
#     html = '''<!DOCTYPE html>
#     <html>
#     <head>
#       <title>''' + title + '''</title>
#     </head>
#     <body>
#         <h1>About ''' + title + '''</h1>
#         <p>This Website was developed by ''' + author + '''.</p>
#     </body>
#     </html>'''
#     return HttpResponse(html)


from django.views.generic import TemplateView

class HomeView(TemplateView):

    def get(self, request, **kwargs):
        # from django.utils import translation
        # user_language = "en"
        # translation.activate(user_language)
        # request.session[translation.LANGUAGE_SESSION_KEY] = user_language

        languuage = request.LANGUAGE_CODE

        if (languuage == 'fr' or languuage == 'zh-cn' or languuage == 'en'):
            url_1 = 'images/{}/icons/one.png'.format(languuage)
            url_2 = 'images/{}/icons/one.png'.format(languuage)
        else:
            url_1 = 'images/{}/icons/travel_ic.png'.format(languuage)
            url_2 = 'images/{}/icons/plane_ic.png'.format(languuage)

        home = _("Home")
        destinations = _("Flight Destinations")
        sign_in = _("Sign In")
        bookings = _("Book Flights")
        placeHolderText = _("Search Travel Guide")
        slogan = _("Create Your Journey Your Adventure Starts Here")

        return render(request, 'base.html', {'title': home, 'url_1': url_1, 'url_2':url_2, 'destinations': destinations, 'bookings': bookings, 'sign_in': sign_in, 'current_lang':languuage
                                             , 'placeholderText': placeHolderText, 'slogan': slogan})
