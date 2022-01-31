#!/usr/bin/env python3

import csv
import logging

import mock_service

REPORT_FILENAME = "TC_Finance_Report.csv"
REJECT_DEST_EMAIL = "feed@marketdial.com"


def send_report(db_client, rejects=False):

    x = db_client["client_collection"]
    y = x["tc_topps"]
    z = y["items_sold"]

    if rejects:
        f = "TC_Reject_Report.csv"
        email = REJECT_DEST_EMAIL
    else:
        email = "tc@gmail.com"
        f = REPORT_FILENAME

    logging.info(f"Starting tc_topps {f}")

    for rw in z:
        rw["name"] = mock_service.SKU_MAP[rw["name"]]

    with open('/tmp/' + f, "w") as csv_file:
        w = csv.DictWriter(csv_file, fieldnames=["name", "price", "quantity_sold"])
        w.writeheader()
        w.writerows(z)

    link = mock_service.get_report_link(filename=f)

    if rejects:
        sub = f"tc_topps rejected properties file."
        cont = (
            f"Here is the rejected properties file link: {link}"
        )
    else:
        sub = f"tc_topps report file."
        cont = f"Here is the Report file link: {link}"
    res = mock_service.email_file_link(email, sub, cont)
    logging.info(f"Successfully reported tc_topps {f}")

    return res
