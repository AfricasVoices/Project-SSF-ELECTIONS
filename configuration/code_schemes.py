import json

from core_data_modules.data_models import CodeScheme


def _open_scheme(filename):
    with open(f"code_schemes/{filename}", "r") as f:
        firebase_map = json.load(f)
        return CodeScheme.from_firebase_map(firebase_map)


class CodeSchemes(object):
    S01E01 = _open_scheme("s01e01.json")
    S01E02 = _open_scheme("s01e02.json")
    S01E03 = _open_scheme("s01e03.json")
    S01E04 = _open_scheme("s01e04.json")
    S01E05 = _open_scheme("s01e05.json")
    S01E06 = _open_scheme("s01e06.json")
    S01E07 = _open_scheme("s01e07.json")

    AGE = _open_scheme("age.json")
    AGE_CATEGORY = _open_scheme("age_category.json")
    RECENTLY_DISPLACED = _open_scheme("recently_displaced.json")
    HOUSEHOLD_LANGUAGE = _open_scheme("household_language.json")
    GENDER = _open_scheme("gender.json")

    SOMALIA_OPERATOR = _open_scheme("somalia_operator.json")
    SOMALIA_DISTRICT = _open_scheme("somalia_district.json")
    MOGADISHU_SUB_DISTRICT = _open_scheme("mogadishu_sub_district.json")
    SOMALIA_REGION = _open_scheme("somalia_region.json")
    SOMALIA_STATE = _open_scheme("somalia_state.json")
    SOMALIA_ZONE = _open_scheme("somalia_zone.json")

    WS_CORRECT_DATASET_SCHEME = _open_scheme("ws_correct_dataset.json")

    FACEBOOK_S01E01 = _open_scheme("facebook_s01e01.json")
    FACEBOOK_S01E02 = _open_scheme("facebook_s01e02.json")
    FACEBOOK_S01E03 = _open_scheme("facebook_s01e03.json")
    FACEBOOK_S01E04 = _open_scheme("facebook_s01e04.json")
    FACEBOOK_S01E05 = _open_scheme("facebook_s01e05.json")
    FACEBOOK_S01E06 = _open_scheme("facebook_s01e06.json")
    FACEBOOK_S01E07 = _open_scheme("facebook_s01e07.json")


    FACEBOOK_COMMENT_REPLY_TO = _open_scheme("facebook_comment_reply_to.json")
    FACEBOOK_POST_TYPE = _open_scheme("facebook_post_type.json")
