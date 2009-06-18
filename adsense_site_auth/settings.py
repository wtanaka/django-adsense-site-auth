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

from django.conf import settings

# AdSense Site Authentication Username
ADSENSE_BOT_USER_AGENT_PREFIX = getattr(settings,
    'ADSENSE_BOT_USER_AGENT_PREFIX',
    'Mediapartners-Google')

# AdSense Site Authentication Username
ADSENSE_SITEAUTH_USERNAME = getattr(settings, 'ADSENSE_SITEAUTH_USERNAME',
    'AdSense')

# AdSense Site Authentication Password
ADSENSE_SITEAUTH_PASSWORD = getattr(settings, 'ADSENSE_SITEAUTH_PASSWORD',
    'BHl0eQmHsnT8Uyy03jGs')
