def test_project_create_update(auth_headers, project_api):
    title = "Тестовый проект"
    response = project_api.create(title=title, headers=auth_headers)
    assert response.status_code == 201
    assert "id" in response.json()
    assert isinstance(response.json()["id"], str)
    assert "application/json" in response.headers["Content-Type"]
    assert response.elapsed.total_seconds() < 3

    project_id = response.json()["id"]

    get_response = project_api.get_one(project_id, headers=auth_headers)
    assert get_response.status_code == 200
    assert get_response.json()["title"] == title
    assert get_response.json()["id"] == project_id
    assert isinstance(get_response.json()["id"], str)
    assert "application/json" in get_response.headers["Content-Type"]

    new_title = "Удаленный проект"
    put_response = project_api.update(project_id, headers=auth_headers,
                                      title=new_title,
                                      deleted=True)
    assert put_response.status_code == 200
    assert put_response.json()["id"] == project_id
    assert isinstance(put_response.json()["id"], str)
    assert "application/json" in put_response.headers["Content-Type"]
    assert put_response.elapsed.total_seconds() < 3

    get_response_final = project_api.get_one(project_id, headers=auth_headers)
    assert get_response_final.status_code == 200
    assert get_response_final.json()["title"] == new_title
    assert get_response_final.json()["id"] == project_id
    assert isinstance(get_response_final.json()["id"], str)
    assert get_response_final.json()["deleted"] is True
    assert isinstance(get_response_final.json()["deleted"], bool)
    assert "application/json" in get_response_final.headers["Content-Type"]
