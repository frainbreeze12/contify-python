#!/bin/sh
gunicorn wsgi:app -w 1 -b 0.0.0.0:8000
