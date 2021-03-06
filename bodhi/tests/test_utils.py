# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

from bodhi.models import Update
from bodhi.util import (get_critpath_pkgs, markup,
                        get_rpm_header, cmd)
from bodhi.config import config


class TestUtils(object):

    def test_config(self):
        assert config.get('sqlalchemy.url'), config
        assert config['sqlalchemy.url'], config

    def test_get_critpath_pkgs(self):
        """Ensure the pkgdb's critpath API works"""
        pkgs = get_critpath_pkgs()
        assert 'kernel' in pkgs, pkgs

    def test_markup(self):
        """Ensure we escape HTML"""
        text = '<b>bold</b>'
        html = markup(None, text)
        assert html == (
            "<div class='markdown'>"
            '<p>--RAW HTML NOT ALLOWED--bold--RAW HTML NOT ALLOWED--</p>'
            "</div>"
        ), html

    def test_rpm_header(self):
        h = get_rpm_header('')
        assert h['name'] == 'libseccomp', h

    def test_cmd_failure(self):
        try:
            cmd('false')
            assert False
        except Exception:
            pass
