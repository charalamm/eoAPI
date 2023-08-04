import azure.functions as func

from eoapi.raster.app import app as raster_app


app = func.AsgiFunctionApp(app=raster_app, http_auth_level=func.AuthLevel.ANONYMOUS)
