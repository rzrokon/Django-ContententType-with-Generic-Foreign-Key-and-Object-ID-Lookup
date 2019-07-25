# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
import gfklookupwidget.fields


class Author(models.Model):
    name = models.CharField('Name', null=True, blank=True, max_length=255)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class SortableBook(models.Model):
    title = models.CharField('Title', null=True, blank=True, max_length=255)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)
    author = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)

    class Meta(object):
        ordering = ['my_order']

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class Chapter(models.Model):
    title = models.CharField('Title', null=True, blank=True, max_length=255)
    book = models.ForeignKey(SortableBook, null=True, on_delete=models.CASCADE)
    my_order = models.PositiveIntegerField(blank=False, null=False)

    class Meta(object):
        ordering = ['my_order']

    def __str__(self):
        return 'Chapter: {0}'.format(self.title)

    def __unicode__(self):
        return 'Chapter: {0}'.format(self.title)


class Notes(models.Model):
    note = models.CharField('Note', null=True, blank=True, max_length=255)
    book = models.ForeignKey(SortableBook, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return 'Note: {0}'.format(self.note)

    def __unicode__(self):
        return 'Note: {0}'.format(self.note)


class Screen(models.Model):
    name = models.CharField('Screen Name', null=True, blank=True, max_length=255)

    class Meta(object):
        ordering = ['name']

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Track(models.Model):
    title = models.CharField('Title', null=True, blank=True, max_length=255)
    album = models.CharField('Album', null=True, blank=True, max_length=255)
    artist = models.CharField('Artist', null=True, blank=True, max_length=255)
    comments = GenericRelation('Comment')

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

class TrackList(models.Model):
    track = models.ForeignKey(Track, null=True, on_delete=models.CASCADE)
    relation = models.ForeignKey(Screen, null=True, on_delete=models.CASCADE)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)
    
    class Meta(object):
        ordering = ['my_order']

    def __str__(self):
        return 'Track: {0}'.format(self.track)

    def __unicode__(self):
        return 'Track: {0}'.format(self.track)


class Album(models.Model):
    title = models.CharField('Title', null=True, blank=True, max_length=255)
    artist = models.CharField('Artist', null=True, blank=True, max_length=255)
    comments = GenericRelation('Comment')

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class Artist(models.Model):
    title = models.CharField('Title', null=True, blank=True, max_length=255)
    intro = models.CharField('Introduction', null=True, blank=True, max_length=255)
    comments = GenericRelation('Comment')

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class Playlist(models.Model):
    title = models.CharField('Title', null=True, blank=True, max_length=255)
    intro = models.CharField('Introduction', null=True, blank=True, max_length=255)
    comments = GenericRelation('Comment')

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title



class Component(models.Model):
    title = models.CharField(null=True, blank=True, max_length=255)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)
    screen = models.CharField(
        max_length=15,
        choices=(
            ('home', 'Home'),
            ('bangla', 'Bangla'),
            ('discovery', 'Discovery'),
        ),
        default='home',
    )
    status = models.CharField(
        max_length=15,
        choices=(
            ('active', 'Active'),
            ('inactive', 'Inactive'),
        ),
        default='active',
    )

    class Meta(object):
        ordering = ['my_order']

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    limit = models.Q(app_label = 'testapp', model = 'album') | models.Q(app_label = 'testapp', model = 'artist') | models.Q(app_label = 'testapp', model = 'playlist')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to = limit)
    # object_id = models.PositiveIntegerField()
    object_id = gfklookupwidget.fields.GfkLookupField('content_type')
    content_object = GenericForeignKey('content_type', 'object_id')

    # object_id = gfklookupwidget.fields.GfkLookupField('content_type')
    # content_object = generic.GenericForeignKey('content_type', 'object_id')

    relation = models.ForeignKey(Component, null=True, on_delete=models.CASCADE)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)
    
    class Meta(object):
        ordering = ['my_order']

