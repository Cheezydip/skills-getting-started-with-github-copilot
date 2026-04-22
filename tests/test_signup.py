def test_signup_adds_participant(client):
    response = client.post(
        "/activities/Chess Club/signup",
        params={"email": "newstudent@mergington.edu"},
    )
    activities_response = client.get("/activities")
    participants = activities_response.json()["Chess Club"]["participants"]

    assert response.status_code == 200
    assert response.json()["message"] == "Signed up newstudent@mergington.edu for Chess Club"
    assert "newstudent@mergington.edu" in participants


def test_signup_rejects_duplicate_participant(client):
    response = client.post(
        "/activities/Chess Club/signup",
        params={"email": "michael@mergington.edu"},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up for this activity"


def test_signup_rejects_unknown_activity(client):
    response = client.post(
        "/activities/Unknown Club/signup",
        params={"email": "newstudent@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"