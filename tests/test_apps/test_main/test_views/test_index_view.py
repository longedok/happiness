from django.test import Client


def test_main_page(client: Client, main_heading: str) -> None:
    """This test ensures that main page works."""
    response = client.get('/')

    assert response.status_code == 200
    assert main_heading in str(response.content)
