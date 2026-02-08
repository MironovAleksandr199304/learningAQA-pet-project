from assertions.assertions import assert_post_item

def test_get_post(get_posts):
    response = get_posts.get_post(1)
    assert response.status_code == 200

    data = response.json()
    assert_post_item(data)