import requests
import allure


@allure.feature("用户认证")


class TestAuth:


    @allure.title("用户注册成功")
    def test_register_success(self, api_url):

        data = {
            "username":"test001",
            "password":"123456"
        }


        response = requests.post(
            api_url + "/register",
            json=data
        )


        assert response.status_code == 200



    @allure.title("用户登录成功")
    def test_login_success(self, api_url):


        data = {
            "username":"test001",
            "password":"123456"
        }


        response = requests.post(
            api_url + "/login",
            json=data
        )


        result = response.json()


        assert "access_token" in result