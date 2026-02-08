def assert_post_item(post):

    assert post is not None

    assert 'userId' in post
    assert 'id' in post
    assert 'title' in post
    assert 'body' in post

    assert isinstance(post['userId'], int)
    assert isinstance(post['id'], int)
    assert isinstance(post['title'], str)
    assert isinstance(post['body'], str)
    assert post['userId'] > 0