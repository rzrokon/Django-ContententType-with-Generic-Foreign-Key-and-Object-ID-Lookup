#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

from . import models

from generic_fk.mixins import ModelAdminMixin



from django.contrib.admin.widgets import ForeignKeyRawIdWidget
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import ManyToOneRel
from django import forms

from generic_fk.widgets import ContentTypeSelect


import gfklookupwidget


# class ChapterInline(SortableInlineAdminMixin, admin.StackedInline):
#     model = models.Chapter
#     extra = 1


# class TrackInline(SortableInlineAdminMixin, admin.StackedInline):
#     model = models.Track
#     extra = 1

class TrackListInline(SortableInlineAdminMixin, admin.StackedInline):
    model = models.TrackList
    autocomplete_fields = ['track']
    extra = 1


class RelationInline(SortableInlineAdminMixin, admin.TabularInline):
    model = models.Comment
    # autocomplete_fields = ['track']
    extra = 0


class MyModelInline(SortableInlineAdminMixin, admin.TabularInline):
    model = models.Comment
    extra = 0

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'object_id':
            kwargs['widget'] = gfklookupwidget.widgets.GfkLookupWidget(
                content_type_field_name='content_type',
                parent_field=models.Comment._meta.get_field('content_type'),
            )

        return super(MyModelInline, self).formfield_for_dbfield(db_field, **kwargs)



# class NotesInline(admin.TabularInline):
#     model = models.Notes
#     extra = 1


# @admin.register(models.SortableBook)
# class SortableBookAdmin(SortableAdminMixin, admin.ModelAdmin):
#     list_per_page = 12
#     list_display = ['author', 'title', 'my_order']
#     list_display_links = ['title']
#     inlines = [ChapterInline, NotesInline]


# @admin.register(models.Author)
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ['name']


# @admin.register(models.Notes)
# class NoteAdmin(SortableAdminMixin, admin.ModelAdmin):
#     list_display = ['note']
#     ordering = ['note']


@admin.register(models.Component)
class ComponentAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_per_page = 12
    list_display = ['title','screen','my_order','status']
    list_display_links = ['title']
    inlines = [RelationInline]
    list_filter = ['screen']

@admin.register(models.Screen)
class ScreenAdmin(admin.ModelAdmin):
    list_per_page = 12
    list_display = ['name']
    list_display_links = ['name']
    inlines = [TrackListInline]

@admin.register(models.Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ['title', 'album', 'artist']
    list_display_links = ['title']
    search_fields = ['title']

@admin.register(models.Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']
    search_fields = ['title']

@admin.register(models.Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']
    search_fields = ['title']

@admin.register(models.Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']
    search_fields = ['title']

@admin.register(models.TrackList)
class TrackListAdmin(admin.ModelAdmin):
    list_display = ['track']
    list_display_links = ['track']
    search_fields = ['track']


class CommentForm(forms.ModelForm):
    class Meta(object):
        model = models.Comment
        fields = ['content_type','object_id']
        widgets = {
            'object_id': gfklookupwidget.widgets.GfkLookupWidget(
                content_type_field_name='content_type',
                parent_field=models.Comment._meta.get_field('content_type'),
            )
        }

class CommentAdmin(ModelAdminMixin, admin.ModelAdmin):
    form = CommentForm
    fields = ['content_type','object_id']
admin.site.register(models.Comment, CommentAdmin)