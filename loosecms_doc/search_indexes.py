from haystack import indexes
from .models import Doc


class DocIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    ctime = indexes.DateTimeField(model_attr='ctime')

    def get_model(self):
        return Doc

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.select_related().all()