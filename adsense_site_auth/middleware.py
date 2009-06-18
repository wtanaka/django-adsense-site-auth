# vim:ts=2:sw=2:et
#
# Django AdSense Site Authentication Support
# http://wtanaka.com/django/adsense-site-auth 
#
# Copyright (C) 2009 Wesley Tanaka <http://wtanaka.com/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import django.http
import django.template

def get_authorization_header(request):
  authorization_header = request.META.get('HTTP_AUTHORIZATION', None)
  if authorization_header is None:
    authorization_header = request.META.get('Authorization', None)
  return authorization_header

class AdSenseSiteAuthMiddleware(object):
  def process_request(self, request):
    """Returns a 401 response to the AdSense bot"""
    request.adsense_site_authenticated = False
    import settings
    if request.META.get('HTTP_USER_AGENT', '').startswith(
                        settings.ADSENSE_BOT_USER_AGENT_PREFIX):
      authorization_header = get_authorization_header(request)
      if authorization_header:
        import base64
        expected_auth = base64.b64encode("%s:%s" % (
              settings.ADSENSE_SITEAUTH_USERNAME,
              settings.ADSENSE_SITEAUTH_PASSWORD))
        expected_header = "Basic %s" % expected_auth
        if authorization_header == expected_header:
          request.adsense_site_authenticated = True
      else:
        response = django.http.HttpResponse()
        response.status_code = 401
        response['WWW-Authenticate'] = 'Basic realm="AdSense Site Authentication"'
        response.write("""<html><head><title>401 Unauthorized</title></head><body>401 Unauthorized</body></html>""")
        return response
