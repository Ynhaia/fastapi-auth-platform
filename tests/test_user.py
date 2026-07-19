import requests
import allure


@allure.feature("用户信息接口")
class TestUser:


    def get_token(self, api_url):

        data = {
            "username":"test001",
            "password":"123456"
        }


        response = requests.post(
            api_url + "/login",
            json=data
        )


        return response.json()["access_token"]



    @allure.title("携带Token获取用户信息")
    def test_get_user_info(self, api_url):


        token = self.get_token(api_url)


        headers = {

            "Authorization":
            f"Bearer {token}"

        }


        response = requests.get(
            api_url + "/user/info",
            headers=headers
        )


        result = response.json()


        assert response.status_code == 200

        assert "username" in result



    @allure.title("无Token访问用户信息失败")
    def test_get_user_info_without_token(self, api_url):


        response = requests.get(
            api_url + "/user/info"
        )


        assert response.status_code == 403