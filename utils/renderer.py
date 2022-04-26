#! /usr/bin/env python3.9
# -*- coding: utf8 -*-
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


class FileRenderMixin(object):
    """
    Mixin which allows the override of the filename being
    passed back to the user when the spreadsheet is downloaded.
    """

    filename = "download"
    file_format = ('csv', 'xlsx')

    def get_filename(self, request=None, *args, **kwargs):
        """
        Returns a custom filename for the spreadsheet.
        """
        return self.filename

    def finalize_response(self, request, response, *args, **kwargs):
        """
        Return the response with the proper content disposition and the customized
        filename instead of the browser default (or lack thereof).
        """
        response = super(FileRenderMixin, self).finalize_response(
            request, response, *args, **kwargs
        )
        if (
            isinstance(response, Response)
            and response.accepted_renderer.format in (self.file_format)
        ):
            response["content-disposition"] = "attachment; filename={}".format(
                self.get_filename(request=request, *args, **kwargs),
            )
        return response


class JSONResponseRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = renderer_context['response']

        if response.exception:
            resp = data
        else:
            resp = {
                'success': True,
                'data': data,
            }
        return super(JSONResponseRenderer, self).render(resp, accepted_media_type, renderer_context)
