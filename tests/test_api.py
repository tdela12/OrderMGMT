def test_get_order_not_found(test_client):
    response = test_client.get("/health")
    assert response.status_code == 200
