from rest_framework import viewsets

import pdb

class MultiSerializerReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    serializers = { 
        'default': None,
    }
    def get_serializer_class(self):
        return self.serializers.get(self.action,
                    self.serializers.get('default'))
