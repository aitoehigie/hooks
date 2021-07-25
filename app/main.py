# -*- coding: utf-8 -*-
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from . import views

app = FastAPI()

# Set all CORS enabled origins
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=["*"],
                   allow_methods=["*"],
                   allow_headers=["*"],
                   )

app.include_router(views.router)
