"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.shortcuts import render_to_response


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class TestTemplates(TestCase):
    def _load_template(self, templateName, context):
        print "Loading template %s " % (templateName)
        return render_to_response(templateName, context)

    def test_chapter(self):
        self._load_template("chapter.djt.html", dict())

    def test_country(self):
        self._load_template("country.djt.html", dict())

    def test_edit_event(self):
        self._load_template("edit-event.djt.html", dict())

    def test_event(self):
        self._load_template("event.djt.html", dict())

    def test_frame(self):
        self._load_template("frame.djt.html", dict())

    def test_front(self):
        self._load_template("front.djt.html", dict())

    def test_illustration(self):
        self._load_template("illustration.djt.html", dict())

    def test_image_upload(self):
        self._load_template("imageupload.djt.html", dict())

    def test_image_framed(self):
        self._load_template("img-framed.djt.html", dict())

    def test_location(self):
        self._load_template("location.djt.html", dict())

    def test_manuscript(self):
        self._load_template("manuscript.djt.html", dict())

    def test_msgallery(self):
        self._load_template("msgallery.djt.html", dict())

    def test_msgrid(self):
        self._load_template("msgrid.djt.html", dict())

    def test_mslist(self):
        self._load_template("mslist.djt.html", dict())

    def test_pagelist(self):
        self._load_template("pagelist.djt.html", dict())

    def test_scene(self):
        self._load_template("scene.djt.html", dict())
