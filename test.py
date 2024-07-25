from main import store_password, register_user, get_password, update_password, delete_password

def test_register_user():
    assert register_user("john123", "password123") == 0
    assert register_user("mihir", "pass") == 0
    assert register_user("mihir@123_576", "thisIsA3434WiresdPassword90__") == 0

def test_store_password():
    assert store_password("john123", 'google', 'abc') == 'stored'
    assert store_password("mihir", 'harvard', '35789512357') == 'stored'
    assert store_password("maiden", 'abc', '35789512357') == None

def test_get_password():
    assert get_password("john123", 'google') == 'abc'
    assert get_password("mihir", 'harvard') == '35789512357'
    assert get_password("john123", 'abc') == None

def test_update_password():
    assert update_password("john123", 'google', 'pass1') == 'pass1'
    assert update_password("mihir", 'harvard', 'pass2') == 'pass2'
    assert update_password("john123", 'abc', 'pass1') == None

def test_delete_password():
    assert delete_password("john123", 'google') == 1
    assert delete_password("mihir", 'harvard') == 1
    assert delete_password("john123", 'abc') == None


def main():
    test_register_user()
    test_store_password()
    test_get_password()
    test_update_password()
    test_delete_password()

if __name__ == "__main__":
    main()
