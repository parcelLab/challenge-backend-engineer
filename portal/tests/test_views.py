from django.test import Client


def test_lookup_page_renders() -> None:
    client = Client()
    response = client.get("/returns/")
    assert response.status_code == 200
    assert b"Returns Portal" in response.content


def test_submit_lookup_redirects_to_order() -> None:
    client = Client()
    response = client.post(
        "/returns/lookup",
        {"order_number": "RMA-1001", "email_or_zip": "alex@example.com"},
    )
    assert response.status_code == 302
    assert response["Location"].endswith("/returns/RMA-1001")


def test_order_details_renders_items() -> None:
    client = Client()
    response = client.get("/returns/RMA-1001")
    assert response.status_code == 200
    assert b"T-Shirt Black" in response.content
    assert b"Returns E-Book" in response.content
