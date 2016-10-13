from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic.base import View
from django.views.generic import DetailView, ListView, TemplateView
from django.apps import apps
from django.utils.translation import ugettext_lazy as _
from django.http import QueryDict
from mezzanine.conf import settings
from mezzanine.utils.views import paginate
from organization.core.models import *


class SlugMixin(object):

    def get_object(self):
        objects = self.model.objects.all()
        return get_object_or_404(objects, slug=self.kwargs['slug'])


# class CustomDisplayableView(SlugMixin, DetailView):
#
#     model = CustomDisplayable


class CustomSearchView(TemplateView):

    template_name='search_results.html'


    def get(self, request, *args, **kwargs):

        """
        Display search results. Takes an optional "contenttype" GET parameter
        in the form "app-name.ModelName" to limit search results to a single model.
        """
        context = super(CustomSearchView, self).get_context_data(**kwargs)
        query = request.GET.get("q", "")
        page = request.GET.get("page", 1)
        per_page = settings.SEARCH_PER_PAGE
        max_paging_links = settings.MAX_PAGING_LINKS
        try:
            parts = request.GET.get("type", "").split(".", 1)
            search_model = apps.get_model(*parts)
            search_model.objects.search  # Attribute check
        except (ValueError, TypeError, LookupError, AttributeError):
            search_model = Displayable
            search_type = _("Everything")
        else:
            search_type = search_model._meta.verbose_name_plural.capitalize()

        results = search_model.objects.search(query, for_user=request.user)
        print("----------------------------")
        print(results)
        print("----------------------------")
        # count objects
        filter_dict = dict()
        for result in results:

            classname = result.__class__.__name__
            app_label = result._meta.app_label

            # aggregate all Page types : CustomPage, TeamPage, Topic etc...
            if result._meta.get_parent_list() :
                parent_class = result._meta.get_parent_list()[0]

                if parent_class.__name__ == 'Page':
                    classname = parent_class.__name__
                    app_label = parent_class._meta.app_label
                elif "Video" in parent_class.__name__:
                    classname = "Video"
                    app_label = parent_class._meta.app_label
                elif "Audio" in parent_class.__name__:
                    classname = "Audio"
                    app_label = parent_class._meta.app_label

            if classname in filter_dict:
                filter_dict[classname]['count'] += 1
            else:
                filter_dict[classname] = {'count' : 1}
                filter_dict[classname].update({'verbose_name' : classname})
                filter_dict[classname].update({'app_label' : app_label})



        # get url param
        current_query = QueryDict(mutable=True)
        current_query = request.GET.copy()

        # generate filter url
        for key, value in filter_dict.items():
            current_query['type'] = value['app_label']+'.'+key
            filter_dict[key].update({'url' : request.path+"?"+current_query.urlencode(safe='/')})

        # pagination
        paginated = paginate(results, page, per_page, max_paging_links)

        # context
        context = {"query": query, "results": paginated,
                   "search_type": search_type}

        # cancel filter url
        if request.GET.__contains__('type'):
            previous_query = QueryDict(mutable=True)
            previous_query = request.GET.copy()
            previous_query.pop('type')
            context['cancel_filter_url'] = '?'+previous_query.urlencode(safe='/')

        context['filter_dict'] = filter_dict
        # context.update(extra_context or {})
        return self.render_to_response(context)
