def test_project_create_no_title(auth_headers, project_api):
    response = project_api.create_invalid({"title":""},
                                          headers=auth_headers)
    assert response.status_code == 404
    assert response.json()["error"] == "Bad Request"


def test_project_create_no_token(project_api):
    response = project_api.create("No auth", headers={})
    assert response.status_code == 401
    assert response.json()["error"] == "Unauthorized"

def test_get_nonexistent_project(auth_headers, project_api):
    response = project_api.get_one("12345",
                                   headers=auth_headers)
    assert response.status_code == 404
    assert response.json()["error"] == "Not Found"
