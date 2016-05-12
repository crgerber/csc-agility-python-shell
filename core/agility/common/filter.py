from core.restclient.connection import RESTException

class InstanceFilter:
    def __init__(self,agility_model):
        self.agility_model = agility_model
    def UNAUTHORIZED(self,instance):
        not_filtered = True
        try:
            template = self.agility_model.template.getTemplate(instance.template.id)
            container = self.agility_model.container.getContainer(template.project.id)
            not_filtered = not container.uuid == "#UNAUTH_INSTANCES#"
        except RESTException as rest_exception:
            if self.retry and 404 == rest_exception.info.get('code'):
                not_filtered = False
            else:
                raise
        return not_filtered

