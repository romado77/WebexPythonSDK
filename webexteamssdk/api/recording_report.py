# -*- coding: utf-8 -*-
"""Webex Teams Recordings API wrapper.

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

from past.builtins import basestring

from webexteamssdk.generator_containers import generator_container
from webexteamssdk.restsession import RestSession
from webexteamssdk.utils import check_type, dict_from_items_with_values

API_ENDPOINT = "recordingReport"
OBJECT_TYPE = "recording_report"


class RecordingReportAPI(object):
    """Webex Teams Recording report API.

    Wraps the Webex Teams Recording report API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory):
        """Init a new RecordingReportAPI object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Webex Teams service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)
        super(RecordingReportAPI, self).__init__()
        self._session = session
        self._object_factory = object_factory

    @generator_container
    def access_summary(
        self,
        max=None,
        _from=None,
        to=None,
        hostEmail="all",
        siteUrl=None,
        **request_parameters,
    ):
        """Lists recording audit report summary.
        You can specify a date range, a parent meeting ID and the maximum number of recordings to return.

        Only recordings of meetings hosted by or shared with the authenticated user will be listed.
        The list returned is sorted in descending order by the date and time that the recordings were created.

        This method supports Webex Teams's implementation of RFC5988 Web
        Linking to provide pagination support.  It returns a generator
        container that incrementally yields all recordings returned by the
        query.  The generator will automatically request additional 'pages' of
        responses from Webex as needed until all responses have been returned.
        The container makes the generator safe for reuse.  A new API call will
        be made, using the same parameters that were specified when the
        generator was created, every time a new iterator is requested from the
        container.

        Args:
            max(int): Limit the maximum number of items returned from the Webex
                Teams service per request.
            _from(basestring): List recording audit report which occurred after a specific
                date and time.
            to(basestring): List recording audit report which occurred before a specific date
                and time.
            hostEmail(basestring): Email address of meeting host. Default is "all".
            siteUrl(basestring): URL of the Webex site which the API lists recordings from.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            GeneratorContainer: A GeneratorContainer which, when iterated,
            yields the recordings returned by the Webex Teams query.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex Teams cloud returns an error.
        """
        check_type(max, int, optional=True)
        check_type(_from, basestring, optional=True)
        check_type(to, basestring, optional=True)
        check_type(hostEmail, basestring, optional=True)
        check_type(siteUrl, basestring, optional=True)

        params = dict_from_items_with_values(
            request_parameters,
            max_recordings=max,
            _from=_from,
            to=to,
            hostEmail=hostEmail,
            siteUrl=siteUrl,
        )

        items = self._session.get_items(API_ENDPOINT + "/accessSummary", params=params)

        for item in items:
            yield self._object_factory(OBJECT_TYPE, item)

    def access_detail(
        self, recordingId, max=None, hostEmail=None, **request_parameters
    ):
        """Retrieves details for a recording audit report with a specified recording ID.

        Args:
            recordingId(basestring): The ID of the recording to be retrieved.
            max(int): Limit the maximum number of items returned from the Webex
                Teams service per request.
            hostEmail(basestring): Email address of meeting host.

        Returns:
            Recording: A RecordingReport object with the details of the requested
            recording.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex Teams cloud returns an error.

        """
        check_type(max, int, optional=True)
        check_type(recordingId, basestring)
        check_type(hostEmail, basestring, optional=True)

        params = dict_from_items_with_values(
            request_parameters,
            max=max,
            recordingId=recordingId,
            hostEmail=hostEmail,
        )

        json_data = self._session.get(API_ENDPOINT + "/accessDetail", params=params)

        return self._object_factory(OBJECT_TYPE, json_data)
