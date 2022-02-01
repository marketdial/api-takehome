SKU_MAP = {"48052": "TC Tuggers"}
MOCK_LINK = "mock_link"


def email_file_link(dest_email, subject, mail_content_text):
    if (
        subject != "tc_topps rejected properties file."
        and subject != f"tc_topps report file."
    ):
        raise ValueError(f"Invalid subject: {subject}")

    if (
        mail_content_text != f"Here is the rejected properties file link: {MOCK_LINK}"
        and mail_content_text != f"Here is the Report file link: {MOCK_LINK}"
    ):
        raise ValueError(f"Invalid con: {mail_content_text}")

    if dest_email != "feed@marketdial.com" and dest_email != "tc@gmail.com":
        raise ValueError(f"Invalid email: {dest_email}")

    return True


def get_report_link(filename):
    if filename != "TC_Reject_Report.csv" and filename != "TC_Finance_Report.csv":
        raise ValueError(f"Invalid filename {filename}")
    return MOCK_LINK
