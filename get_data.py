import os
import zipfile
from urllib.request import urlretrieve

countries = ["AZ", "GU", "MP", "PR", "US", "VI"]


def get_zip_code_data():
    file_path = "zip"

    if not os.path.exists(file_path):
        os.makedirs(file_path)

    for country in countries:
        print("Get Zip code data for {}".format(country))
        zip_file = os.path.join(file_path, "{}.zip".format(country))
        urlretrieve("http://download.geonames.org/export/{}/{}.zip".format(file_path, country), zip_file)

        zip_ref = zipfile.ZipFile(zip_file, "r")
        zip_ref.extractall(file_path)
        zip_ref.close()

    for extra_file in ["readme.txt"]:
        print("Download {}/{}".format(file_path, extra_file))
        urlretrieve(
            "http://download.geonames.org/export/{}/{}".format(file_path, extra_file),
            os.path.join(file_path, extra_file),
        )


def get_gazzetteer_data():
    file_path = "dump"

    if not os.path.exists(file_path):
        os.makedirs(file_path)

    for country in countries:
        print("Get Gazzetteer data for {}".format(country))
        zip_file = os.path.join(file_path, "{}.zip".format(country))
        urlretrieve("http://download.geonames.org/export/{}/{}.zip".format(file_path, country), zip_file)

    for extra_file in [
        "readme.txt",
        "admin1CodesASCII.txt",
        "admin2Codes.txt",
        "alternateNamesV2.zip",
        "timeZones.txt",
        "countryInfo.txt",
    ]:
        print("Download {}/{}".format(file_path, extra_file))
        urlretrieve(
            "http://download.geonames.org/export/{}/{}".format(file_path, extra_file),
            os.path.join(file_path, extra_file),
        )

    print("Download Feature Codes.")
    urlretrieve(
        "http://www.geonames.org/export/codes.html", os.path.join(file_path, "codes.html"),
    )


if __name__ == "__main__":
    get_zip_code_data()
    get_gazzetteer_data()
