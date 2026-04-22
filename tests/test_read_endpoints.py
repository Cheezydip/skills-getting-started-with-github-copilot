def test_root_redirects_to_static_index(client):
    response = client.get("/", follow_redirects=False)

    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"


def test_get_activities_returns_expected_structure(client):
    response = client.get("/activities")
    payload = response.json()

    assert response.status_code == 200
    assert isinstance(payload, dict)
    assert "Chess Club" in payload
    assert set(payload["Chess Club"].keys()) == {
        "description",
        "schedule",
        "max_participants",
        "participants",
    }