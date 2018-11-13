#!/usr/bin/python3
"""Folder becomes a python module"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
