from old.api_final.pages.base_api import BaseAPI


class ProjectAPI(BaseAPI):
    def __init__(self, base_url):
        super().__init__(base_url)
        self.endpoint = "projects"


    def create(self, title, headers=None):
        data = {
            "title": title
        }
        return self.post(self.endpoint, data=data, headers=headers)

    def create_invalid(self, data, headers=None):
        return self.post(self.endpoint, data=data, headers=headers)

    def get_one(self, project_id, headers=None):
        return self.get(f"{self.endpoint}/{project_id}", headers=headers)

    def get_all(self, headers=None):
        return self.get(self.endpoint, headers=headers)

    def update(self, project_id, headers=None, **kwargs):
        return self.put(f"{self.endpoint}/{project_id}",data=kwargs, headers=headers)
