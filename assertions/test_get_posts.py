##раз есть фикстура, которая и так обращается к GetPostsAPI, то тогда и не надо тут ниче импортировать
##просто пишем ассерты
from assertions.assertions import assert_post_item

def test_get_posts(get_posts):

    response = get_posts.get_all_posts()
    assert response.status_code == 200

    data = response.json()
    assert data is not None

    first_item = data[0]
    assert_post_item(first_item)