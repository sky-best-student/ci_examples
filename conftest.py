import pytest
import os
from dotenv import load_dotenv
from config import BASE_URL
from api.project_api import ProjectAPI
from api.departments_api import DepartmentsAPI


load_dotenv()


@pytest.fixture
def auth_headers():
    my_token = os.getenv("KEY")
    return {
        "Authorization": f"Bearer {my_token}",
        "Content-Type": "application/json",
    }


@pytest.fixture
def project_api():
    return ProjectAPI(base_url=BASE_URL)


@pytest.fixture
def departments_api():
    return DepartmentsAPI(base_url=BASE_URL)
