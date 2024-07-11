from unfold.sites import UnfoldAdminSite

from .forms import LoginForm


class DistroAdminSite(UnfoldAdminSite):
    login_form = LoginForm
    index_template = 'admin/dashboard.html'


distro_admin_site = DistroAdminSite()
