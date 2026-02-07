##раз есть фикстура, которая и так обращается к GetPostsAPI, то тогда и не надо тут ниче импортировать
##просто пишем ассерты

def test_get_posts(get_posts):
    response = get_posts.get_all_posts()

    assert response.status_code == 200

    data = response.json()

    assert data is not None

    first_item = data[0]

    assert 'userId' in first_item
    assert 'id' in first_item
    assert 'title' in first_item
    assert 'body' in first_item

    assert isinstance(first_item['userId'],int)
    assert isinstance(first_item['id'],int)
    assert isinstance(first_item['title'],str)
    assert isinstance(first_item['body'],str)

    assert first_item['userId'] is not None
    assert first_item['userId'] > 0