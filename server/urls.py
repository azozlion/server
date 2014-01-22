from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'taxiexpress.views.index', name='index'),
    url(r'^client/login', 'taxiexpress.views.loginUser', name='loginUser'),
    url(r'^client/register', 'taxiexpress.views.registerUser', name='registerUser'),
    url(r'^client/validateuser', 'taxiexpress.views.validateUser', name='validateUser'),
    url(r'^client/recovervalidationcodecustomer', 'taxiexpress.views.recoverValidationCodeCustomer', name='recoverValidationCodeCustomer'),
    url(r'^client/recovervalidationcodedriver', 'taxiexpress.views.recoverValidationCodeDriver', name='recoverValidationCodeDriver'),
    url(r'^client/gettaxi', 'taxiexpress.views.getClosestTaxiBeta', name='getClosestTaxiBeta'),
    url(r'^driver/accepttravel', 'taxiexpress.views.acceptTravel', name='acceptTravel'),
    url(r'^driver/travelstarted', 'taxiexpress.views.travelStarted', name='travelStarted'),
    url(r'^driver/travelcompleted', 'taxiexpress.views.travelCompleted', name='travelCompleted'),
    url(r'^client/travelpaid', 'taxiexpress.views.travelPaid', name='travelPaid'),
    url(r'^client/getneartaxies', 'taxiexpress.views.getNearestTaxies', name='getNearestTaxies'),
    url(r'^client/changedetails', 'taxiexpress.views.updateProfile', name='updateProfile'),
    url(r'^client/changepassword', 'taxiexpress.views.changePassword', name='changePassword'),
    url(r'^client/changefilters', 'taxiexpress.views.updateFilters', name='updateFilters'),
    url(r'^client/addfavorite', 'taxiexpress.views.addFavoriteDriver', name='addFavoriteDriver'),
    url(r'^client/removefavorite', 'taxiexpress.views.removeFavoriteDriver', name='removeFavoriteDriver'),
    url(r'^client/removetravel', 'taxiexpress.views.removeTravel', name='removeTravel'),
    url(r'^client/getlasttravel', 'taxiexpress.views.getLastTravel', name='getLastTravel'),
    url(r'^driver/login', 'taxiexpress.views.loginDriver', name='loginDriver'),
    url(r'^driver/updatedriverposition', 'taxiexpress.views.updateDriverPosition', name='updateDriverPosition'),
    url(r'^driver/updatedriveravailable', 'taxiexpress.views.updateDriverAvailable', name='updateDriverAvailable'),
    url(r'^test', 'taxiexpress.views.testPush', name='testPush'),
    url(r'^loaddata', 'taxiexpress.views.loadData', name='loaddata'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^recoverpassword', 'taxiexpress.views.recoverPassword', name='recoverPassword'),

    # url(r'^server/', include('server.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

        #url para la Web
    url(r'^$', 'web.views.index', name='index'),
    url(r'^map', 'web.views.map', name='map'),
    url(r'^client', 'web.views.client', name='client'),
    url(r'^driver', 'web.views.driver', name='driver'),
    url(r'^faq', 'web.views.faq', name='faq'),
    url(r'^legalnotice', 'web.views.legalnotice', name='legalnotice'),
    url(r'^register', 'web.views.register', name='register'),
    url(r'^mantclient_data', 'web.views.mantclient_data', name='mantclient_data'),
    url(r'^mantclient_changepassword', 'web.views.mantclient_changePassword', name='mantclient_changePassword'),
    url(r'^mantclient_preferences', 'web.views.mantclient_preferences', name='mantclient_preferences'),
    url(r'^mantdriver_data', 'web.views.mantdriver_data', name='mantdriver_data'),
    url(r'^mantdriver_changepassword', 'web.views.mantdriver_changePassword', name='mantdriver_changePassword'),
    url(r'^mantdriver_car', 'web.views.mantdriver_car', name='mantdriver_car'),
    url(r'^mantdriver_bankaccount', 'web.views.mantdriver_bankAccount', name='mantdriver_bankAccount'),
    url(r'^mantdriver_travelgraphic', 'web.views.mantdriver_TravelGraphic', name='mantdriver_TravelGraphic'),
    url(r'^termsofuse', 'web.views.termsofuse', name='termsofuse'),
    url(r'^validatecode', 'web.views.validateCode', name='validateCode'),
    url(r'^logout', 'web.views.logout', name='logout'),
    url(r'^updateprofileuserweb', 'web.views.updateProfileUserWeb', name='updateProfileUserWeb'),
    url(r'^updateprofiledriverweb', 'web.views.updateProfileDriverWeb', name='updateProfileDriverWeb'),
    url(r'^updatecarweb', 'web.views.updateCarWeb', name='updateCarWeb'),
    url(r'^recovervalidationcode', 'web.views.recoverValidationCodeWeb', name='recoverValidationCodeWeb'),
    url(r'^contact', 'web.views.contact', name='contact'),
    url(r'^statistics/gettravelsbymonth', 'web.views.getTravelsByMonth', name='getTravelsByMonth'),
)
