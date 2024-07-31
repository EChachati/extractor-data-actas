from Acta import Acta
from db import (
    create_actas_table,
    get_all_image_urls,
    insert_acta_into_db,
    is_acta_registered,
    is_acta_registered_by_image_name,
)
from utils import extract_qr_from_image, extract_text_from_image, image_from_url

if __name__ == "__main__":
    CURRENT = 0
    MAX = 25000

    fails = []
    create_actas_table()

    for id_, url in get_all_image_urls(1330):
        CURRENT += 1
        if CURRENT == MAX:
            break
        print(id_, url)
        image_name = url.split("/")[-1]
        image = image_from_url(url)

        if is_acta_registered_by_image_name(image_name):
            print(f"Acta {image_name} already registered\n")
            continue

        try:
            acta_id, parties_votes, total_null, total_invalid = extract_qr_from_image(image)
            if is_acta_registered(acta_id):
                print(f"Acta {acta_id} already registered\n")
                continue
            state, municipality, parish = extract_text_from_image(image)

            acta = Acta(
                acta_id=acta_id,
                image_name=image_name,
                TOTAL_INVALID=total_invalid,
                TOTAL_NULL=total_null,
                STATE=state,
                MUNICIPALITY=municipality,
                PARISH=parish,
                **dict(parties_votes),
            )
            print()
            print(acta)
            print()
            insert_acta_into_db(acta)

        except IndexError:
            print("Fail to extract data from image. Added to fails list\n")
            fails.append(url)
        except Exception:
            with open("fails.txt", "a") as f:
                f.write("\n".join(fails))
                f.write("\n")
                fails = []

    with open("fails.txt", "a") as f:
        f.write("\n".join(fails))
        f.write("\n")
