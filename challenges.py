#!/usr/bin/env python3


import mock_service

import csv
REJECT_DEST_EMAIL = "feed@marketdial.com"


def send_report(db_client, rejects=False):



    if rejects:
        f = "TC_Reject_Report.csv"
        email = REJECT_DEST_EMAIL
    else:
        email = "tc@gmail.com"
        f = "TC_Finance_Report.csv"
    x = db_client["client_collection"]
    rep = x["tc_topps"]
    import logging
    logging.info(f"Starting tc_topps {f}")

    z = rep["items_sold"]
    for rw in z:
        rw["name"] = mock_service.SKU_MAP[rw["name"]]
    with open('/tmp/' + f, "w") as f2:
        w = csv.DictWriter(f2, fieldnames=["name", "price", "quantity_sold"])
        w.writeheader()
        w.writerows(z)

    link = mock_service.get_report_link(filename=f)
    if rejects == True:
        sub = f"tc_topps rejected properties file."
        cont = (
            f"Here is the rejected properties file link: {link}"
        )
    else:
        sub = f"tc_topps report file."
        cont = f"Here is the Report file link: {link}"
    res = mock_service.email_file_link(email, sub, cont)
    logging.info(f"Successfully reported tc_topps {f}")

    if res == True:
        return True
    else:
        return False
