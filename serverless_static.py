from os
from starlette.response import FileResponse
from starlette.staticfiles import StaticFiles

# Define the directory where your static files are collected
static_dir = os.path.join(os.getcwd(), "staticfiles")

app = StaticFiles(directory=static_dir, packages=[])

def handler(request):
	return app(request)