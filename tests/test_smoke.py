import app


def test_index_returns_error_without_db():
    client = app.app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert "Error conectando a la base de datos" in resp.get_data(as_text=True)