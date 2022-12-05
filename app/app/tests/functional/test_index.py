def test_index(client):
    response = client.get("/", follow_redirects=True)
    assert response.status_code == 200
    assert "Hello DHBW" in response.get_data(as_text=True)

def test_hello(client):
    response = client.post(
        "/hello",
        data = dict(name="Bernd"),
        follow_redirects = True
    )
    assert response.status_code == 200
    assert "Hello Bernd" in response.get_data(as_text=True)
    #assert response.imageLoaded

