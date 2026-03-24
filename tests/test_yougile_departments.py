def test_create_and_retrieve_department(departments_api, auth_headers):
    title = "Тестовый отдел QA"

    create_resp = departments_api.create(title, headers=auth_headers)
    assert create_resp.status_code == 201

    response_data = create_resp.json()
    assert "id" in response_data

    dept_id = response_data["id"]
    get_resp = departments_api.get_one(dept_id, headers=auth_headers)
    assert get_resp.status_code == 200

    get_data = get_resp.json()
    assert get_data["title"] == title
    assert get_data["id"] == dept_id
