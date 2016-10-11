from __future__ import unicode_literals

from pyquery import PyQuery as pq

from django.db import models
from django.utils.translation import ugettext_lazy as _
from mezzanine.core.managers import SearchableManager
from mezzanine.core.models import RichText, Displayable, Slugged
from mezzanine.core.fields import RichTextField, OrderField, FileField
from mezzanine.utils.models import AdminThumbMixin, upload_to
from organization.core.models import *
from mezzanine_agenda.models import Event
from django.conf import settings
import requests

MEDIA_BASE_URL = getattr(settings, 'MEDIA_BASE_URL', 'http://medias.ircam.fr/embed/media/')


class Media(Displayable):
    """Media"""

    media_id = models.CharField(_('media id'), max_length=128)
    open_source_url = models.URLField(_('open source URL'), max_length=1024, blank=True)
    closed_source_url = models.URLField(_('closed source URL'), max_length=1024, blank=True)
    poster_url = models.URLField(_('poster'), max_length=1024, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    # objects = SearchableManager()
    search_fields = ("title",)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title

    @property
    def uri(self):
        return MEDIA_BASE_URL + self.media_id

    def get_html(self):
        r = requests.get(self.uri)
        return r.content

    def clean(self):
        super(Media, self).clean()
        self.q = pq(self.get_html())
        sources = self.q('source')
        for source in sources:
            if self.open_source_mime_type in source.attrib['type']:
                self.open_source_url = source.attrib['src']
            elif self.closed_source_mime_type in source.attrib['type']:
                self.closed_source_url = source.attrib['src']
        video = self.q('video')
        if len(video):
            if 'poster' in video[0].attrib.keys():
                self.poster_url = video[0].attrib['poster']


class Audio(Media):
    """Audio"""

    open_source_mime_type = 'audio/ogg'
    closed_source_mime_type = 'audio/mp4'
    category = models.ForeignKey('MediaCategory', verbose_name=_('category'), related_name='audios', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = _('audio')
        ordering = ('-created_at',)

    def get_absolute_url(self):
        return reverse("festival-audio-detail", kwargs={"slug": self.slug})


class Video(Media):
    """Video"""

    open_source_mime_type = 'video/webm'
    closed_source_mime_type = 'video/mp4'
    category = models.ForeignKey('MediaCategory', verbose_name=_('category'), related_name='videos', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = _('video')
        ordering = ('-created_at',)

    def get_absolute_url(self):
        return reverse("festival-video-detail", kwargs={"slug": self.slug})


class MediaCategory(Slugged, Description):
    """Media Category"""

    class Meta:
        verbose_name = _('media category')
        verbose_name_plural = _('media categories')

    def count(self):
        try:
            return self.videos.published().count()+1
        except:
            return self.audios.published().count()+1


class Playlist(Slugged, Description):
    """(Playlist description)"""

    audios = models.ManyToManyField('Audio', verbose_name=_('audios'), related_name='playlists', blank=True)

    def __str__(self):
        return self.title
