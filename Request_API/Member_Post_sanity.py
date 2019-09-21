import requests, json
import Configuration

# Token Generation Code:


token_url = "https://accounts-devsp.zeomega.org/oauth2/token"
data = {'grant_type': 'password', 'username': 'zeomega.com/zeadmin', 'password': 'Jiva@123', 'scope': 'mgc'}
header = {'Authorization': 'Basic MkQ1eVN2eWw1aFE1T2Q3ampCT2RscEw3bldFYToxazRDVzE5dVE2dVF5ZjBlTFZQQnQ2ZDR1WXdh',
'Content_type': 'application/json'}
access_token = requests.post(token_url, data=data, headers=header)
print(access_token)
tok = access_token.json()['access_token']
print(access_token.headers)
token1 = 'Bearer ' + tok

def setup():
    headers = {'accept': 'application/json', 'Authorization': token1, 'Content-Type': 'application/json'}


def dup_mbr_chk(set_up):

    contents=Configuration.f1_dup_MBR_CHK.read()
    # print(contents)
    json_response = requests.post("https://api-devsp.zeomega.org/members/v1.1", data=contents, headers=headers,
                                  indent=4)
    print(json_response.text)
    assert json_response.status_code == 404



def invalid_GENDER_CD(set_up):

    contents = Configuration.f2_invalid_GENDER_CD.read();
# print(contents)

    json_response = requests.post("https://api-devsp.zeomega.org/members/v1.1", data=contents, headers=headers,
indent=4)
    print(json_response.text)
    assert json_response.status_code == 404


def invalid_COVERAGE_LEVEL_CD(set_up):

    contents = Configuration.f3_invalid_COVERAGE_LEVEL_CD.read();
# print(contents)

    json_response = requests.post("https://api-devsp.zeomega.org/members/v1.1", data=contents, headers=headers,
indent=4)
    print(json_response.text)
    assert json_response.status_code == 404


def invalid_COVERAGE_STATUS_CD(set_up):

    contents = Configuration.f4_invalid_COVERAGE_STATUS_CD.read();
# print(contents)

    json_response = requests.post("https://api-devsp.zeomega.org/members/v1.1", data=contents, headers=headers,
indent=4)
    print(json_response.text)
    assert json_response.status_code == 404


def invalid_DEPENDENT_CD():

    contents = Configuration.f5_invalid_DEPENDENT_CD.read();
# print(contents)

    json_response = requests.post("https://api-devsp.zeomega.org/members/v1.1", data=contents, headers=headers,
indent=4)
    print(json_response.text)
    assert json_response.status_code == 404


def invalid_FUNDING_ARRANGEMENT_CD():

    contents = Configuration.f6_invalid_FUNDING_ARRANGEMENT_CD.read();
# print(contents)

    json_response = requests.post("https://api-devsp.zeomega.org/members/v1.1", data=contents, headers=headers,
indent=4)
    print(json_response.text)
    assert json_response.status_code == 404


def invalid_GROUP_ID():

    contents = Configuration.f7_invalid_GROUP_ID.read();
# print(contents)

    json_response = requests.post("https://api-devsp.zeomega.org/members/v1.1", data=contents, headers=headers,
indent=4)
    print(json_response.text)
    assert json_response.status_code == 404


def invalid_PRODUCT_TYPE_CD():

    contents = Configuration.f8_invalid_PRODUCT_TYPE_CD.read();
# print(contents)

    json_response = requests.post("https://api-devsp.zeomega.org/members/v1.1", data=contents, headers=headers,
indent=4)
    print(json_response.text)
    assert json_response.status_code == 404


def invalid_STATE_CD():

    contents = Configuration.f9_invalid_STATE_CD.read();
# print(contents)

    json_response = requests.post("https://api-devsp.zeomega.org/members/v1.1", data=contents, headers=headers,
indent=4)
    print(json_response.text)
    assert json_response.status_code == 404


def invalid_DATA_SOURCE_CD():
    contents = Configuration.f10_invalid_DATA_SOURCE_CD.read();
# print(contents)

    json_response = requests.post("https://api-devsp.zeomega.org/members/v1.1", data=contents, headers=headers,
indent=4)
    print(json_response.text)
    assert json_response.status_code == 404


def invalid_ETHNICITY_CD():

    contents = Configuration.f11_invalid_ETHNICITY_CD.read();
# print(contents)

    json_response = requests.post("https://api-devsp.zeomega.org/members/v1.1", data=contents, headers=headers,
indent=4)
    print(json_response.text)
    assert json_response.status_code == 404


def invalid_MEMBER_LANGUAGE_CD():

    contents = Configuration.f12_invalid_MEMBER_LANGUAGE_CD.read();
# print(contents)

    json_response = requests.post("https://api-devsp.zeomega.org/members/v1.1", data=contents, headers=headers,
indent=4)
    print(json_response.text)
    assert json_response.status_code == 404


def invalid_SUFFIX_CD():

# print(contents)
    contents = Configuration.f13_invalid_SUFFIX_CD.read();
    json_response = requests.post("https://api-devsp.zeomega.org/members/v1.1", data=contents, headers=headers,
indent=4)
    print(json_response.text)
    assert json_response.status_code == 404


def invalid_RACE_CD():

# print(contents)
    contents = Configuration.f14_invalid_RACE_CD.read();
    json_response = requests.post("https://api-devsp.zeomega.org/members/v1.1", data=contents, headers=headers,
indent=4)
    print(json_response.text)
    assert json_response.status_code == 404


def invalid_COUNTRY_CD():
    contents = Configuration.f15_invalid_COUNTRY_CD.read();
# print(contents)

    json_response = requests.post("https://api-devsp.zeomega.org/members/v1.1", data=contents, headers=headers,
indent=4)
    print(json_response.text)
    assert json_response.status_code == 404


def invalid_PHONE_TYPE_CD():
    contents = Configuration.f16_invalid_PHONE_TYPE_CD.read();
# print(contents)

    json_response = requests.post("https://api-devsp.zeomega.org/members/v1.1", data=contents, headers=headers,
indent=4)
    print(json_response.text)
    assert json_response.status_code == 404


