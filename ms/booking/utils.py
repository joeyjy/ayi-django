import json
from django.http import HttpResponse

from django.db import models
from datetime import datetime

class CommonMixin(object):
    def before_save(self):
        pass
    def after_save(self):
        pass

    def save(self, **kwargs):
        if not self.pk:
            self.date_created = datetime.now()
        intact = kwargs.pop('intact', False)
        if not intact:
            self.date_modified = datetime.now()
        super(CommonMixin, self).save(**kwargs)
        self.after_save()


def JSONResponse(json_data, charset='utf-8', ensure_ascii=False, plain=False):
    # change back if functions(dojo?) fail to work                                                                                           
    # mimetype = 'text/x-json'                                                                                                               
    mimetype = 'application/json'
    if plain: # useful for debug                                                                                                             
        mimetype = 'text/plain'
    json_data = json.dumps((json_data), ensure_ascii=ensure_ascii)
    return HttpResponse(json_data, mimetype='%s; charset=%s' %(mimetype, charset))
