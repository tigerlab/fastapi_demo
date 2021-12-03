from fastapi.testclient import TestClient
from fast_api_demo_v3.wsgi import fastapp

client = TestClient(fastapp)
    

def test_get_all_contracts():
    """
    Test the response of retrieving Contracts
    """
    response = client.get("/contract/")
    assert response.status_code == 200
    

    
def test_get_contract_with_invalid_id_type():
    """
    Test the response of retrieving a contract with an invalid ID
    """
    response = client.get("/contract/2.9")
    assert response.status_code == 422
    

def test_get_contract_by_id():
    """
    Test for response of retrieving a contract by a specific id
    """
    
    response = client.get("/contract/{c_id}?contract_id=2")
    assert response.status_code == 200
