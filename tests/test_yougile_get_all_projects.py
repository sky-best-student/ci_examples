from models import ProjectsList


def test_get_all_projects(project_api, auth_headers):
    response = project_api.get_all(headers=auth_headers)
    assert response.status_code == 200

    data = response.json()
    project_list = ProjectsList(**data)

    assert len(project_list.content) > 0
