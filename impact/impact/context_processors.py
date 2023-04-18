from impact.settings import CRISP_WEBSITE_ID


def crisp_website_id(request):
    return {"CRISP_WEBSITE_ID": CRISP_WEBSITE_ID}
