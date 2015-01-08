from django.views import generic


__all__ = ['SearchView']


class SearchView(generic.edit.FormMixin, generic.ListView):
    """
    """

    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        self.object_list = None
        if request.GET:
            form_class = self.get_form_class() 
            form = self.get_form(form_class)
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
        else:
            return self.render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        if 'form' in kwargs:
            form = kwargs['form']
        else:
            form_class = self.get_form_class()
            form = self.get_form(form_class)
        context = super().get_context_data(form=form)
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.GET:
            kwargs['data'] = self.request.GET
        return kwargs

    def form_valid(self, form):
        self.cleaned_data = form.cleaned_data
        self.queryset = self.search(self.cleaned_data)
        return super().get(self.request, self.args, self.kwargs)

    def search(self, cleaned_data):
        """
        Receives the form's cleaned data.
        Returns a queryset or iterable.
        """
        queryset = None
        try:
            queryset = self.model._default_manager.search(**cleaned_data)
        except:
            queryset = self.get_queryset()
        return queryset
