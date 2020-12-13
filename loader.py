
import pandas

from printer import print_header, print_message


def load(config):
    print_header("LOAD START", config, level=1)
    contacts = _load_contacts(config)
    donations = _load_donations(config)
    data = _join(donations, contacts, config)
    print_header("LOAD END", config, level=1)
    return data


def _load_contacts(config):
    contacts = pandas.read_csv(
        config["inputs"]["contacts"] + "Contact_April_2020.csv"
    )
    print_message("- Contacts data loaded", config)
    return contacts


def _load_donations(config):
    donations = pandas.read_csv(
        config["inputs"]["donations"] + "Donation_April_2020.csv"
    )
    print_message("- Donations data loaded", config)
    return donations


def _join(donations, contacts, config):
    data = donations.merge(contacts, how="outer", on="PeopleID")
    print_message("- Donations and contacts merged", config)
    return data


def _check_one_record_per_combination(data, var_one, var_two):
    pass


def _check_one_to_one_values(data, var_one, var_two):
    pass
