import os.path
import json
import argparse
import sys

from db import db_session, Ad


def load_json_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file:
        return json.load(file)


def parse_command_line_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--filepath',
        help='a JSON file with ads info for database update '
             '(default value: ads.json)',
        default='ads.json',
        type=str,
    )
    command_line_arguments = parser.parse_args()

    return command_line_arguments


def get_flat_list(sequence):
    return [element for subsequence in sequence for element in subsequence]


def get_old_ads_ids(new_ads_ids):
    active_ads_ids = get_flat_list(
        list(db_session.query(Ad.id).filter(Ad.active)),
    )
    return list(set(active_ads_ids) - set(new_ads_ids))


def set_ads_inactive(ads_ids):
    for ad_id in ads_ids:
        ad = db_session.query(Ad).filter(Ad.id == ad_id).first()
        ad.active = False


def is_existing_ad(ad_id):
    return db_session.query(Ad).filter(Ad.id == ad_id).count() > 0


def update_database(new_ads):
    old_ads_ids = get_old_ads_ids(
        new_ads_ids=[ad['id'] for ad in new_ads],
    )
    set_ads_inactive(ads_ids=old_ads_ids)

    for ad in new_ads:
        if is_existing_ad(ad['id']):
            db_session.query(Ad).filter(Ad.id == ad['id']).update(ad)
        else:
            db_session.add(Ad(**ad))

    db_session.commit()


def main():
    command_line_arguments = parse_command_line_arguments()

    filepath = command_line_arguments.filepath

    try:
        ads = load_json_data(filepath)
    except (UnicodeDecodeError, json.JSONDecodeError):
        sys.exit('JSON file has invalid format')

    if ads is None:
        sys.exit('JSON file not found')

    update_database(new_ads=ads)


if __name__ == '__main__':
    main()
