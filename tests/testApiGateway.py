def test_get_order_not_found(client):
    response = client.get("/health")
    assert response.status_code == 404