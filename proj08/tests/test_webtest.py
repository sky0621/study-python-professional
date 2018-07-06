
def test_it():
    from webtest import TestApp
    import proj08.tests.app
    app = TestApp(proj08.tests.app)
    res = app.get('/')
    assert "Hello" in res
