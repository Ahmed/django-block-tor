__author__ = 'Ahmed Hassan'

from django.shortcuts import Http404
import TorCheck


class BlockTorMiddleware(object):
    @staticmethod
    def process_request(request):
        if TorCheck.is_using_tor(request.META['REMOTE_ADDR'], '80') == 0:
            raise Http404
