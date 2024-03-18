from fastapi.testclient import TestClient

from app.core.config import settings


def test_test_two_list_sum_api_successful(client: TestClient):
    """
    GIVEN a FastAPI app client and input parameter that are known to be successfully calculated
    WHEN the 'recursive' endpoint is requested (POST) with those known parameters
    THEN check if the response is valid
    """

    data = {"list_a": [3, 4, 6], "list_b": [3, 4, 6], "target": 10}

    response = client.post(f"{settings.API_V1_STR}/two-list-sum/optimized", json=data)

    assert 200 <= response.status_code < 300
    result = response.json()
    assert result == True


def test_test_two_list_sum_api_unsuccessful(client: TestClient):
    """
    GIVEN a FastAPI app client and input parameter that are known to be successfully calculated
    WHEN the 'recursive' endpoint is requested (POST) with those known parameters
    THEN check if the response is valid
    """

    data = {"list_a": [3, 4, 6], "list_b": [3, 4, 6], "target": 14}

    response = client.post(f"{settings.API_V1_STR}/two-list-sum/optimized", json=data)

    assert 200 <= response.status_code < 300
    result = response.json()
    assert result == False


def test_test_two_list_sum_optimized_api_successful(client: TestClient):
    """
    GIVEN a FastAPI app client and input parameter that are known to be successfully calculated
    WHEN the 'recursive' endpoint is requested (POST) with those known parameters
    THEN check if the response is valid
    """

    data = {"list_a": [3, 4, 6], "list_b": [3, 4, 6], "target": 10}

    response = client.post(f"{settings.API_V1_STR}/two-list-sum/unoptimized", json=data)

    assert 200 <= response.status_code < 300
    result = response.json()
    assert result == True


def test_test_two_list_sum_optimized_api_unsuccessful(client: TestClient):
    """
    GIVEN a FastAPI app client and input parameter that are known to be successfully calculated
    WHEN the 'recursive' endpoint is requested (POST) with those known parameters
    THEN check if the response is valid
    """

    data = {"list_a": [3, 4, 6], "list_b": [3, 4, 6], "target": 14}

    response = client.post(f"{settings.API_V1_STR}/two-list-sum/unoptimized", json=data)

    assert 200 <= response.status_code < 300
    result = response.json()
    assert result == False
