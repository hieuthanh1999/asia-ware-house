import odoo.http as http
from odoo.http import request


class ApiController(http.Controller):
    @http.route("/api-controller", type="http", auth="public")
    def index(self, **kw):
        print('dsadsadsadsadas')
        return 'Xin chao toi dng tsadsadsadsades321321321321 1232132132'