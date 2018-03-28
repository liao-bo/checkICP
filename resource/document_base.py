from mongoengine import Document as Mongo_Document
from mongoengine import EmbeddedDocument as Mongo_EmbeddedDocument

from resource.connect import CheckICPDB


# checkICPDB = CheckICPDB()
# checkICPdb.build_connection()


class Document(Mongo_Document):
    meta = {
        'allow_inheritance': True,
        'abstract': True
    }

    def to_dict(self):
        data = {}
        for f in self._fields_ordered:
            v = getattr(self, f)
            if isinstance(v, Mongo_Document):
                v = getattr(v, 'id')
            elif isinstance(v, Mongo_EmbeddedDocument):
                v = v.to_dict()
            elif isinstance(v, list) and v:
                if isinstance(v[0], Mongo_EmbeddedDocument):
                    v = [sub.to_dict() for sub in v]
                elif isinstance(v[0], Mongo_Document):
                    v = [getattr(sub, 'id') for sub in v]
            data[f] = v
        del data['_cls']
        return data

    @property
    def fields_name(self):
        return [i for i in self._fields_ordered if i != '_cls']

    # def __eq__(self, other):
    #     return self.as_dict() == other.as_dict()
    #
    # @classmethod
    # def get_field_names(cls):
    #     fields = inspect.getargspec(cls.__init__)[0]
    #     return set(fields) - set(["self"])

    # def update(self, **kwargs):
    #     kwargs['update_time'] = datetime.utcnow()
    #     print(kwargs)
    #     super.update(**kwargs)


class EmbeddedDocument(Mongo_EmbeddedDocument):
    meta = {
        'allow_inheritance': True,
        'abstract': True
    }

    def to_dict(self):
        data = {}
        for f in self._fields_ordered:
            v = getattr(self, f)
            data[f] = v
        del data['_cls']
        return data
