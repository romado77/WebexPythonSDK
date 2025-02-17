# -*- coding: utf-8 -*-
"""Webex Teams Recording data model.

Copyright (c) 2016-2020 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from builtins import *

from webexteamssdk.utils import WebexTeamsDateTime


class RecordingBasicPropertiesMixin(object):
    """Recording basic properties"""

    @property
    def id(self):
        """The unique identifier for the recording."""
        return self._json_data.get("id")

    @property
    def meetingId(self):
        """Unique identifier for the parent ended meeting instance which the recording belongs to."""
        return self._json_data.get("meetingId")

    @property
    def scheduledMeetingId(self):
        """Unique identifier for the parent scheduled meeting which the recording belongs to."""
        return self._json_data.get("scheduledMeetingId")

    @property
    def topic(self):
        """The recording's topic."""
        return self._json_data.get("topic")

    @property
    def meetingSeriesId(self):
        """Unique identifier for the parent meeting series which the recording belongs to."""
        return self._json_data.get("meetingSeriesId")

    @property
    def createTime(self):
        """The date and time recording was created in ISO 8601 compliant format."""
        created = self._json_data.get("createTime")
        if created:
            return WebexTeamsDateTime.strptime(created)

    @property
    def timeRecorded(self):
        """The date and time recording started in ISO 8601 compliant format."""
        recorded = self._json_data.get("timeRecorded")
        if recorded:
            return WebexTeamsDateTime.strptime(recorded)

    @property
    def siteUrl(self):
        """Site URL for the recording."""
        return self._json_data.get("siteUrl")

    @property
    def downloadUrl(self):
        """The download link for recording."""
        return self._json_data.get("downloadUrl")

    @property
    def playbackUrl(self):
        """The playback link for recording."""
        return self._json_data.get("playbackUrl")

    @property
    def password(self):
        """The recording's password."""
        return self._json_data.get("password")

    @property
    def format(self):
        """The recording's file format."""
        return self._json_data.get("format")

    @property
    def serviceType(self):
        """The recording's service type."""
        return self._json_data.get("serviceType")

    @property
    def durationSeconds(self):
        """The duration of the recording, in seconds."""
        return self._json_data.get("durationSeconds")

    @property
    def sizeBytes(self):
        """The size of the recording file, in bytes."""
        return self._json_data.get("sizeBytes")

    @property
    def shareToMe(self):
        """Whether or not the recording has been shared to the current user."""
        return self._json_data.get("shareToMe")

    @property
    def integrationTags(self):
        """External keys of the parent meeting created by an integration application."""
        return self._json_data.get("integrationTags")


class RecordingReportBasicPropertiesMixin(object):
    """Recording report basic properties"""

    @property
    def recordingId(self):
        """The unique identifier for the recording."""
        return self._json_data.get("recordingId")

    @property
    def topic(self):
        """The recording's topic."""
        return self._json_data.get("topic")

    @property
    def timeRecorded(self):
        """The date and time recording started in ISO 8601 compliant format."""
        recorded = self._json_data.get("timeRecorded")
        if recorded:
            return WebexTeamsDateTime.strptime(recorded)

    @property
    def accessTime(self):
        """The date and time recording was accessed in ISO 8601 compliant format."""
        recorded = self._json_data.get("accessTime")
        if recorded:
            return WebexTeamsDateTime.strptime(recorded)

    @property
    def siteUrl(self):
        """Site URL for the recording."""
        return self._json_data.get("siteUrl")

    @property
    def hostEmail(self):
        """Email address for the meeting host."""
        return self._json_data.get("hostEmail")

    @property
    def viewCount(self):
        """The number of times the recording was viewed."""
        return self._json_data.get("viewCount")

    @property
    def downloadCount(self):
        """The number of times the recording was downloaded."""
        return self._json_data.get("downloadCount")

    @property
    def email(self):
        """Email address for the user who viewed or downloaded the recording."""
        return self._json_data.get("email")

    @property
    def format(self):
        """The recording's file format."""
        return self._json_data.get("format")

    @property
    def viewed(self):
        """Whether or not the recording was viewed."""
        return self._json_data.get("viewed")

    @property
    def downloaded(self):
        """Whether or not the recording was downloaded."""
        return self._json_data.get("downloaded")
