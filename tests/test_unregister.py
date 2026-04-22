def test_unregister_removes_participant(client):
    response = client.delete("/activities/Chess Club/participants/michael@mergington.edu")
    activities_response = client.get("/activities")
    participants = activities_response.json()["Chess Club"]["participants"]

    assert response.status_code == 200
    assert response.json()["message"] == "Unregistered michael@mergington.edu from Chess Club"
    assert "michael@mergington.edu" not in participants


def test_unregister_rejects_unknown_activity(client):
    response = client.delete("/activities/Unknown Club/participants/michael@mergington.edu")

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_rejects_non_registered_student(client):
    response = client.delete("/activities/Chess Club/participants/notregistered@mergington.edu")

    assert response.status_code == 404
    assert response.json()["detail"] == "Student not registered for this activity"