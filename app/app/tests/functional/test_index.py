def test_index_page_loaded(client):
    response = client.get("/", follow_redirects=True)
    assert response.status_code is 200
    assert "Hello DHBW" in response.get_data(as_text=True)

def test_hello_page_loaded_with_name(client):
    response = client.post(
        "/hello",
        data = dict(name="Bernd"),
        follow_redirects = True
    )
    assert response.status_code is 200
    assert "Hello Bernd" in response.get_data(as_text=True)

def test_hello_page_loaded_without_name(client):
    response = client.post(
        "/hello",
        follow_redirects = True
    )
    assert response.status_code is 200
    assert response.request.path == "/hello"
    assert "Hello DHBW" in response.get_data(as_text=True)

def test_favicon_loaded(client):
    response = client.get("/favicon.ico")
    assert response.status_code is 200
    assert response.content_type == "image/vnd.microsoft.icon"


