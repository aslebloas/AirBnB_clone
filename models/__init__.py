#!/usr/bin/python3
"""Folder becomes a python module"""
import engine.file_storage

storage = FileStorage()
reload(storage)
