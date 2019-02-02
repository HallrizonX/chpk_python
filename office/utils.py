from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import *



class ObjectDetailMixin:
    model = None
    template = None
    # post, tag
    queryType = None

    def get(self, request, slug):
        if self.queryType == "post":
            # Get detail page to post
            obj = get_object_or_404(self.model, slug__iexact=slug)
            return render(request, self.template, context={self.model.__name__.lower(): obj})
        elif self.queryType == "tag":
            # Get page with list posts of same tag (slug)
            obj = get_list_or_404(self.model, tags__slug__iexact=slug)
            return render(request, self.template, context={"posts": obj})
        else:
            obj = get_object_or_404(self.model, slug=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})
